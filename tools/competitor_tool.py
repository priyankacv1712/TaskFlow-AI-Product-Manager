import os
import json

from agents import function_tool
from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()


tavily_api_key = os.getenv("TAVILY_API_KEY")

if not tavily_api_key:
    raise ValueError(
        "TAVILY_API_KEY was not found in the .env file."
    )


tavily_client = TavilyClient(
    api_key=tavily_api_key
)


@function_tool
def search_competitor_information(query: str) -> str:
    """
    Search the web for current competitor and product-market information.
    """

    response = tavily_client.search(
        query=query,
        max_results=5,
        include_answer=False
    )

    simplified_results = []

    for result in response.get("results", []):
        simplified_results.append(
            {
                "title": result.get("title"),
                "url": result.get("url"),
                "content": result.get("content")
            }
        )

    return json.dumps(
        simplified_results,
        indent=2
    )
