import requests
from serpapi import GoogleSearch
from keybert import KeyBERT
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

kw_model = KeyBERT()


def fetch_serpapi_results(query, num_results=5):
    """Fetch results from SerpAPI."""
    params = {
        "engine": "google",
        "q": query,
        "num": num_results,
        "api_key": SERPAPI_API_KEY,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if "organic_results" not in results:
        return []
    return [
        {
            "title": item["title"],
            "snippet": item["snippet"],
            "link": item["link"],
            "source": "Google",
        }
        for item in results["organic_results"]
    ]


def extract_keywords(text):
    """Extract keywords using KeyBERT."""
    keywords = kw_model.extract_keywords(
        text, keyphrase_ngram_range=(1, 2), stop_words="english"
    )
    return [kw[0] for kw in keywords]


def search_topic(query, num_results=5):
    """
    Search for articles from multiple sources.
    """
    google_results = fetch_serpapi_results(query, num_results)
    # You can add more sources like Semantic Scholar, PubMed, etc.
    all_results = google_results
    return all_results
