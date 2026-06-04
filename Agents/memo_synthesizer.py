import os
from datetime import datetime
from openai import OpenAI
import retry

class MemoSynthesizer:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GOOGLE_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.model = "gemini-2.5-flash"

    def compile_memo(
            self,
            business_report,
            hiring_report,
            competitor_report
    ):


        today_date = datetime.now().strftime("%B %d, %Y")

        system_prompt = f"""
        You are a General Partner at a top venture capital firm.

        Generate a professional investment memo.

        Use the following header:

        To: Senior Investment Committee
        From: Navin Kumar
        Date: {today_date}

        Sections:
        1. Executive Summary
        2. Opportunity
        3. Business Model
        4. Growth Signals
        5. Competitive Landscape
        6. Risks
        7. Recommendation

        Possible recommendations:
        - INVEST
        - WATCH
        - PASS
        """

        user_content = (
            f"=== RAW BUSINESS REPORT ===\n{business_report}\n\n"
            f"=== RAW HIRING REPORT ===\n{hiring_report}\n\n"
            f"=== RAW COMPETITOR REPORT ===\n{competitor_report}"

        )

        response = retry.call_gemini(
            self.client,
            model=self.model,
            temperature=0.2,  # Low temperature for analytical consistency
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_content
                }
            ]
        )

        return response.choices[0].message.content