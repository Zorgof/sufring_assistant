"""Surfer Assistant:
Main application entry point for summarizing articles.
"""

from user_controller import UserController
from chunker import Chunker
from models import Models

from transformers.utils.logging import set_verbosity_error

set_verbosity_error()

def save_summary_to_md(summaries, filename="summary.md"):
    """Save summaries to a Markdown file in a readable format."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Article Summary\n\n")
        if isinstance(summaries, list):
            for summary in summaries:
                f.write(f"{summary}\n\n")
        else:
            f.write(f"{summaries}\n\n")

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
        summarizer = Models()
        summaries = summarizer.summarize_chunks(chunks)
        UserController.show_summary(summaries)
        save_summary_to_md(summaries)
        UserController.show_message("Summary saved in *.md file.")
    except ImportError as e:
        UserController.show_message(f"ImportError: {e}")
    except Exception as e:
        UserController.show_message(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()