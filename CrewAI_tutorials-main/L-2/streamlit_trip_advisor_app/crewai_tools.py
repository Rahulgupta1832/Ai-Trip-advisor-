# crewai_tools.py (stub module)

class WebsiteSearchTool:
    def __init__(self, *args, **kwargs):
        pass

    def search(self, query, n=3):
        return [{
            "title": "Search disabled (stub)",
            "url": "",
            "snippet": "Real web search not available in this deployment."
        }]


class ScrapeWebsiteTool:
    def __init__(self, *args, **kwargs):
        pass

    def scrape(self, url):
        return "Scraping disabled (stub)."


def tool(name="generic_tool"):
    def inner(*args, **kwargs):
        return f"Stub tool '{name}' executed."
    return inner


__all__ = ["WebsiteSearchTool", "ScrapeWebsiteTool", "tool"]
