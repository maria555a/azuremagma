def is_palindrome(text):
    text = text.lower()
    edited_line = ''.join(smbl for smbl in text if smbl.isalnum())

    return edited_line == edited_line[::-1]

text = input("Enter the text: ")
if is_palindrome(text):
    print("True")
else:
    print("False")
