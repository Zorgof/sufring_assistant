"""Class for model configuration and summarization of the LLM response.
This module handles the configuration of the summarization model and provides methods to summarize text chunks.
"""

from transformers import pipeline

class Model:
    """Class to control the summarization model."""
    def __init__(self, model_name="facebook/bart-large-cnn", device=0):
        self.summarizer = pipeline(
            "summarization",
            model=model_name,
            device=device
        )

    def summarize_chunks(self, chunks: list) -> list:
        """Summarizes a list of text chunks.
        Args:
            chunks (list): List of text chunks to summarize.
        Returns:
            list: List of summarized text strings.
        """
        summaries = []
        for i, chunk in enumerate(chunks):
            try:
                chunk_len = len(chunk)
                max_length = min(int(chunk_len * 0.5), 200)
                min_length = max(int(chunk_len * 0.2), 30)
                if min_length >= max_length:
                    min_length = max_length - 1 if max_length > 1 else 1
                summary = self.summarizer(
                    chunk,
                    max_length=max_length,
                    min_length=min_length,
                    do_sample=True,
                    early_stopping=True
                )
                summaries.append(summary[0]['summary_text'])
            except Exception as e:
                summaries.append(f"Error summarizing chunk {i}: {e}")
        return summaries