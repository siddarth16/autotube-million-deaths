from idea_scraper import get_random_death_idea
from script_writer import generate_script
from image_fetcher import fetch_images
from tts_engine import generate_voice
from video_maker import create_video
from uploader import upload_video

def run_autotube():
    print("📌 Step 1: Fetching idea...")
    idea = get_random_death_idea()
    print("👉", idea)

    print("\n🧠 Step 2: Generating narration script...")
    script = generate_script(idea)
    print("🎤", script)

    print("\n🖼️ Step 3: Fetching images from Unsplash...")
    fetch_success = fetch_images(idea)
    if not fetch_success:
        print("❌ Failed to fetch images. Aborting.")
        return

    print("\n🔊 Step 4: Generating voiceover...")
    generate_voice(script)

    print("\n🎞️ Step 5: Creating final video...")
    create_video(script_text=script)

    print("\n🚀 Step 6: Uploading to YouTube...")
    upload_video(
        video_path="tmp/final_video.mp4",
        title=idea,
        description=script
    )

    print("\n✅ Done! One more strange way to die uploaded.")

if __name__ == "__main__":
    run_autotube()
