#include "HashTable.cpp"

int main() {
    setlocale(LC_ALL, "rus");
    HashTable table(20, 0);

    table.insert_cell("Поттер", "Гарри");
    table.insert_cell("Грейнджер", "Гермиона");
    table.insert_cell("Уизли", "Рональд");
    table.insert_cell("Поттер", "Джеймс");
    table.insert_cell("Малфой", "Драко");
    table.insert_cell("Лестрейндж", "Беллатриса");
    table.insert_cell("Дамблдор", "Альбус");
    table.insert_cell("Снейп", "Северус");
    table.insert_cell("Дигарри", "Седрик");
    table.insert_cell("Лавгуд", "Полумна"); 
    table.insert_cell("Долгопупс", "Невилл");
    table.insert_cell("Пенелопа", "Кристалл");
    table.insert_cell("Забини", "Блейз");

    table.print_table();

    table.insert_cell("Уизли", "Джинни");
    table.insert_cell("Поттер", "Гарри");
    table.print_table();


    return 0;
}
