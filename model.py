from transformers import pipeline

class Model:
    """Konfiguruje i obsługuje model podsumowujący."""
    def __init__(self, model_name="facebook/bart-large-cnn", device=0):
        self.summarizer = pipeline(
            "summarization",
            model=model_name,
            device=device
        )

    def summarize_chunks(self, chunks):
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