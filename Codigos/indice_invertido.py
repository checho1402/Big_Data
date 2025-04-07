import os
import re
import nltk
import pickle
from nltk.stem import PorterStemmer
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Guardar el diccionario en un archivo
def save_index(inverted_index, filename):
    with open(filename, 'wb') as file:
        pickle.dump(inverted_index, file)

# Cargar el diccionario desde un archivo
def load_index(filename):
    with open(filename, 'rb') as file:
        inverted_index = pickle.load(file)
    return inverted_index

def preprocess_text(text):
    # Tokenización
    words = nltk.word_tokenize(text)
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]

    return stemmed_words

def process_file(filename):
    inverted_index = defaultdict(set)
    with open(filename, 'r', encoding='utf-8') as file:
        for linea in file:
            text = linea.strip().lower()  # Leer el contenido del archivo y convertir a minúsculas
            words = preprocess_text(text)
            for word in words:
                inverted_index[word].add(filename)
    return inverted_index

def build_inverted_index(directory):
    inverted_index = defaultdict(set)
    filenames = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith(".txt")]
    print(filenames)
   
    with ThreadPoolExecutor() as executor:
        results = executor.map(process_file, filenames)

    for result in results:
        for word, files in result.items():
            inverted_index[word].update(files)
            
       

    print(inverted_index)
    save_index(inverted_index,"dccionario2.pkl")
    return inverted_index

def search(query, inverted_index):
    query_words = preprocess_text(query.lower())
    result = None

    for word in query_words:
        if result is None:
            result = inverted_index.get(word, set())
        else:
            result = result.intersection(inverted_index.get(word, set()))

    return result

if __name__ == "__main__":
    
    directory = "C:/Users/Sergio/Downloads/corpus/archivoss2"  

    # Construir el índice invertido
    #inverted_index = build_inverted_index(directory)
    
    inverted_index = load_index('dccionario.pkl')
    print(len(inverted_index))
    
    

    query = input("query: ")
    result = search(query, inverted_index)
    print("Resultados de la búsqueda para la consulta '{}':".format(query))
    print(result)
