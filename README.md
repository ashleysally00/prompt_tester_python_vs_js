# GPT API Prompt Tester - Comparing Prompt Requests Written in Python vs. JavaScript

This project demonstrates how to make requests to the OpenAI GPT API using both JavaScript (frontend) and Python (backend). It allows users to test sending prompts and receiving responses from the API, providing a comparison of how API requests and API key handling differ in JavaScript vs. Python.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Setting Up the Environment](#setting-up-the-environment)
  - [Getting an API Key](#getting-an-api-key)
  - [Storing Your API Key](#storing-your-api-key)
- [Running the Project](#running-the-project)
  - [Testing with Python](#testing-with-python)
  - [Testing with JavaScript](#testing-with-javascript)
- [Key Differences Between JavaScript and Python](#key-differences-between-javascript-and-python)
  - [Security Considerations](#security-considerations)
- [How to Write and Test Prompts](#how-to-write-and-test-prompts)

## Overview

This project includes two files, `prompt_tester.py` for Python and `index.html` for JavaScript, that allow you to send prompts to the OpenAI API and receive responses. By running both files, you can observe the differences in how API requests are handled in the backend (Python) vs. the frontend (JavaScript) and see some key security considerations when storing API keys.

# GPT-4 API Prompt Tester

This project demonstrates how to make requests to the OpenAI GPT API using both JavaScript (frontend) and Python (backend). It allows users to test sending prompts and receiving responses from the API, providing a comparison of how API requests and API key handling differ in JavaScript vs. Python.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Setting Up the Environment](#setting-up-the-environment)
  - [Getting an API Key](#getting-an-api-key)
  - [Storing Your API Key](#storing-your-api-key)
- [Running the Project](#running-the-project)
  - [Testing with Python](#testing-with-python)
  - [Testing with JavaScript](#testing-with-javascript)
- [Key Differences Between JavaScript and Python](#key-differences-between-javascript-and-python)
  - [Security Considerations](#security-considerations)
- [How to Write and Test Prompts](#how-to-write-and-test-prompts)

## Overview

This project includes two files, `prompt_tester.py` for Python and `index.html` for JavaScript, that allow you to send prompts to the OpenAI API and receive responses. By running both files, you can observe the differences in how API requests are handled in the backend (Python) vs. the frontend (JavaScript) and see some key security considerations when storing API keys.

## Getting Started

### Requirements

- Python 3.7 or higher
- Basic understanding of HTML and JavaScript
- An OpenAI API key with access to either GPT-4 or GPT-3.5-turbo models

### Setting Up the Environment

1. **Clone the Repository**:

```bash
git clone https://github.com/yourusername/GPT4-API-Prompt-Tester.git
cd GPT4-API-Prompt-Tester
```

2. **Set Up a Virtual Environment (Python)**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python Dependencies**:

```bash
pip install -r requirements.txt
```

### Getting an API Key

To access OpenAI's API, you'll need an API key:

1. Go to OpenAI's API page
2. Sign up for an account or log in
3. Go to API keys and create a new key
4. Copy the key—this will be used in both `prompt_tester.py` (Python) and `index.html` (JavaScript)

### Storing Your API Key

- **Python**: Use a `.env` file to securely store your API key:

  1. Create a `.env` file in the root directory
  2. Add your API key in the following format:

  ```plaintext
  API_KEY=your_openai_api_key_here
  ```

- **JavaScript**: Insert your API key directly in the HTML file for testing purposes. Note that this method is not secure for production.

## Running the Project

### Testing with Python

1. Ensure your `.env` file is set up with your API key
2. Run the Python file:

```bash
python prompt_tester.py
```

3. Enter a prompt when prompted, and the script will return a response from the API

### Testing with JavaScript

1. Open `index.html` in a web browser
2. In the input field, type your prompt and click "Submit"
3. The response will display on the page

## Key Differences Between JavaScript and Python

### API Key Storage

- **Python (Backend)**: The API key is stored in a `.env` file, which is not accessible to users and remains hidden on the server or your local machine. This approach is secure because the key is not exposed to the public.

- **JavaScript (Frontend)**: The API key is stored directly in the HTML file. This exposes the key to anyone who views the page's source code, making it insecure for sensitive information.

### Security Considerations

- **JavaScript API Key Exposure**: When you put your API key in JavaScript, it becomes accessible to anyone who opens the developer tools in their browser. This is a security risk in a production environment because the API key can be misused.

- **Best Practice**: In production, avoid storing API keys in frontend code. Instead, use a backend server to handle API requests securely and send only the required data to the frontend.

## How to Write and Test Prompts

1. **Write a Prompt**: Think of a question or request you'd like GPT-4 to answer. For example, "Generate a list of marketing ideas for a holiday greeting card campaign."

2. **Test the Prompt**:
   - **Python**: Run `prompt_tester.py`, enter the prompt when prompted, and view the response in your terminal.
   - **JavaScript**: Open `index.html` in a browser, type the prompt in the input field, and submit it. The response should appear on the webpage.
