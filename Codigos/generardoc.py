import nltk
import random
from nltk.probability import FreqDist
import os

nltk.download('words')

# Obtener todas las palabras del corpus en inglés
english_words = set(nltk.corpus.words.words())

# Calcular la frecuencia de las palabras en inglés
fdist_english = FreqDist(english_words)

# Obtener las 10 palabras más comunes en inglés
top_english = [word for word, _ in fdist_english.most_common(100000000)]

def generate_random_words(N):
    random_words = random.choices(top_english, k=N)
    return random_words

def save_to_file(filename):
    N = 100000000
    with open(filename, 'w') as file:
        words = generate_random_words(N)
        file.write(' '.join(words))
        
if __name__ == "__main__":
    directory = "C:/Users/Sergio/Downloads/corpus/archivoss2"  # Ruta al directorio donde guardar los archivos
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, 21):  # Generar 20 archivos
        filename = os.path.join(directory, f"random_words{i}.txt")
        save_to_file(filename)
