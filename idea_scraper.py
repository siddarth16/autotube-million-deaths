import random
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_wikipedia_death():
    url = "https://en.wikipedia.org/wiki/List_of_unusual_deaths"
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.content, 'html.parser')

    deaths = []
    for li in soup.select("ul li"):
        text = li.get_text(strip=True)
        if len(text) > 80 and any(year in text for year in ['18', '19', '20']):
            deaths.append(text)

    return random.choice(deaths) if deaths else None

def fetch_reddit_death():
    subreddits = ['UnresolvedMysteries', 'Weird']
    subreddit = random.choice(subreddits)
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=25"

    try:
        res = requests.get(url, headers=HEADERS)
        posts = res.json()['data']['children']
        titles = [post['data']['title'] for post in posts if post['data']['ups'] > 50]
        return random.choice(titles) if titles else None
    except Exception as e:
        print(f"Reddit fetch failed: {e}")
        return None

def get_random_death_idea():
    sources = [fetch_wikipedia_death, fetch_reddit_death]
    random.shuffle(sources)
    for source in sources:
        idea = source()
        if idea:
            return idea
    return "A mysterious death occurred, but details were lost to time..."

# Example run
if __name__ == "__main__":
    print(get_random_death_idea())
