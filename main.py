from pytube import YouTube 
import time
def Download(link , format):
    ti = time.time()
    youtubeObj = YouTube(link)
    if format == 'video':
        youtubeObj = youtubeObj.streams.filter(progressive=True).get_highest_resolution()
    elif format == 'audio' :
        youtubeObj =youtubeObj.streams.filter(abr='160kbps', progressive=False).first()
    else:
        print('format not valid , try again 🥲')
        return
    try :
        youtubeObj.download()
        print('Time taken: {:.0f} sec'.format(time.time() - ti))
        print("Successfully downloaded")
            

    except : 
        print('an error has been occurred while downloading your youtube video')


link = input('Paste your youtube link here ! \n URL:')
format = input('choose the format (video || audio) \n')
Download(link , format)