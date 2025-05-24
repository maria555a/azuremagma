def is_palindrome(text):
    text = text.lower()
    cleaned = ''.join(smbl for smbl in text if smbl.isalnum())

    return cleaned == cleaned[::-1]

text = input("Enter the text: ")
if is_palindrome(text):
    print("True")
else:
    print("False")
