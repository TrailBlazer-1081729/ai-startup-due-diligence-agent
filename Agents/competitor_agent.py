from openai import OpenAI
import os
import retry
from dotenv import load_dotenv

load_dotenv(override=True)
class CompetitorAgent:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("GOOGLE_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.model = "gemini-3.5-flash"

    def analyze_market(
            self,
            company_name,
            search_context
    ):

        system_prompt = """
                        You are an elite venture capital market analyst.
                        
                        Based on search results:
                        
                        1. Identify the most likely competitors.
                        2. Explain why they compete.
                        3. Describe the market landscape.
                        4. Identify competitive threats.
                        5. Identify competitive advantages.
                        
                        Be concise and evidence-based.
                        """

        response = retry.call_gemini(
            self.client,
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content":
                        f"Company: {company_name}\n\n"
                        f"Search Results:\n{search_context}"
                }
            ]
        )

        return response.choices[0].message.content