def sort_letters_in_words(sentence):
    sorted_words = [''.join(sorted(word)) for word in sentence.split()]
    return ' '.join(sorted_words)

input_sentence = "привет мир"
output_sentence = sort_letters_in_words(input_sentence)
print(output_sentence)