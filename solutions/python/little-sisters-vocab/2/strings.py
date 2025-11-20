"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    
    # 1. Extract the prefix (the first element).
    prefix = vocab_words[0]
    
    # 2. Extract the list of words (everything after the first element).
    words = vocab_words[1:]
    
    # 3. Create a new list starting with the prefix itself.
    # We iterate through 'words' and prepend the prefix to each.
    prefixed_group = [prefix] + [prefix + word for word in words]
        
    # 4. Join the list into a single string with the " :: " separator.
    return " :: ".join(prefixed_group)
    


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    # 1. Remove the last 4 characters ("ness")
    clean_word = word[:-4]
    
    # 2. Check for the spelling rule exception.
    # If the new word ends in "i", it was originally a "y".
    # Example: "heaviness" -> "heavi" -> "heavy"
    if clean_word.endswith("i"):
        return clean_word[:-1] + "y"
        
    # 3. Otherwise, return the word with the suffix simply removed.
    # Example: "sadness" -> "sad"
    return clean_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    # 1. Split the sentence into a list of individual words.
    words_list = sentence.split()
    
    # 2. Extract the target word using the index.
    target_word = words_list[index]
    
    # 3. Clean the word.
    # Words in sentences often have punctuation attached (e.g., "dark.").
    # We strip common punctuation marks to get the raw adjective.
    clean_word = target_word.strip(".,!?;:")
    
    # 4. Transform to verb.
    # If the word ends in 'e' (like "white" or "wide"), just add 'n'.
    if clean_word.endswith("e"):
        return clean_word + "n"
        
    # Otherwise, add "en" (like "dark" -> "darken").
    return clean_word + "en"
