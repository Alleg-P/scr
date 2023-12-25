# Задача 1: Переверни слова

def invert(words):
    line = words.split()
    inverted_words = []
    for word in line:
        inverted_words.append(word[::-1])
    print(" ".join(inverted_words))


invert("Hello World")
invert("Python")
