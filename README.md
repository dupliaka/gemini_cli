# Simple Gemini CLI 

This Python script allows you to interact with a Google Gemini model (specifically `gemini-2.0-flash`) from the command line. It takes your input as a prompt and prints the model's response.

## Prerequisites

* **Python 3:** Ensure you have Python 3 installed on your system.
* **`google-generativeai` library:** Install this library using pip:
    ```bash
    pip install google-generativeai
    ```
* **Google Cloud API Key:** You need a Google API key https://aistudio.google.com/apikey copied to .api_key file

## Usage

Open your terminal or command prompt, navigate to the directory where you saved the script, and run it with your prompt as arguments:

```bash
./gm "Answer to the Ultimate Question of Life, The Universe, and Everything"
