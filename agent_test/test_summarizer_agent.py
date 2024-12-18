from transformers import pipeline

# Import the summarization function
from agents.summarizer_agent import summarize_text

# Sample text for testing
test_text = """
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines
that are programmed to think and learn. AI is revolutionizing industries, from healthcare
to finance, enabling automation, improving efficiencies, and creating new opportunities.
The future of AI involves enhanced natural language processing, computer vision, and
reinforcement learning techniques.
"""

# Test summarization
if __name__ == "__main__":
    try:
        summary = summarize_text(test_text)
        print("Original Text:\n", test_text)
        print("\nSummary:\n", summary)
    except Exception as e:
        print(f"Error during summarization: {e}")
