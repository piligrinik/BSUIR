#include "HashTable.h"
#include <iomanip>


inline int get_char_index(char c) {
    if (c >= 'À' && c <= 'ß') {
        return c - 'À';
    }
    if (c >= 'à' && c <= 'ÿ') {
        return c - 'à';
    }
    throw std::invalid_argument("Invalid character");
}

inline int make_v(const string& key) {
    return get_char_index(key[0]) * 33 + get_char_index(key[1]);
}

inline int HashTable::hash_func(int v) {
    return v % capacity + begin_numerate;
}

inline int HashTable::line_search(int i) {
    int number = 1;
    for (number = 1; i + (number * this->q) < 20; number++)
    {
        if(table[i + (q * number)] == nullptr)
            return i + (this->q * number);
    }
    return -1;
}

inline HashTable::HashTable(int capacity, int begin_enumerate) {
    this->capacity = capacity;
    this->begin_numerate = begin_enumerate;
    size = id = 0;
    table.resize(capacity, nullptr);
}

inline HashTable::~HashTable() {
    for (Cell* cell : table) {
        delete cell;
    }
}

inline void HashTable::insert_cell(string key, string data) {
    int v = make_v(key);
    int index = hash_func(v);
    while (table[index] != nullptr && table[index]->key != key) {
        index = line_search(index);

    }

    if (table[index] != nullptr && table[index]->key == key) {
        if (table[index]->data != data)
        {
            index = line_search(index);
        }
        else table[index]->data = data;

    }
    if (table[index] != nullptr && table[index]->key == key && table[index]->data == data)
    {
    }
    else
    {
        table[index] = new Cell(key, data);
        ++size;
        table[index]->id = ++id;
    }
}

inline string HashTable::get_cell_data(string key) {
    int v = make_v(key);
    int index = hash_func(v);

    while (table[index] != nullptr) {
        if (table[index]->key == key) {
            return table[index]->data;
        }
        index = line_search(index);
    }

    return "";
}

inline void HashTable::delete_cell(string key) {
    int v = make_v(key);
    int index = hash_func(v);

    while (table[index] != nullptr) {
        if (table[index]->key == key) {
            delete table[index];
            table[index] = nullptr;
            --size;
            return;
        }
        index = line_search(index);
    }
}

inline void HashTable::print_table() {
    cout << setw(10) << " ID" << setw(25) << "Key" << setw(30) << "Data" << endl;
    for (int i = 0; i < capacity; ++i) {
        if (table[i] != nullptr) {
            cout<< setw(10) << " ID" << table[i]->id << setw(25) << table[i]->key << setw(30) << table[i]->data << endl;
        }
        else {
            cout << endl;
        }
    }
}