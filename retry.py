import time

def call_gemini(client, **kwargs):

    for attempt in range(5):
        try:
            return client.chat.completions.create(**kwargs)

        except Exception as e:

            if "429" in str(e) or "503" in str(e):
                wait = 2 ** attempt
                print(f"Retrying in {wait}s...")
                print(e)
                time.sleep(wait)
            else:
                raise

    raise Exception("Gemini failed after 5 retries")