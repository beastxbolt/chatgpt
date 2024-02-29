# ChatGPT Integration with Python OpenAI Library

## Overview
This Python script allows you to integrate the OpenAI GPT-3.5 model into your application for conversational AI purposes.

## Prerequisites
- Python 3.x installed on your system.
- An OpenAI API key. You can obtain one by signing up at the [OpenAI website](https://openai.com/).

## Installation
1. Clone or download the script from this repository.
2. Install the required library:
   ```pip install openai```

## Usage
1. Replace `"openai api key"` in the script with your actual OpenAI API key.
2. Run the script:
   ```python chatgpt.py```

The inputs and responses are stored temporarily in the list ``messages``. Therefore, the model responds according to the past conversations.
The script also streams the model's response in the console/terminal.
