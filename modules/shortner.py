import pyshorteners

def Shortener(url):
    link = pyshorteners.Shortener()
    shortner_url = link.tinyurl.short(url)

    return shortner_url
