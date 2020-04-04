import cv2
import random
import ffmpeg
# Globals

video_path = '[Erai-raws] Kimetsu no Yaiba - 19 [1080p][Multiple Subtitle].mkv'
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

def generate_clip(video_path,start_frame=2000,duration=5):
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
  stream = ffmpeg.output(stream, 'genLoop.gif',s='848x480',y=None)
  # stream = ffmpeg.overwrite_output(stream, 'genLoop.gif',s='640x480')

  ffmpeg.run(stream)


number = generate_start_frame(video_path)
frames = generate_clip(video_path,start_frame=number, duration=4)
write_mp4(frames)
generate_GIF()
