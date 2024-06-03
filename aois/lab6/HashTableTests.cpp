#include "pch.h"
#include "CppUnitTest.h"
#include "..//aois6/HashTable.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace HashTableTests
{
	TEST_CLASS(HashTableTests)
	{
	public:
		
		TEST_METHOD(TestMethod1)
		{
			HashTable ht(20, 0);
			ht.insert_cell("Поттер", "Гарри");
			ht.insert_cell("Грейнджер", "Гермиона");
			ht.insert_cell("Уизли", "Рональд");
			ht.insert_cell("Малфой", "Драко");

			ht.delete_cell("Поттер");
			ht.insert_cell("Поттер", "Джеймс");
\
			Assert::AreEqual(string("Джеймс"), ht.get_cell_data("Поттер"));
		}

		TEST_METHOD(TestMethod2)
		{
			HashTable ht(20, 0);
			ht.insert_cell("Поттер", "Гарри");
			ht.insert_cell("Грейнджер", "Гермиона");
			ht.insert_cell("Уизли", "Рональд");
			ht.insert_cell("Малфой", "Драко");

			ht.print_table();

			ht.delete_cell("Поттер");
			ht.print_table();
			Assert::AreEqual(string(""), ht.get_cell_data("Поттер"));
		}

		TEST_METHOD(TestMethod3)
		{
			HashTable ht(20, 0);

			ht.insert_cell("Лестрейндж", "Беллатриса");
			ht.insert_cell("Дамблдор", "Альбус");
			ht.insert_cell("Снейп", "Северус");
			ht.insert_cell("Дигарри", "Седрик");
			ht.insert_cell("Лавгуд", "Полумна");
			ht.insert_cell("Долгопупс", "Невилл");

			ht.print_table();

			ht.delete_cell("Дамблдор");
			ht.insert_cell("Поттер", "Джеймс");
			Assert::AreEqual(string("Северус"), ht.get_cell_data("Снейп"));

		}
	};
}
