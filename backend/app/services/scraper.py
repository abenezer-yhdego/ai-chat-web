import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            return f"Failed to retrieve content, status code: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()

    except Exception as e:
        return f"Error: {str(e)}"
