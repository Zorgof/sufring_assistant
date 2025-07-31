import requests
from bs4 import BeautifulSoup

class Chunker:
    """Chunkuje tekst na mniejsze części i pobiera treść z URL."""
    @staticmethod
    def get_url_content(url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs if p.get_text(strip=True)])
        return text

    @staticmethod
    def chunk_text(text, chunk_size=1024):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]