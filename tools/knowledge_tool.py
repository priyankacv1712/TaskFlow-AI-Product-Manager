from pathlib import Path

from agents import function_tool


@function_tool
def search_taskflow_knowledge(query: str) -> str:
    """
    Search TaskFlow's internal product knowledge base
    for information relevant to the supplied query.
    """

    project_root = Path(__file__).resolve().parent.parent
    knowledge_dir = project_root / "knowledge_base"

    documents = []

    for file_path in knowledge_dir.glob("*.md"):

        content = file_path.read_text(
            encoding="utf-8"
        )

        documents.append(
            {
                "file": file_path.name,
                "content": content
            }
        )

    query_terms = query.lower().split()

    scored_documents = []

    for document in documents:

        text = document["content"].lower()

        score = sum(
            1
            for term in query_terms
            if term in text
        )

        if score > 0:

            scored_documents.append(
                (
                    score,
                    document
                )
            )

    scored_documents.sort(
        key=lambda item: item[0],
        reverse=True
    )

    if not scored_documents:

        return (
            "No relevant TaskFlow internal "
            "knowledge was found."
        )

    top_results = scored_documents[:3]

    response_parts = []

    for score, document in top_results:

        response_parts.append(
            f"""
SOURCE: {document["file"]}

{document["content"]}
"""
        )

    return "\n".join(response_parts)