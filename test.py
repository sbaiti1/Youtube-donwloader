import ffmpeg 

video = ffmpeg.input('vid.mp4')
audio = ffmpeg.input('aud.webm')

        
ffmpeg.output(video , audio , 'video1.mp4').run(overwrite_output=True)


