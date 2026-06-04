import os

from dotenv import load_dotenv
import scrape_paritculars

import competitor_func
from Agents.memo_synthesizer import MemoSynthesizer
from Agents.buisness_agent import BusinessAgent
from Agents.business_analyst import BusinessAnalyst
from Agents.hiring_analyst import HiringAnalyst
from Scrapper.web import fetch_website_links, fetch_website_contents

load_dotenv(override=True)
api_key = os.getenv("GOOGLE_API_KEY")


print("=============================================")
print("      AI STARTUP DUE DILIGENCE AGENT         ")
print("=============================================\n")

# Get target company from user input
target_url = input("Enter startup website URL (e.g., https://example.com): ").strip()
if not target_url.startswith("http"):
    target_url = "https://" + target_url

# Initialize components

biz_agent =  BusinessAgent()

print(f"\n Fetching raw links from homepage: {target_url}...")
raw_links = fetch_website_links(target_url)
print(f"Found {len(raw_links)} total raw links.")
if not raw_links:
    print("❌ Could not extract any links. Exiting workflow.")




print(f"\n Analyzing links using Gemini to find business signals...")
analysis_result = biz_agent.filter_relevant_links(target_url, raw_links)
relevant_links = analysis_result.get("links", [])
print(f"✨ Success! Gemini identified {len(relevant_links)} priority internal pages:\n")
# Printing the dict file Directly
for item in relevant_links:
    print(f" 🔹 {item['type'].upper()}: {item['url']}")






company_knowledge_base=scrape_paritculars.scrape_(target_url,relevant_links)


b_analyst=BusinessAnalyst()
summarise_response=b_analyst.analyze_fundamentals(company_knowledge_base)



hiring_analy=HiringAnalyst()
careers_content = company_knowledge_base.get("careers", [])
careers_content = "\n\n".join(careers_content)
if careers_content:
    hiring_report = hiring_analy.calculate_growth_signals(
        careers_content
    )

else:
    hiring_report = "No careers page discovered."
    print(hiring_report)


competitor_report=competitor_func.find(company_knowledge_base["homepage"])


memo_o=MemoSynthesizer()
final_memo=memo_o.compile_memo(summarise_response,hiring_report,competitor_report)
with open(
    "investment_memo.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(final_memo)

from reports.pdf_generator import ReportGenerator
report_generator = ReportGenerator()

html_file = report_generator.generate_html(
    "investment_memo.md"
)
import webbrowser
webbrowser.open_new_tab(html_file)

