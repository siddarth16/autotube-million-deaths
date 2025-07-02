import os
import requests

UNSPLASH_URL = "https://api.unsplash.com/search/photos"
ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def fetch_images(query, output_dir="tmp/frames", count=3):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    params = {
        "query": query,
        "per_page": count,
        "orientation": "landscape",
        "client_id": ACCESS_KEY
    }

    try:
        res = requests.get(UNSPLASH_URL, params=params)
        res.raise_for_status()
        data = res.json()

        for i, result in enumerate(data["results"][:count]):
            img_url = result["urls"]["regular"]
            img_data = requests.get(img_url).content
            img_path = os.path.join(output_dir, f"image_{i+1}.jpg")
            with open(img_path, "wb") as f:
                f.write(img_data)
            print(f"✅ Saved image: {img_path}")

        return True

    except Exception as e:
        print("❌ Error fetching images:", e)
        return False

# Example test
if __name__ == "__main__":
    fetch_images("mysterious death in shadows")
