#Adds the prefix 'un' to a given word
def add_prefix_un(word):
    return "un" + word

#Takes a list of vocabulary words and returns a string of words grouped together based on a common prefix
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    return prefix + " :: " + " :: ".join([prefix + word for word in words])

#Removes the suffix 'ness' or 'iness' from a given word, if it is present
def remove_suffix_ness(word):
    if word.endswith("iness"):
        return word[:-5] + "y"
    elif word.endswith("ness"):
        return word[:-4]
    else:
        return word

#Converts an adjective to a verb by adding the suffix 'en'
def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index].strip(",.")
    return adjective + "en"

x=add_prefix_un("happy")
print(x)