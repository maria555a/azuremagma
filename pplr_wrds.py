def popular_words(text, words):
    text = text.lower().split()
    return {word: text.count(word) for word in words}

result = popular_words(
    '''At 9 pm it is already dark and at 7 am it is already light''',
    ['at', 'it', 'is', 'already']
)

print(result)
