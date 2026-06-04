from Search.search import  MarketSearchTool
from Agents.competitor_agent import CompetitorAgent
search_tool = MarketSearchTool()

def find(s):
    results = search_tool.find_competitors(
        s
    )

    search_context = "\n\n".join(
        [
            f"Title: {item['title']}\n"
            f"Snippet: {item['body']}"
            for item in results
        ]
    )

    competitor_agent = CompetitorAgent()

    competitor_report = competitor_agent.analyze_market(
        s,
        search_context
    )

    return competitor_report