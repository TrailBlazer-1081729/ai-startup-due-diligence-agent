from openai import OpenAI
import os
import retry
class HiringAnalyst:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GOOGLE_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        self.model = "gemini-3.5-flash"

    def calculate_growth_signals(self, careers_content):

        if not careers_content:
            return "No careers page found."

        system_prompt = """
            You are a venture capital hiring and organizational growth analyst.
            Analyze the provided careers page content.
            Determine:
            1. Hiring intensity
            2. Functions being prioritized
               - Engineering
               - Product
               - Sales
               - Marketing
               - Operations
               - Customer Success
            
            3. Seniority distribution
               - Entry-level
               - Mid-level
               - Senior
               - Executive
            
            Infer:
            
            - Growth Velocity (HIGH / MODERATE / CONSERVATIVE)
            - Evidence supporting the conclusion
            - Organizational focus
            
            Rules:
            - Use only evidence found in the provided text
            - Do not invent facts
            - If evidence is insufficient, explicitly say so
            - Be concise and objective
            """

        response = retry.call_gemini(
            self.client,
            model=self.model,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": careers_content
                }
            ]
        )

        return response.choices[0].message.content