import os
import time
import getpass
from Email import sendMail

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

path_to_watch = "C:\\Users\\" + getpass.getuser() + "\\Pictures\\MaskMonitoring"
before = dict([(f, None) for f in os.listdir(path_to_watch)])
while 1:
    time.sleep(10)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    # removed = [f for f in before if not f in after]
    if added:
        print("Added: ", ", ".join(added))
        # foreach picture in added:
        # checkForMask.
        # If not WearMask:
        foto = path_to_watch + "\\" + added[0]
        if (getSize(foto) > 100000):
            sendMail(foto)
    # if removed:
    #     print("Removed: ", ", ".join(removed))
    before = after
