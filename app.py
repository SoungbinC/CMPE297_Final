import streamlit as st
from agents.searcher_agent import search_topic, extract_keywords
from agents.summarizer_agent import summarize_text
from agents.organizer_agent import organize_information


def research_assistant(query, num_results, sources):
    """
    Orchestrates the Multi-Agent Research Assistant pipeline.
    """
    search_results = search_topic(query, num_results=num_results)
    if not search_results:
        return None, "No search results found."

    # Summarize all snippets
    combined_snippets = " ".join([result["snippet"] for result in search_results])
    summary = summarize_text(combined_snippets)

    # Organize results
    organized_output = organize_information(search_results)

    # Extract keywords
    keywords = extract_keywords(combined_snippets)

    return search_results, summary, organized_output, keywords


# Streamlit UI
st.title("Multi-Agent Research Assistant")
st.write("Automate your research with advanced agents!")

# Input for the research topic
topic = st.text_input("Enter your research topic:")
num_results = st.slider("Number of Results", 1, 10, 5)
sources = st.multiselect("Select Sources", ["Google", "PubMed"], default=["Google"])

if st.button("Run Assistant"):
    if topic:
        st.write("Fetching and processing results...")
        try:
            search_results, summary, organized_output, keywords = research_assistant(
                topic, num_results, sources
            )

            if not search_results:
                st.warning("No results found.")
            else:
                # Display raw search results
                with st.expander("View Raw Search Results"):
                    for result in search_results:
                        st.write(f"**{result['title']}**")
                        st.write(result["snippet"])
                        st.write(f"[Read More]({result['link']})")

                # Display summarized content
                with st.expander("View Summarized Content"):
                    st.write(summary)

                # Display organized results
                st.subheader("Organized Results:")
                st.markdown(organized_output)

                # Display keywords
                st.subheader("Key Insights:")
                st.write(", ".join(keywords))

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a research topic.")
