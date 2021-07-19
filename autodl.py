from services.cutter import autodlCutter
from services.video import autodlVideo
from services.audio import autodlAudio
from ascii.ascii import selectOption

def Start():
    selectOption()
    user = input("[Select Option]: ")

    #Choices
    cutter = ["C","c"]
    video = ["V", "v"]
    audio = ["A", "a"]

    for i in range(len(cutter)):
        if user == cutter[i]:autodlCutter()
        elif user == video[i]:autodlVideo()
        elif user == audio[i]:autodlAudio()
    else: print("Bye! ")

Start()


