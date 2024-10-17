def PrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split()

    for index, word in enumerate(words, start=1):

        if word.startswith(searchWord):
            return index  # Return the 1-based index

    return -1  # Return -1 if no prefix is found
print(PrefixOfWord("i love eating burger", "burg"))  # Output: 4
