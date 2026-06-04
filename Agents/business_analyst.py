# agents/business_analyst.py
from openai import OpenAI
import os
import retry
class BusinessAnalyst:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GOOGLE_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.model = "gemini-3.5-flash"


    def analyze_fundamentals(self, knowledge_base):
        context_text = ""
        for page_type, pages in knowledge_base.items():
            if isinstance(pages, list):
                for page in pages:
                    context_text += f"""
        === {page_type.upper()} ===
        {page}
        """
            else:
                context_text += f"""
        === {page_type.upper()} ===
        {pages}
        """

        system_prompt = """
        You are a venture capital analyst performing first-pass startup due diligence

        Analyze the provided website content and perform a thorough first-pass venture capital due diligence assessment

        Return the following sections:

        1. Company Overview
        2. Problem Being Solved
        3. Product & Solution
        4. Revenue Model
        5. Target Customers
        6. Growth Signals
        7. Competitive Advantages
        8. Potential Risks
        9. Confidence Level

        Rules:
        - Base conclusions only on website evidence
        - If information is unavailable, explicitly state "Not enough evidence"
        - Do not invent facts
        - Be concise and factual
        """

        response = retry.call_gemini(
            self.client,
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context_text}
            ]
        )
        return response.choices[0].message.content