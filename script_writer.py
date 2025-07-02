import os
import openai
from idea_scraper import get_random_death_idea

# Use environment variable for security (set in GitHub Actions or Render)
openai.api_key = os.getenv("GROQ_API_KEY")
openai.base_url = "https://api.groq.com/openai/v1"

def generate_script(idea):
    prompt = (
        f"Write a short 30-second YouTube narration script about this strange way to die:\n\n"
        f"{idea}\n\n"
        "Make it dramatic, eerie, and engaging. Avoid jokes. Keep it tight and intriguing."
    )

    response = openai.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()

# Example run
if __name__ == "__main__":
    idea = get_random_death_idea()
    print("DEATH IDEA:\n", idea)
    print("\nSCRIPT:\n", generate_script(idea))
