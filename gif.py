from   moviepy.editor import*

print('imported')
clip = VideoFileClip('08.mp4')

print('video uploaed')
clip.write_gif('mygif.gif')