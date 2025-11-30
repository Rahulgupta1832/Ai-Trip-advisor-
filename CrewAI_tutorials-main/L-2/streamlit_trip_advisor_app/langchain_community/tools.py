# langchain_community/tools.py (stub)
# Minimal stub so `from langchain_community.tools import DuckDuckGoSearchResults` works.

class DuckDuckGoSearchResults:
    def __init__(self, *args, **kwargs):
        pass

    # Some code expects .run or __call__ — provide a simple method
    def run(self, query, max_results=3):
        return [
            {"title": "Stub result 1", "link": "", "snippet": "DuckDuckGo search disabled (stub)."},
            {"title": "Stub result 2", "link": "", "snippet": "Install duckduckgo-search to enable real search."},
        ]

__all__ = ["DuckDuckGoSearchResults"]
