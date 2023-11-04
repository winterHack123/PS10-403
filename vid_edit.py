from moviepy.editor import VideoFileClip

video_path = "downloads/Tom & Jerry ｜ Jerry in Full Force 🐭 ｜ Classic Cartoon Compilation ｜ @WB Kids.mp4"
clip = VideoFileClip(video_path)

new_height = 720
new_width = 9*new_height/16


x1 = (clip.size[0] - new_width) / 2
x2 = x1 + new_width
y1 = (clip.size[1] - new_height) / 2
y2 = y1 + new_height

cropped_clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

cropped_clip.write_videofile("vertical_video.mp4", codec="libx264")