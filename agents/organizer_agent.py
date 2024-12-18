def organize_information(data):
    """
    Organizes the summarized data into sections based on source.
    """
    grouped_results = {}
    for item in data:
        source = item.get("source", "Other")
        grouped_results.setdefault(source, []).append(item)

    organized_text = ""
    for source, items in grouped_results.items():
        organized_text += f"### {source}\n"
        for item in items:
            organized_text += f"- **{item['title']}**:\n  {item['snippet']}\n  [Read More]({item['link']})\n"
    return organized_text
