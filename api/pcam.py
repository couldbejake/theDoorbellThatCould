import os
import datetime
from time import localtime, strftime


def saveNextImage():
    folder_path = strftime("images/%Y-%m-%d", localtime())
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    picture_path = folder_path + strftime("/%H-%M-%S.jpg", localtime())

    os.system ("fswebcam -S 50 -D 1 -r 1280x720 --no-banner "+picture_path)
    return picture_path
