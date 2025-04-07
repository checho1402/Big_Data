#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <thread> // Agregar esta línea
#include <mutex>
#include <sstream>

using namespace std;

const size_t BUFFER_SIZE = 1024 * 1024; // Tamaño del buffer para leer el archivo (1 MB)

void count_words_in_block(const string &block, unordered_map<string, int> &counter, mutex &mtx) {
    stringstream ss(block);
    string word;
    while (ss >> word) {
        lock_guard<mutex> lock(mtx);
        counter[word]++;
    }
}

int main() {
    ifstream file("C:/Users/Sergio/Downloads/corpus/20GB_words.txt", ios::binary);
    if (!file.is_open()) {
        cout << "Error al abrir el archivo\n";
        return EXIT_FAILURE;
    }

    string block;
    unordered_map<string, int> counter;
    mutex mtx;

    // Vector de threads
    vector<thread> threads;

    // Leer el archivo en bloques y procesar cada bloque en un thread
    while (getline(file, block, '\0')) {
        threads.emplace_back(count_words_in_block, block, ref(counter), ref(mtx));
    }

    // Esperar a que todos los threads terminen
    for (auto &thread : threads) {
        thread.join();
    }

    // Imprimir el conteo de palabras
    for (const auto &pair : counter) {
        cout << "{" << pair.first << ": " << pair.second << "}\n";
    }

    return 0;
}
