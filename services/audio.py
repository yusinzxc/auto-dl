from process import Audio
from ascii.ascii import selectFormat
def autodlAudio():
    url = input("Paste video/audio URL from: ")
    autodl = Audio(url)
    autodl.audio()
