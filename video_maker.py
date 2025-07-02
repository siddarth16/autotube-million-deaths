from moviepy.editor import *
import os
import glob

def create_video(script_text, frames_dir="tmp/frames", audio_path="tmp/voice.wav", output_path="tmp/final_video.mp4", duration=30):
    image_paths = sorted(glob.glob(os.path.join(frames_dir, "*.jpg")))
    if not image_paths:
        raise Exception("❌ No images found in tmp/frames")

    # Calculate duration per image
    clip_duration = duration / len(image_paths)

    # Create image clips
    clips = []
    for img_path in image_paths:
        img = ImageClip(img_path).set_duration(clip_duration).resize(height=720)
        clips.append(img)

    # Concatenate image clips
    video_clip = concatenate_videoclips(clips, method="compose")

    # Add audio
    audio_clip = AudioFileClip(audio_path)
    video_clip = video_clip.set_audio(audio_clip)

    # Add subtitle
    subtitle = TextClip(script_text, fontsize=36, font="Arial-Bold", color="white", method="caption", size=video_clip.size)
    subtitle = subtitle.set_duration(duration).set_position("center")

    # Final composition
    final_video = CompositeVideoClip([video_clip, subtitle])
    final_video.write_videofile(output_path, fps=24, audio_codec='aac')

# Example
if __name__ == "__main__":
    sample_text = "In 1997, a man died while trying to pet a lion through the bars of a zoo cage. He didn’t survive the encounter."
    create_video(sample_text)
