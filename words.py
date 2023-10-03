def print_upper_words(words):

    for word in words:
        print(word.upper())


def print_upper_words_sw_e(words):

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words_sw(words, that_start_with):

    for word in words:
        for letter in that_start_with:
            if word.startswith(letter):
                print(word.upper())
            

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print("-----------------------")

print_upper_words_sw_e(["hello", "hey", "goodbye", "yo", "yes","elephant"])
print("-----------------------")

print_upper_words_sw(["hello", "hey", "goodbye", "yo", "yes"], that_start_with={"h", "y"})
print("-----------------------")