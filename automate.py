# sudo fswebcam -S 50 -r 1280x720 --no-banner image3.jpg


from api import psettings as ps
from api import pnotification as pn
from api import plogging as logger
from api import pcam

import subprocess
import time
import sys

try:
	import RPi.GPIO as GPIO
	pass
except ImportError:
	print("ERROR: Can not import RPi.GPIO!")
	print("This is required for detecting when there's a signal from the doorbell")
	print("If you are already using Raspbian install rpi.gpio using 'sudo apt-get -y install python3-rpi.gpio'")
	print("(Please read the documentation for more information)")
	sys.exit()
  
GPIOMODE = GPIO.BCM
DOORBELL_GPIO = 17
NAME = "couldhome"
VERSION = "0.1b"
PUSHED_CREDEITIALS = ps.loadSettings()

# Initialize global variables
custom_messages = {}
nm = None

def randomMessage(messages):
	return nm.getRandomNotif(custom_messages[messages])

def setup():
	# Set up the log into the p_log directory
	logger.setuplog('logs/log-%Y-%m-%d.txt')
	logger.log("Starting {} version {}".format(NAME, VERSION))
	logger.log("Loading PUSHED credentials")

	# Load the Notification Manager
	global nm
	nm = pn.notificationManager(PUSHED_CREDEITIALS, logger)

	# Load custom message files into the custom messages array.
	custom_messages["doorbell"] = nm.loadMessages("messages/doorbell.json")

	# Setup the GPIO pins
	logger.log("Setting up GPIO Pins")

	GPIO.setmode(GPIOMODE)
	GPIO.setup(DOORBELL_GPIO, GPIO.IN)
	logger.log("Setting up doorbell RPi GPIO Pin "+str(DOORBELL_GPIO))

def main():
	logger.log("Done!")

	while True:
		if (GPIO.input(DOORBELL_GPIO) == True):
		#if (input() != "adasd"):
			time.sleep(2)
			logger.log("Doorbell pressed on pin {}".format(DOORBELL_GPIO))
			img_dir = pcam.saveNextImage()
			#print(img_dir)
			logger.log("Photo has been saved!")

			#url = "http://pinewood.thesunflowergeneration.com/doorbell/"+img_dir
			url = "http://pinewood.thesunflowergeneration.com/doorbell/"
			nm.messageAllURL(randomMessage("doorbell"), url, True)
			time.sleep(10)

if __name__ == '__main__':
	setup()
	try:
		main()
	except KeyboardInterrupt:
		logger.log("Stopping {} version {}".format(NAME, VERSION))
		logger.stopmsg()



