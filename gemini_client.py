#!/usr/bin/env python3

import sys
from google import genai

GOOGLE_API_KEY=""

if __name__ == "__main__":
    with open('.api_key', 'r') as f:
        GOOGLE_API_KEY = f.read().strip()

    prompt = " ".join(sys.argv[1:])
    client = genai.Client(api_key=GOOGLE_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    print(response.text)
