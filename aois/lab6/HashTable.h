#pragma once
#include "Cell.cpp"

class HashTable {
private:
    vector<Cell*> table;
    int capacity;
    int size;
    int begin_numerate;
    int id;
    int q = 1;
    int hash_func(int v);

    int line_search(int);

public:
    HashTable(int capacity, int baseAddress);

    ~HashTable();

    void insert_cell(string key, string data);

    string get_cell_data(string key);

    void delete_cell(string key);

    void print_table();
};