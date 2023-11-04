import moviepy.editor as me
import pandas as pd

def create_vid(filename, res, ):
    video_path = "downloads/" + filename
    clip = me.VideoFileClip(video_path).without_audio()

    new_height = res
    new_width = 9*new_height/16

    speed = 1.25

    x1 = (clip.size[0] - new_width) / 2
    x2 = x1 + new_width
    y1 = (clip.size[1] - new_height) / 2
    y2 = y1 + new_height

    cropped_clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

    x=10
    dur = 5

    clips = []

    clip1 = cropped_clip.subclip(0,10).speedx(speed)

    clips.append(clip1)

    clip1.write_videofile("vertical_video.mp4", codec="libx264")