import requests


def fetch_text(url):
    if not isinstance(url, str) or not url.startswith("http"):
        raise ValueError("Invalid URL")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching URL: {e}")