from transformers import pipeline
import os
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import pipeline

# Load environment variables
load_dotenv()

# Get Hugging Face token from the .env file
huggingface_token = os.getenv("HUGGINGFACE_TOKEN")

if not huggingface_token:
    raise ValueError("Hugging Face token not found in .env file.")

# Login to Hugging Face
login(token=huggingface_token)
# Use a more powerful summarizer
summarizer = pipeline("summarization", model="t5-small", device=-1)


def chunk_text(text, max_chunk_size=512):
    """Split text into smaller chunks."""
    words = text.split()
    return [
        " ".join(words[i : i + max_chunk_size])
        for i in range(0, len(words), max_chunk_size)
    ]


def summarize_text(text, max_length=150):
    """
    Summarizes the input text by chunking if necessary.
    """
    chunks = chunk_text(text)
    summaries = [
        summarizer(chunk, max_length=max_length, do_sample=False)[0]["summary_text"]
        for chunk in chunks
    ]
    return " ".join(summaries)
