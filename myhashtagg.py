import string
text = input("Enter a line: ")

filtered_text = ''.join(sign for sign in text if sign not in string.punctuation)
words = filtered_text.split()
cap_words = [word.capitalize() for word in words]

hashtag = '#' + ''.join(cap_words)
ready_hashtag = hashtag[:140]

print(ready_hashtag)
