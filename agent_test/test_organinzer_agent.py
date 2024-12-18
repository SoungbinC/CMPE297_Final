from agents.organizer_agent import organize_information

# Sample input data
sample_data = [
    {
        "title": "OpenAI",
        "snippet": "OpenAI is a leading AI research organization.",
        "link": "https://openai.com",
    },
    {
        "title": "Google AI",
        "snippet": "Google AI focuses on advancing AI for societal benefit.",
        "link": "https://ai.google",
    },
    {
        "title": "AI Ethics",
        "snippet": "AI ethics explores the responsible use of artificial intelligence.",
        "link": "https://example.com/ai-ethics",
    },
]

# Test the organizer agent
if __name__ == "__main__":
    organized_output = organize_information(sample_data)
    print("Organized Results:\n")
    print(organized_output)
