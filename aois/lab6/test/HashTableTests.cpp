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
			ht.new_cell("Поттер", "Гарри");
			ht.new_cell("Грейнджер", "Гермиона");
			ht.new_cell("Уизли", "Рональд");
			ht.new_cell("Малфой", "Драко");

			ht.delete_cell("Поттер");
			ht.new_cell("Поттер", "Джеймс");
\
			Assert::AreEqual(string("Джеймс"), ht.get_cell_info("Поттер"));
		}

		TEST_METHOD(TestMethod2)
		{
			HashTable ht(20, 0);
			ht.new_cell("Поттер", "Гарри");
			ht.new_cell("Грейнджер", "Гермиона");
			ht.new_cell("Уизли", "Рональд");
			ht.new_cell("Малфой", "Драко");

			ht.print_table();

			ht.delete_cell("Поттер");
			ht.print_table();
			Assert::AreEqual(string(""), ht.get_cell_info("Поттер"));
		}

		TEST_METHOD(TestMethod3)
		{
			HashTable ht(20, 0);

			ht.new_cell("Лестрейндж", "Беллатриса");
			ht.new_cell("Дамблдор", "Альбус");
			ht.new_cell("Снейп", "Северус");
			ht.new_cell("Дигарри", "Седрик");
			ht.new_cell("Лавгуд", "Полумна");
			ht.new_cell("Долгопупс", "Невилл");

			ht.print_table();

			ht.delete_cell("Дамблдор");
			ht.new_cell("Поттер", "Джеймс");
			Assert::AreEqual(string("Северус"), ht.get_cell_info("Снейп"));

		}
	};
}
