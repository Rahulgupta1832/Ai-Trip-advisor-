# crewai/tools.py (Stub tools module)

class WebsiteSearchTool:
    def __init__(self, *args, **kwargs):
        pass

    def search(self, query, n=3):
        return [{
            "title": "Stub Search",
            "url": "",
            "snippet": "Web search is disabled in deployed version."
        }]

class ScrapeWebsiteTool:
    def __init__(self, *args, **kwargs):
        pass

    def scrape(self, url):
        return "Scraping disabled in stub mode."

def tool(name="generic_tool"):
    def _inner(*args, **kwargs):
        return f"{name}: Stub tool executed."
    return _inner

__all__ = ["WebsiteSearchTool", "ScrapeWebsiteTool", "tool"]
