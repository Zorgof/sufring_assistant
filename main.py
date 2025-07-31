"""Script to summarize content from a URL using a transformer model.
This script fetches content from a provided URL, chunks it into manageable sizes,
and summarizes each chunk using a pre-trained BART model from the Hugging Face Transformers library.
"""
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def get_url_content(url: str) -> str:
    """
    Fetches and extracts main text content from any given URL.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = "\n".join([p.get_text() for p in paragraphs if p.get_text(strip=True)])
    return text

def chunk_text(text, chunk_size=1024):
    """
    Method to chunk text into smaller parts.
    Args:
        text (str): Text to be split into chunks.
        chunk_size (int, optional): Size of single chunk in the output. Defaults to 1024.
    Returns:
        list: List of text chunks.
    """
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

try:
    print("Hi surfer, provide URL to summarize:")
    user_input = input("Enter URL: ")
    
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        device=0
    )

    ARTICLE = get_url_content(user_input.strip())
    if not ARTICLE.strip():
        print("No article content found. Check the URL or page structure.")
        exit(1)

    chunks = chunk_text(ARTICLE, 1024)
    print("Summarizing the article...")

    summaries = []
    for i, chunk in enumerate(chunks):
        try:
            chunk_len = len(chunk)
            max_length = min(int(chunk_len * 0.5), 200)
            min_length = max(int(chunk_len * 0.2), 30)
            if min_length >= max_length:
                min_length = max_length - 1 if max_length > 1 else 1
            summary = summarizer(
                chunk,
                max_length=max_length,
                min_length=min_length,
                do_sample=True,
                early_stopping=True
            )
            summaries.append(summary[0]['summary_text'])
        except Exception as e:
            print(f"Error summarizing chunk {i}: {e}")

    if summaries:
        print("\n".join(summaries))
    else:
        print("No summary generated.")

except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")