def correct_sentence(text):
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text

user_text = input("Enter text: ")
result = correct_sentence(user_text)
print(result)

