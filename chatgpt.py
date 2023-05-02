import openai
from openai.error import RateLimitError

openai.api_key = "openai api key"
model_engine = "gpt-3.5-turbo"

logo = """
 ________  ___  ___  ________  __________   __________   ________    _________   
|\   ____\|\  \|\  \|\   __  \|\___   ___\  \ \   ____\ |\   __  \  |\___   ___\ 
\ \  \___|\ \  \ \  \ \  \|\  \|___ \  \_|   \ \  \___|  \ \  \|\ \ \|___ \  \_| 
 \ \  \    \ \   __  \ \   __  \   \ \  \     \ \  \  __  \ \   ___\     \ \  \  
  \ \  \____\ \  \ \  \ \  \ \  \   \ \  \     \ \  \|\  \ \ \  \___|     \ \  \ 
   \ \_______\ \__\ \__\ \__\ \__\   \ \__\     \ \_______\ \ \__\         \ \__\ 
    \|_______|\|__|\|__|\|__|\|__|    \|__|      \|_______|  \|__|          \|__|
"""

messages = []

def generate_response():
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
        temperature=0,
        stream=True,
    )

    response_str = ""
    for chunk in response:
        try:
            content = chunk["choices"][0]["delta"]["content"]
            for char in content:
                response_str += char
                print(char, end="", flush=True)
        except:
            pass
    print("\n")
    messages.append({"role": "assistant", "content": response_str})

def main():
    print(logo)
    while True:
        try:
            message = input("> ")
            messages.append({"role": "user", "content": message})
            generate_response()
        except RateLimitError as e:
            print(f"3 req/min rate limit reached. Please wait and try again.\n")


if __name__ == "__main__":
    main()
