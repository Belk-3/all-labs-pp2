# 6. Reverse words in a sentence
def reverse_sentence(sentence):
    result = ' '.join(sentence.split()[::-1])
    print(f"Reversed sentence: {result}")
    return result
