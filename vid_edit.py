import moviepy.editor as me
import pandas as pd

def create_vid(res, ts, length):

    video_path = "downloads/video.mp4"

    clip = me.VideoFileClip(video_path)

    new_height = res
    new_width = 10*new_height/16

    speed = 1

    x1 = (clip.size[0] - new_width) / 2
    x2 = x1 + new_width
    y1 = (clip.size[1] - new_height) / 2
    y2 = y1 + new_height

    cropped_clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

    v_clips = []
    a_clips = []

    for i in range(length):
        ac = me.AudioFileClip('Speech/speech' + str(i+1) + '.mp3')
        a_clips.append(ac)
        vc = cropped_clip.subclip(ts[i], ts[i] + speed*ac.duration).speedx(speed)
        v_clips.append(vc)

    final_audio = me.concatenate_audioclips(a_clips)
    final_video = me.concatenate_videoclips(v_clips)

    final_video = final_video.set_audio(final_audio)

    final_audio.write_audiofile("final_audio.mp3",codec = 'mp3')

    final_video.write_videofile("final.mp4",codec='libx264', audio_codec='aac')