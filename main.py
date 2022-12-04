from pytube import YouTube 

def Download(link):
    youtubeObj = YouTube(link)
    youtubeObj = youtubeObj.streams.get_highest_resolution()
    try :
        youtubeObj.download()
    except : 
        print('an error has been occurred while downloading your youtube video')

    print("Successfully downloaded")

link = input('Paste your youtube link here ! \n URL:')
Download(link)