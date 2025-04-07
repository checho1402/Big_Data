import threading

global_counter = {}  # Diccionario global para almacenar el conteo de palabras
lock = threading.Lock()  # Lock para sincronización


def count_words_in_block(lines):
    local_counter = {}  # Diccionario local para el conteo de palabras en el bloque

    for line in lines:
        words = line.split()
        for word in words:
            if word in local_counter:
                local_counter[word] += 1
            else:
                local_counter[word] = 1

    # Sincronizar la actualización del diccionario global usando el lock
    with lock:
        for word, count in local_counter.items():
            if word in global_counter:
                global_counter[word] += count
            else:
                global_counter[word] = count


def main():
    myfile = open("random_words.txt", "r")
    threads = []

    mylist = myfile.readlines()
    for line in mylist:
        lines = []
        lines.append(line)
        thread = threading.Thread(target=count_words_in_block, args=(lines,))
        thread.start()
        threads.append(thread)


    # Esperar a que todos los threads terminen
    for thread in threads:
        thread.join()

    # Imprimir el conteo de palabras
    for word, count in global_counter.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
