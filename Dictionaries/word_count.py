def count_word_frequency(words):
    
    words_count = {}

    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    
    print(words_count)

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words)
