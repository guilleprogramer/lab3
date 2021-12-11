import os


def convert_to_VP8(video, new_video):
    os.system('ffmpeg - i '+video+' - c: v libvpx - b: v 1 M - c: a libvorbis '+new_video)

def convert_to_VP9(video, new_video):
    os.system('ffmpeg -i '+video+' -c:v libvpx-vp9 -b:v 2M'+new_video)

    #if we change the bit rate we will obtain different results with more or less quality in the two cases-

def convert_to_h265(video, new_video):
    os.system('ffmpeg -i '+video+' -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k '+new_video)



    #we can work with different crf values to provide a better quality. Then we can change the preset with other
    #speeds.

def convert_to_av1(video, new_video):
    os.system('ffmpeg -i '+video+' -c:v libaom-av1 -crf 30 -b:v 0 '+new_video)


convert_to_VP8('BBB.mp4', 'BBB_vp8.webm')
convert_to_VP9('BBB.mp4', 'BBB_vp9.webm')
convert_to_h265('BBB.mp4', 'BBB_h265.mp4')
convert_to_av1('BBB.mp4', 'BBB_av1.mvk')


def combine_videos(video1, video2):
    os.system('ffplay -v warning -f rawvideo -s 800x400 -i /dev/zero -vf movie='+video1+',scale=400x400 [mv2] ; movie='+video2+',scale=400x400 [mv1]; [in][mv1] overlay=0:0 [tmp]; [tmp][mv2] overlay=400:0')

combine_videos('BBB_vp8.webm', 'BBB_vp9.webm')


def stream(video, ip):
    os.system('ffmpeg -i ' + video + ' -v 0 -vcodec mpeg4 -f mpegts udp://' + ip)


stream('BBB.mp4', '127.0.0.1:23000')
