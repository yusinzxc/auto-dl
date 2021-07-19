
def cmdCutter(
        url, ss, to, 
        filename, fileformat):
    return f"ffmpeg $(youtube-dl -f bestvideo+bestaudio -g  '{url}' | sed 's/^/-ss {ss} -to {to} -i /') {filename}.{fileformat}"


def cmdVideo(url, quality):
    if quality == "B" or quality == "b":
        return f"youtube-dl -f bestvideo+bestaudio '{url}'"
    elif quality == "H" or quality == "h":
        return f"youtube-dl -f bestvideo'[height<=720]'+bestaudio '{url}'"

    elif quality == "L" or quality == "l":
        return f"youtube-dl -f bestvideo'[height<=360]'+bestaudio '{url}'" 


def cmdAudio(url):
    return f"youtube-dl --extract-audio --audio-format mp3 -o '%(title)s.%(ext)s' {url}"
