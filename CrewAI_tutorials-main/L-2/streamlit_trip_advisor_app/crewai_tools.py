# crewai_tools.py (stub)
class WebsiteSearchTool:
    def __init__(self,*a,**k): pass
    def search(self, query, n=3):
        return [{"title":"Search disabled (stub)","url":"","snippet":"Install crewai_tools to enable real search."}]

class ScrapeWebsiteTool:
    def __init__(self,*a,**k): pass
    def scrape(self, url): return "Scraping disabled (stub)."

__all__ = ["WebsiteSearchTool","ScrapeWebsiteTool"]
