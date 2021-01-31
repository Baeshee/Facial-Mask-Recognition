import os
import time
import getpass
from Email import sendMail


def getSize(filename):
    st = os.stat(filename)
    return st.st_size


def startWatchingNoMaskFolder():
    # Change the path to the location you save your No_Mask files
    path_to_watch = "C:/Users/" + getpass.getuser() + "/Pictures/MaskMonitoring/ZonderMasker"
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while 1:
        time.sleep(5)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if not f in before]
        if added:
            print("Added: ", ", ".join(added))
            for file in added:
                foto = path_to_watch + "/" + file
                sendMail(foto)
        before = after
