import os
from cmd import *

class AutoDl:
    def __init__(self, url):
        self.url = url


class Cutter(AutoDl):
    def __init__(self, url, filename, fileformat):
        super().__init__(url)
        self.filename = filename
        self.fileformat = fileformat


    def cutter(self, ss, to):
        os.system(cmdCutter(
            self.url, ss, to,
            self.filename, self.fileformat
        ))
        

class Video(AutoDl):
    def __init__(self, url, quality):
        super().__init__(url)
        self.quality = quality

    def video(self):
        os.system(cmdVideo(
            self.url, self.quality
        ))


class Audio(AutoDl):
    def __init__(self, url):
        super().__init__(url)

    def audio(self):
        os.system(cmdAudio(self.url))


   
