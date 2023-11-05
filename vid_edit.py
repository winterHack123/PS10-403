from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips, concatenate_videoclips, CompositeAudioClip

def create_vid(res, ts, length):

    video_path = "downloads/video.mp4"
    clip = VideoFileClip(video_path).without_audio()

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
        ac = AudioFileClip('Speech/speech' + str(i + 1) + '.mp3')
        a_clips.append(ac)
        if ts[i] == ts[i-1]:
            ts[i] = ts[i-1] + prev_duration
        vc = cropped_clip.subclip(ts[i], ts[i] + ac.duration)
        prev_duration = ac.duration
        v_clips.append(vc)

    music_audio  = AudioFileClip('music\Still-Awake-Lofi-Study-Music(chosic.com).mp3').subclip(32,130)

    final_audio = concatenate_audioclips(a_clips)
    final_video = concatenate_videoclips(v_clips)

    music_audio = music_audio.set_duration(final_audio.duration)
    final_audio = CompositeAudioClip([final_audio,music_audio.volumex(0.4)])

    final_audio = final_audio.set_duration(final_video.duration)
    final_video = final_video.set_audio(final_audio)

    final_audio.write_audiofile('final_audio.mp3',fps = 44100)
    final_video.write_videofile("final.mp4")