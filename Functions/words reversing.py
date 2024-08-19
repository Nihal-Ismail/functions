sentence = input("Enter a Sentence:")
def master_yoda(sentance):
    # creating list of words
    words = []
    for word in sentance.split(' '):
        words.append(word)

    terminator = ""
    # If the sentance ends with a dot(.) we need to extract that
    if words[-1].endswith('.') or words[-1].endswith('?'):
        terminator = words[-1][-1]
        words[-1] = words[-1][:-1]

    # reversing the words
    words.reverse()

    # recreating the sentance with reversed words
    new_sentance = " ".join(words)
    new_sentance = new_sentance + terminator
    return new_sentance
print(master_yoda(sentence))