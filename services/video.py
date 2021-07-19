from process import Video
from ascii.ascii import *
def autodlVideo():
    url = input("Paste video/audio URL from: ")
    selectQuality()
    quality = input("[Select Quality]: ")

    autodl = Video(url,quality)
    autodl.video()
