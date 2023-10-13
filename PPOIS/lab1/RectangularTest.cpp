#include "pch.h"
#include "CppUnitTest.h"
#include <vector>
#include "..//Rectangular/Rectangular.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace RectangularTest
{
	TEST_CLASS(RectangularTest)
	{


		TEST_METHOD(TestMethodGetDimentions)
		{

			Rectangular r1(1, 3, 1, 4);
			std::vector <int> Expectation = { 1, 3, 1, 4 };
			std::vector <int> Result = { r1.GetX1(), r1.GetX2(), r1.GetY1(), r1.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodChangeSize)
		{
			Rectangular r1(0,1 ,0, 3);
			int x1 = r1.GetX1() + 1;
			int x2 = r1.GetX2() + 2;
			int y1 = r1.GetY1() + 1;
			int y2 = r1.GetY2() + 0;
			std::vector <int> Expectation = { x1, x2, y1, y2 };
			r1.changeSize(1, 2, 1, 0);
			std::vector <int> Result = { r1.GetX1(), r1.GetX2(), r1.GetY1(), r1.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodPostIncrement)
		{
			Rectangular r1(0, 1, 0, 1);
			std::vector <int> Expectation = { r1.GetX1(), r1.GetX2() + 1, r1.GetY1(), r1.GetY2() + 1 };
			r1++;
			std::vector <int> Result = { r1.GetX1(), r1.GetX2(), r1.GetY1(), r1.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodPostDecrement)
		{
			Rectangular r1(0, 1, 0, 1);
			std::vector <int> Expectation = { r1.GetX1(), r1.GetX2() - 1, r1.GetY1(), r1.GetY2() - 1 };
			r1--;
			std::vector <int> Result = { r1.GetX1(), r1.GetX2(), r1.GetY1(), r1.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodAddition)
		{
			Rectangular r1(0,1,0,1);
			Rectangular r2(1, 3, 1, 4);
			std::vector <int> Result = { 0, 3, 0, 4 };
			Rectangular r3(0,1,0,1);
			r3 = r1 + r2;
			std::vector <int> Expectation = { r3.GetX1(), r3.GetX2(), r3.GetY1(), r3.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodSubtraction)
		{
			Rectangular r1(0,2,0,2);
			Rectangular r2(1, 3, 1, 4);
			std::vector <int> Result = { 1, 2, 1, 2 };
			Rectangular r3(0,1,0,1);
			r3 = r1 - r2;
			std::vector <int> Expectation = { r3.GetX1(), r3.GetX2(), r3.GetY1(), r3.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodAdditionWithAssignment)
		{
			Rectangular r1(0,2,0,2);
			Rectangular r2(1,3,1,4);
			std::vector <int> Result = { 0, 3, 0, 4 };
			r1 += r2;
			std::vector <int> Expectation = { r1.GetX1(), r1.GetX2(), r1.GetY1(), r1.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodSubtractionWithAssignment)
		{
			Rectangular r1(0,2,0,2);
			Rectangular r2(1,3,1,4);
			std::vector <int> Result = { 1, 2, 1, 2 };
			r1 -= r2;
			std::vector <int> Expectation = { r1.GetX1(), r1.GetX2(), r1.GetY1(), r1.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodPreIncrement)
		{
			Rectangular r1(0,1,0,1);
			std::vector <int> Expectation = { r1.GetX1(), r1.GetX2() + 1, r1.GetY1(), r1.GetY2() + 1 };
			++r1;
			std::vector <int> Result = { r1.GetX1(), r1.GetX2(), r1.GetY1(), r1.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
		TEST_METHOD(TestMethodPreDecrement)
		{
			Rectangular r1(0,1,0,1);
			std::vector <int> Expectation = { r1.GetX1(), r1.GetX2() - 1, r1.GetY1(), r1.GetY2() - 1 };
			--r1;
			std::vector <int> Result = { r1.GetX1(), r1.GetX2(), r1.GetY1(), r1.GetY2() };
			for (int i = 0; i < Expectation.size(); i++)
			{
				Assert::AreEqual(Expectation[i], Result[i]);
			}
		}
	};
}