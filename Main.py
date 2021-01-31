from threading import Thread
from Email import setEmailData
from Watcher import startWatchingNoMaskFolder
from FaceMaskRecognition import startFaceRecognition

if __name__ == "__main__":
    setEmailData()
    t1 = Thread(target=startWatchingNoMaskFolder)
    t1.setDaemon(True)
    t1.start()
    startFaceRecognition()
    # t1.join() <-- causes a subprocess to hang after main script is closed...
