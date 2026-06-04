import markdown2


class ReportGenerator:

    def generate_html(
            self,
            markdown_file,
            output_file="investment_memo.html"
    ):

        with open(markdown_file, "r", encoding="utf-8") as f:
            md_content = f.read()

        html_body = markdown2.markdown(md_content)

        html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">

<style>

body {{
    font-family: Segoe UI, Arial, sans-serif;
    max-width: 1000px;
    margin: 0 auto;
    padding: 40px;
    line-height: 1.8;
    color: #222;
    background-color: #fafafa;
}}

.report-header {{
    text-align: center;
    padding: 30px;
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    margin-bottom: 40px;
}}

.report-title {{
    font-size: 42px;
    font-weight: bold;
}}

.report-subtitle {{
    color: #666;
    margin-top: 10px;
}}

.content {{
    background: white;
    padding: 40px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}}

h1 {{
    font-size: 34px;
    border-bottom: 3px solid #111827;
    padding-bottom: 12px;
}}

h2 {{
    background-color: #f3f4f6;
    padding: 12px;
    border-left: 6px solid #2563eb;
    border-radius: 4px;
}}

h3 {{
    color: #374151;
}}

p {{
    font-size: 16px;
}}

li {{
    margin-bottom: 8px;
}}

</style>

</head>

<body>

<div class="report-header">

    <div class="report-title">
        AI Startup Due Diligence Report
    </div>

    <div class="report-subtitle">
        Prepared by Navin Kumar
    </div>

</div>

<div class="content">

{html_body}

</div>

</body>
</html>
"""

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        return output_file