from Scrapper.web import fetch_website_links, fetch_website_contents

def scrape_(target_url,relevant_links):
    print("\n Scraping priority pages to build corporate context...")
    company_knowledge_base = {
        "homepage": fetch_website_contents(target_url)
    }

    for item in relevant_links:
        page_type = item['type'].lower()
        page_url = item['url']
        print(f" 📑 Scraping {page_type}...")
        if page_type not in company_knowledge_base:
            company_knowledge_base[page_type] = []
        content=fetch_website_contents(page_url)
        company_knowledge_base[page_type].append(content)
    return company_knowledge_base
