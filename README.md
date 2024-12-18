# Multi-Agent Research Assistant

This project implements a **Multi-Agent Research Assistant** using multiple agents for **searching**, **summarizing**, and **organizing** research articles based on user input. It leverages models from Hugging Face for summarization and custom search logic to fetch results from various sources.

## Features

-   **Searcher Agent**: Fetches articles and information from APIs like **SerpAPI**, **Google**, and others.
-   **Summarizer Agent**: Summarizes the fetched content using the `t5-small` model from Hugging Face.
-   **Organizer Agent**: Organizes the results into structured bullet points, making it easier to digest.

## Scalability

The **Multi-Agent Research Assistant** is designed to be scalable, with the ability to extend the following:

1. **Search Sources**:
    - Currently, the assistant fetches results using APIs such as **SerpAPI**. You can scale it by adding more data sources, such as **PubMed**, **Semantic Scholar**, and **Bing**.
    - You can integrate academic databases for more in-depth and specialized research.
2. **Summarizer Models**:
    - Currently, the assistant uses the **`t5-small`** model for summarization. For larger datasets or more complex content, you can scale by switching to larger models like **`t5-base`**, **`flan-t5-large`**, or even **`facebook/bart-large-cnn`**.
3. **Organizing Results**:
    - The current implementation organizes results into bullet points, but this can be expanded to include additional categories, such as **key findings**, **keywords**, or **citations**.

## Limitations

### Search Results

Due to limitations in the **API used** (such as **SerpAPI**, which is restricted to a limited number of results per query), the current implementation fetches a maximum of **two to five results** per search query. However, there are multiple ways to **scale** this:

1. **Increase Results per Query**: Adjust the parameters to retrieve more results from the APIs if supported.
2. **Use Multiple Sources**: Fetch results from multiple APIs or sources, such as **Google**, **Bing**, **Semantic Scholar**, and **PubMed**, to gather more comprehensive research material.
3. **Pagination**: Implement pagination to retrieve more results by making multiple requests to the API, increasing the overall number of results fetched.

### API Limitations

Currently, the **SerpAPI** or any API used has a limit to how many results can be fetched. In production environments, consider upgrading to premium versions of APIs or integrating multiple APIs to provide more comprehensive results. For larger-scale use cases, you can also **scrape** data from web pages directly (ensure that scraping follows legal and ethical guidelines).

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/multi-agent-research-assistant.git
    cd multi-agent-research-assistant
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Make sure to create a .env file in the root directory containing your Hugging Face token for model access and API keys for search services:
    ```makefile
    HUGGINGFACE_TOKEN=your_hugging_face_token
    SERP_API_KEY=your_serp_api_key
    ```
4. Run the application:
    ```bash
    streamlit run app.py
    ```

---

## How It Works

### 1. **Input Topic**

The user inputs a research topic they want to explore.

### 2. **Search**

The **Searcher Agent** fetches results using APIs like **SerpAPI**. You can scale by adding more sources or using other APIs.

### 3. **Summarization**

The **Summarizer Agent** processes the fetched results, reducing them to concise summaries using the **`t5-small`** model.

### 4. **Organization**

The **Organizer Agent** organizes the summarized results into bullet points, making the data easy to digest.

### 5. **Visualization**

Streamlit is used to create an interactive interface where users can view raw search results, summaries, and organized results.

---

## Scalability and Extensibility

### 1. **Additional Data Sources**

-   To scale your search results, you can integrate other search APIs or academic databases.
-   For instance, **Bing Search API** or **PubMed** can be used to fetch more specialized research results.

### 2. **Better Summarization Models**

-   You can replace `t5-small` with larger models like **`t5-base`**, **`flan-t5-large`**, or **`facebook/bart-large-cnn`** for more complex summarization.

### 3. **Advanced Result Organization**

-   Future versions of the organizer can include more advanced structuring such as **keywords extraction**, **key insights**, or **citations**.

---

## Future Improvements

-   **Pagination for Search Results**: Implement a pagination system to retrieve more results for each query.
-   **More Sources for Summarization**: Extend summarization capabilities with domain-specific models or more comprehensive data.
-   **Multilingual Support**: Add support for summarizing and searching in multiple languages.

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Please ensure that you adhere to the coding standards and write unit tests for any new features.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Conclusion

This project is designed to automate the research process using **multiple agents** and can easily be scaled by adding more sources, improving summarization quality, and enhancing result organization. The limitations in the search results can be addressed by using multiple APIs or implementing pagination, providing an easy path for further expansion.
