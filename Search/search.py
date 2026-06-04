from ddgs import DDGS

class MarketSearchTool:

    def find_competitors(self, company_name):

        query = f"{company_name} competitors alternatives"

        try:

            with DDGS(timeout=20) as ddgs:

                results = list(
                    ddgs.text(
                        query,
                        max_results=5
                    )
                )

            return results

        except Exception as e:

            print(f"Search failed: {e}")

            return []