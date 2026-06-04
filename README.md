# AI Startup Due Diligence Agent

An AI-powered multi-agent system that performs first-pass venture capital due diligence by analyzing startup websites, extracting business intelligence, evaluating hiring activity, researching competitors, and generating structured investment memos

## Project Overview

Performing startup due diligence manually requires gathering information from multiple sources, understanding the company's business model, evaluating growth indicators, and researching competitors.

This project automates the first-pass due diligence process.

Given a startup website URL, the system:

1. Discovers important business pages.
2. Scrapes relevant company information.
3. Analyzes the business model and target market.
4. Evaluates hiring activity as a growth signal.
5. Identifies competitors and market positioning.
6. Generates a structured investment memo.
7. Produces a shareable HTML report.

The goal is to simulate the initial research workflow performed by venture capital analysts and investors.

## Why I Built This

Venture capital analysts spend significant time collecting information about startups before making investment decisions.

This project explores how AI agents can automate parts of that workflow by gathering public information from company websites and transforming it into structured investment research.

The goal is not to replace human judgment, but to accelerate the initial research process and surface key business insights more efficiently


## Example

Input:

```text
https://www.zepto.com
```

Output:

```text
✓ Business Overview
✓ Revenue Model
✓ Hiring Analysis
✓ Competitor Research
✓ Growth Signals
✓ Investment Recommendation
```

## Sample Insights Generated

The generated investment memo can include:

- Company Overview
- Problem Being Solved
- Product & Solution Analysis
- Revenue Model Assessment
- Target Customer Identification
- Hiring & Growth Signals
- Competitive Landscape Analysis
- Risk Assessment
- Investment Recommendation (INVEST / WATCH / PASS)

  

## Features

- Automatically discovers and filters business-relevant website pages
- Builds a company knowledge base from scraped content
- Performs AI-driven business model analysis
- Evaluates hiring activity as a proxy for growth
- Identifies competitors using web search
- Generates venture-capital-style investment memos
- Produces shareable HTML reports

  ## Workflow

```text
Startup Website URL
        │
        ▼
Website Scraper
        │
        ▼
Business Agent
(Link Selection)
        │
        ▼
Content Scraper
        │
        ▼
Company Knowledge Base
        │
        ├──────────────► Business Analyst
        │
        ├──────────────► Hiring Analyst
        │
        └──────────────► Competitor Research
                                │
                                ▼
                        Competitor Agent
                                │
                                ▼
                        Memo Synthesizer
                                │
                                ▼
                     Investment Memo (.md)
                                │
                                ▼
                      HTML Report Generator
                                │
                                ▼
                          Final Report
```


## Repository Structure

```text
AI_Startup_Due_Diligence_Agent
│
├── Agents
│   ├── business_agent.py
│   ├── business_analyst.py
│   ├── competitor_agent.py
│   ├── hiring_analyst.py
│   └── memo_synthesizer.py
│
├── Search
│   └── search.py
│
├── Scrapper
│   └── web.py
│
├── reports
│   └── pdf_generator.py
│
├── competitor_func.py
├── scrape_paritculars.py
├── retry.py
├── main.py
├── requirements.txt
└── .env.example
```

## Screenshots

### Link Discovery & Scraping & Analysis

<img width="1813" height="878" alt="Screenshot 2026-06-04 065329" src="https://github.com/user-attachments/assets/af6a1d60-ebca-4abf-9378-a87e4d1a1d57" />


### Generated Report

<img width="1547" height="852" alt="Screenshot 2026-06-04 065350" src="https://github.com/user-attachments/assets/24e1ff96-f3b5-41f5-a80f-429cd377ffc9" />

## Tech Stack

- Python
- Gemini API
- OpenAI-Compatible SDK
- BeautifulSoup
- Requests
- DDGS Search
- Markdown2
- HTML/CSS

## Installation

```bash
git clone <repo-url>
cd ai-startup-due-diligence-agent
pip install -r requirements.txt
```

## Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_api_key_here


## Usage

```bash
python main.py
```

Example:

```text
Enter startup website URL:
https://www.zepto.com
```

## Example Output

- Company Overview
- Business Model
- Growth Signals
- Competitive Landscape
- Risks
- Recommendation


## Challenges Faced

During development, several practical challenges had to be addressed:

- Filtering hundreds of irrelevant website links while retaining business-critical pages
- Handling Gemini API rate limits and retry logic
- Extracting useful information from inconsistent website structures
- Managing websites with missing or incomplete content
- Designing a multi-stage AI pipeline where outputs from one agent become inputs to another

## Current Limitations

- Analysis quality depends on publicly available website content
- Some websites may block scraping or expose limited information
- Competitor discovery relies on search-engine results
- No financial statement analysis is currently performed


## Future Improvements

- Interactive Web Dashboard
- PDF Export
- Multi-Company Comparison
- Startup Scoring System
- Financial Data Integration
- Vector Database Support
- Historical Trend Analysis





