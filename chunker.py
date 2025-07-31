"""Chunker Module for text processing.
This module provides functionality to chunk text into smaller parts and fetch content from a URL."""

import requests
from bs4 import BeautifulSoup

class Chunker:
    """Chunks text and fetches content from a URL."""
    @staticmethod
    def get_url_content(url: str) -> str:
        """Fetches content from a given URL.
        Args:
            url (str): The URL to fetch content from.
        Returns:
            str: The text content of the URL.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs if p.get_text(strip=True)])
        return text

    @staticmethod
    def chunk_text(text : str, chunk_size=1024) -> list:
        """Chunks text into smaller parts.
        Args:
            text (str): The text to chunk.
            chunk_size (int): The maximum size of each chunk.
        Returns:
            list: A list of text chunks.
        """
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]