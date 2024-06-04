#include "HashTable.cpp"
#include <iostream>

int main() {
    setlocale(LC_ALL, "rus");
    HashTable table(20, 0);

    table.new_cell("Поттер", "Гарри");
    table.new_cell("Грейнджер", "Гермиона");
    table.new_cell("Уизли", "Рональд");
    table.new_cell("Поттер", "Джеймс");
    table.new_cell("Малфой", "Драко");
    table.new_cell("Лестрейндж", "Беллатриса");
    table.new_cell("Дамблдор", "Альбус");
    table.new_cell("Снейп", "Северус");
    table.new_cell("Дигарри", "Седрик");
    table.new_cell("Лавгуд", "Полумна"); 
    table.new_cell("Долгопупс", "Невилл");
    table.new_cell("Пенелопа", "Кристалл");
    table.new_cell("Забини", "Блейз");

    table.print_table();

    table.new_cell("Уизли", "Джинни");
    table.new_cell("Поттер", "Гарри");
    cout << "================================================================================" << endl;
    table.print_table();


    return 0;
}
