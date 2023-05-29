Prefix and Suffix Manipulation Functions

This code includes several functions for manipulating prefixes and suffixes of words. These functions can be used to modify words and create new words based on specific rules.

add_prefix_un(word)
Description: This function takes a word as input and adds the prefix "un" to it.
Parameters:

word (string): The word to which the prefix will be added.
Returns:
The modified word with the "un" prefix added.
make_word_groups(vocab_words)
Description: This function takes a list of vocabulary words and groups them together based on a common prefix. It returns a string of words separated by "::".
Parameters:

vocab_words (list of strings): The list of vocabulary words.
Returns:
A string of words grouped together based on a common prefix.
remove_suffix_ness(word)
Description: This function removes the suffix "ness" or "iness" from a given word, if it is present.
Parameters:

word (string): The word from which the suffix will be removed.
Returns:
The modified word with the "ness" or "iness" suffix removed, or the original word if the suffix is not present.
adjective_to_verb(sentence, index)
Description: This function converts an adjective to a verb by adding the suffix "en" to the specified adjective in a given sentence.
Parameters:

sentence (string): The sentence containing the adjective to be converted.
index (integer): The index of the adjective in the sentence (0-based index).
Returns:
The modified sentence with the adjective converted to a verb by adding "en" as a suffix.