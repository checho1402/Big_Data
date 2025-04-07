import nltk
import random

nltk.download('words')

word_list = nltk.corpus.words.words()

def generate_random_words(N):
    random_words = random.choices(word_list, k=N)
    return random_words

def save_to_file(filename):
    N = 1000000
    with open(filename, 'w') as file:
        words = generate_random_words(N)
        for i in range(2000):
            file.write(' '.join(words))
save_to_file('random_words3.txt')