from process import Cutter
from ascii.ascii import *
def autodlCutter():
    url = input("Paste video/audio URL from: ")
    filename = input("Name: ")
    selectFormat()
    fileformat = input("[Select Format]: ")
    print()

    #Video Format
    if fileformat == "V" or fileformat == "v":
        fileformat = "mp4"

    #Audio Format
    elif fileformat == "A" or fileformat == "a":
        fileformat = "mp3"

    cutterExample()
    ss,to = input("[ss-to]: ").split()
    print()

    autodl = Cutter(url, filename, fileformat)
    autodl.cutter(ss,to)

