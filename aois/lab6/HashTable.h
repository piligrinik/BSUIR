#pragma once
#include "Cell.cpp"

class HashTable {
private:
    vector<Cell*> table;
    int capacity;
    int size;
    int begin_enumerate;
    int id;
    int q = 1;
    int hash_foo(const string& key);

    int line_search(int);

public:
    HashTable(int capacity, int baseAddress);

    ~HashTable();

    void new_cell(string key, string data);

    string get_cell_info(string key);

    void delete_cell(string key);

    void print_table();
};