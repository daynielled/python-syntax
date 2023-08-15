def print_upper_words(words):
    for word in words:
        print(word.upper())

def print_words_with_e(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print (word)

def must_start_with(word_list, begininng_letter):
    for word in word_list:
        if word[0].lower() in begininng_letter:
            print(word)

        #     for word in words:
        # for letter in must_start_with:
        #     if word.startswith(letter):
        #         print(word.upper())
        #         break