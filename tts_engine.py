import requests
import time
import os

TTS_API = "https://api-inference.huggingface.co/models/suno/bark"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}

def generate_voice(text, output_path="tmp/voice.wav"):
    payload = {
        "inputs": text,
        "parameters": {"do_sample": True}
    }

    response = requests.post(TTS_API, headers=HEADERS, json=payload)
    
    if response.status_code == 503:
        print("Model is loading on HuggingFace... waiting 10 seconds")
        time.sleep(10)
        return generate_voice(text, output_path)

    if response.ok:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print("✅ Voice generated:", output_path)
    else:
        print("❌ Error:", response.text)

# Example use
if __name__ == "__main__":
    sample_text = "In 1997, a man died trying to pet a lion through a zoo cage."
    generate_voice(sample_text)
