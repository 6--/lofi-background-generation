import cv2
import random
import ffmpeg
import kromo
from PIL import Image
import numpy
# Globals

video_path = '[bonkai77] Your Name (Kimi no Na wa)  [BD-1080p] [DUAL-AUDIO] [x265] [HEVC] [AAC] [10bit].mkv'
frame_number = 643
import time

def get_video_properties(video_path):

  video = cv2.VideoCapture(video_path)
  length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  width = int(video.get(3))
  height = int(video.get(4))
  fps = int(round(video.get(5)))

  video.release()
  cv2.destroyAllWindows()

  properties_tuple = (length, width, height, fps) 
  return properties_tuple

def generate_clip(video_path,start_frame=2000,duration=4.2):
  length, width, height, fps = get_video_properties(video_path)


  video = cv2.VideoCapture(video_path)
  clip_length = int(fps * duration)
  frames_array = []

  video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

  for frame_number in range(clip_length):
    ret, frame = video.read()
    frames_array.append(frame)

  video.release()
  cv2.destroyAllWindows()
  return frames_array


def write_images():
  pass

def write_mp4(frames_array):
  length, width, height, fps = get_video_properties(video_path)
  out = cv2.VideoWriter('genGIF.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))
  for frame in frames_array:
    out.write(frame)

  out.release()
  cv2.destroyAllWindows()
  return None


def generate_start_frame(video_path):
  length, width, height, fps = get_video_properties(video_path)
  random_number = random.randrange(0,length)
  return random_number

def generate_GIF():
  stream = ffmpeg.input('genGIF.avi')
  # stream = ffmpeg.overwrite_output(stream)
  stream = ffmpeg.output(stream, 'genLoop.gif',s='640x360',y=None)
  # stream = ffmpeg.overwrite_output(stream, 'genLoop.gif',s='640x480')

  ffmpeg.run(stream)

# def add_fx(frames,strength=1.0,jitter=1.0):
#   fx_frames = []
#   for frame in frames:
#     frame = cv2.resize(frame,(640,360))
#     frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     winname = 'asd'
#     cv2.imshow(winname,frame)
#     im = Image.fromarray(frame)
#     time.sleep(12)
#     print('done frame')

#     if (im.size[0] % 2 == 0 or im.size[1] % 2 == 0):
#       if (im.size[0] % 2 == 0):
#         im = im.crop((0, 0, im.size[0] - 1, im.size[1]))
#         im.load()
#       if (im.size[1] % 2 == 0):
#         im = im.crop((0, 0, im.size[0], im.size[1] - 1))
#         im.load()

#     og_im = im.copy()
#     im = kromo.add_chromatic(im, strength=strength)
#     # im = kromo.add_jitter(im, pixels=jitter)
#     # im = kromo.blend_images(im, og_im, alpha=0.0, strength=strength)
#     im = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
    
#     im = cv2.resize(im,(640,360))

#     fx_frames.append(im)
#   return fx_frames



number = generate_start_frame(video_path)
frames = generate_clip(video_path,start_frame=number, duration=4.2)
# frames = add_fx(frames)
write_mp4(frames)
generate_GIF()
