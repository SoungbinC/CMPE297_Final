from agents.searcher_agent import search_topic


# Define test inputs
test_query = "Artificial Intelligence"
num_results = 3

# Test the searcher agent
if __name__ == "__main__":
    print("Testing Searcher Agent...")
    try:
        results = search_topic(test_query, num_results)
        if results:
            for i, result in enumerate(results, start=1):
                print(f"\nResult {i}:")
                print(f"Title: {result['title']}")
                print(f"Snippet: {result['snippet']}")
                print(f"Link: {result['link']}")
                print(f"Source: {result.get('source', 'Unknown')}")
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error testing searcher agent: {e}")
