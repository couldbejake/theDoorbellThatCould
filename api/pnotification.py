import requests
import json
import random
import sys

PUSHED_CREDEITIALS = None
LOGGER = None

class notificationManager():

    # Pushed Custom API
    
    def __init__(self, credentials, logger):
        global PUSHED_CREDEITIALS, LOGGER
        PUSHED_CREDEITIALS = credentials
        LOGGER = logger

    def pushPayload(self, payloadSend):
        try:
            request = requests.post("https://api.pushed.co/1/push", data=payloadSend)
            self.responseDecipher(request)
        except ConnectionError as e:
            print(e)
            print("ERROR: You may have exceeded your max push limit.")

    # todo will add logger
    def responseDecipher(self, requestIn):
        if(requestIn.status_code == 200):
            return True
        else:
            LOGGER.log("Error Sending request to Pushed Server\n")
            LOGGER.log("-- [ Response {} ] --".format(requestIn.status_code))
            LOGGER.log(str(json.loads(requestIn.text)))
            LOGGER.log("----")
            if(json.loads(requestIn.text)['error']['type'] == "app_credentials_are_not_valid"):
                print("***********")
                print("\nYour application credentials are invalid!\nThey appear as the following lengths:\n")
                print("app_key => \n********************\n")
                print("app_secret => \n****************************************************************\n")
                print("target_type -> \nchannel\n")
                print("target_alias => \n******\n")
                sys.exit("***********")
                      
    def messageAll(self, message):
        temppayload = PUSHED_CREDEITIALS
        temppayload['content'] = message
        self.pushPayload(temppayload)
        LOGGER.log("Sent message to PUSHED Server")

    def messageAllURL(self, message, url, visit_suggestion = False):
        temppayload = PUSHED_CREDEITIALS
        if(visit_suggestion):
            temppayload['content'] = message + "\n\n( Tap here for front door cam )"
        else:
            temppayload['content'] = message
        temppayload['content_type'] = 'url'
        temppayload['content_extra'] = url
        self.pushPayload(temppayload)
        LOGGER.log("Sent message with URL to PUSHED Server")

    # Custom Messages
    def loadMessages(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
        totalChance = 0
        messages = data["messages"]
        for message in messages:
            message["text"]
            totalChance+= int(message["chance"])
            
        if(totalChance != 100):
            print("WARNING: '{}' message chance does not add up to 100%".format(path))
        return messages

    def getRandomNotif(self, message_file):
        LOGGER.log("Fetching random response message")
        random_index = random.randint(0, 100)
        message_scan = 0
        for message in message_file:
            message_duration = int(message["chance"])
            if(random_index >= message_scan and random_index <= message_scan + message_duration):
                return message['text']
            message_scan += message_duration
        LOGGER.log("ERROR: Error fetching message text!")
        return "Error fetching message text!"
        

