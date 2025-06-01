import re

def first_word(text):
    match = re.search(r"[a-zA-Z']+", text)
    return match.group(0) if match else ''

print(first_word("Hello world"))
