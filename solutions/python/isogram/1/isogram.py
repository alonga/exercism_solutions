def is_isogram(word):
    word = word.lower().replace(" ","").replace("-","")
    return len(word) == len(set(word))