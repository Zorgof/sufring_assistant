"""Surfer Assistant:
Main application entry point for summarizing articles.
"""

from user_controller import UserController
from chunker import Chunker
from model import Model

from transformers.utils.logging import set_verbosity_error

set_verbosity_error()

def main():
    """Main function to run the Surfer Assistant application."""
    try:
        url = UserController.get_url()
        article = Chunker.get_url_content(url)
        if not article.strip():
            UserController.show_message("No article content found. Check the URL or page structure.")
            return
        chunks = Chunker.chunk_text(article, 1024)
        UserController.show_message("Summarizing the article...")
        summarizer = Model()
        summaries = summarizer.summarize_chunks(chunks)
        UserController.show_summary(summaries)
    except ImportError as e:
        UserController.show_message(f"ImportError: {e}")
    except Exception as e:
        UserController.show_message(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()