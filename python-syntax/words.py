def print_upper_words(words):
    """Print each word on sep line, uppercased.

        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """
#this will create that loop and return all uppercase
    for word in words:
        print(word.upper())

def print_upper_words2(words):
   
#this will only print words with upper or lowercase e
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

#this will allow you to pass in your own variable of what to start with
def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break