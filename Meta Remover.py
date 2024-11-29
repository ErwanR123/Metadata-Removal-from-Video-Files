from moviepy.editor import *
import os

def remove_metadata(video_path):
    try:
        video = VideoFileClip(video_path)
        new_video_path = os.path.splitext(video_path)[0] + "_no_metadata" + os.path.splitext(video_path)[1]
        new_video = video.set_audio(None)
        print(f"Output video path: {new_video_path}")
        new_video.write_videofile(new_video_path, codec='libx264', audio_codec='aac')
    except Exception as e:
        print(f"Error: {e}")


remove_metadata('/path/to/your/video.mp4')
