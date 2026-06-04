import os
import json
from openai import OpenAI
import retry

class BusinessAgent:
    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("GOOGLE_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.model = "gemini-3.5-flash"

        self.link_system_prompt = """
        You are an AI analyst assisting with startup due diligence

        You will receive a list of links discovered on a company's website

        Your goal is to identify pages that help an investor understand:

        - What the company does
        - Products and services
        - Target customers
        - Pricing and business model
        - Team and leadership
        - Hiring activity and growth signals
        - Customer success stories and case studies
        - Company news and announcements

        Prioritize pages such as:

        - About
        - Product
        - Platform
        - Solutions
        - Pricing
        - Customers
        - Case Studies
        - Team
        - Leadership
        - Careers
        - Blog
        - News
        - Contact

        Exclude pages such as:

        - Privacy Policy
        - Terms of Service
        - Cookie Policy
        - Legal pages
        - Login pages
        - Signup pages
        - Password reset pages
        - Mailto links
        - Social media links
        - JavaScript links

        Return ONLY valid JSON

        Expected format:

        {
          "links": [
            {
              "type": "about",
              "url": "https://example.com/about"
            },
            {
              "type": "careers",
              "url": "https://example.com/careers"
            }
          ]
        }

        Do not include explanations, markdown, or additional text
        """

    def filter_relevant_links(self, target_url, raw_links):
        user_prompt = f"""
        You are performing startup due diligence.

        Website:
        {target_url}

        Below is a list of links discovered on the website.

        Your task:
        1. Select only the pages that would be useful for understanding the business.
        2. Prioritize pages such as:
           - About
           - Products
           - Solutions
           - Pricing
           - Customers
           - Case Studies
           - Team
           - Careers
           - Blog
           - Contact
        3. Exclude:
           - Terms of Service
           - Privacy Policy
           - Cookie Policy
           - Legal pages
           - Login pages
           - Signup pages
           - mailto links
           - javascript links
        4. Return only valid absolute HTTPS URLs.
        5. Select at most:
            - 1 About page
            - 1 Careers page
            - 1 Pricing page
            - Up to 3 Product pages
            - Up to 3 Customer pages
            - Up to 2 Blog/News pages
            - 1 contact page 
        6. Avoid duplicate URLs.
        7. Prefer the most representative page when multiple pages serve the same purpose.
        
        Links:
        {chr(10).join(raw_links)}
        """

        try:
            response = retry.call_gemini(
                self.client,
                model=self.model,
                temperature=0,
                messages=[
                    {"role": "system", "content": self.link_system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                response_format={"type": "json_object"}
            )

            result_text = response.choices[0].message.content
            return json.loads(result_text)
        except Exception as e:
            print(f"Error filtering links with AI: {e}")
            return {"links": []}