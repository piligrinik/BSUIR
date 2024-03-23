#include "pch.h"
#include "CppUnitTest.h"
#include "../AOIS1/int.h"
#include "../AOIS1/real.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace aois1tests
{
	TEST_CLASS(aois1tests)
	{
	public:

		TEST_METHOD(IntStraight)
		{
			binaryCodeInt a(8);
			vector <int> answer = { 0, 0, 0, 0, 1, 0, 0, 0 };
			vector <int> pr_answer = a.get_straight_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}
		}
		TEST_METHOD(IntReverse)
		{
			binaryCodeInt a(-8);
			vector <int> answer = { 1, 1, 1, 1, 0, 1, 1, 1 };
			vector <int> pr_answer = a.get_reverse_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}
		}
		TEST_METHOD(IntAdditional)
		{
			binaryCodeInt a(-8);
			vector <int> answer = { 1, 1, 1, 1, 1, 0, 0, 0 };
			vector <int> pr_answer = a.get_additional_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}
		}
		TEST_METHOD(IntSummary)
		{
			binaryCodeInt a(2);
			binaryCodeInt b(-1);
			binaryCodeInt c;
			c = a + b;
			Assert::AreEqual(c.get_a(), 1);
		}
		TEST_METHOD(IntSummary2)
		{
			binaryCodeInt a(-19);
			binaryCodeInt b(11);
			binaryCodeInt c;
			c = a + b;
			vector <int> answer = { 1, 0, 0, 0, 1, 0, 0, 0 };
			vector <int> pr_answer = c.get_straight_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}	
		}
		TEST_METHOD(IntSubstraction)
		{
			binaryCodeInt a(19);
			binaryCodeInt b(11);
			binaryCodeInt c;
			c = a - b;
			Assert::AreEqual(c.get_a(), 8);
		}
		TEST_METHOD(IntSub2)
		{
			binaryCodeInt a(4);
			binaryCodeInt b(-3);
			binaryCodeInt c;
			c = a - b;
			vector <int> answer = { 0, 0, 0, 0, 0, 1, 1, 1 };
			vector <int> pr_answer = c.get_straight_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}

		}
		TEST_METHOD(IntProduct)
		{
			binaryCodeInt a(-4);
			binaryCodeInt b(3);
			binaryCodeInt c;
			c = a * b;
			Assert::AreEqual(c.get_a(), -12);
		}

		TEST_METHOD(IntPro2)
		{
			binaryCodeInt a(4);
			binaryCodeInt b(-3);
			binaryCodeInt c;
			c = a * b;
			vector <int> answer = { 1, 0, 0, 0, 1, 1, 0, 0 };
			vector <int> pr_answer = c.get_straight_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}

		}
		TEST_METHOD(IntDivision)
		{
			binaryCodeInt a(6);
			binaryCodeInt b(4);
			binaryCodeReal c;
			c = a / b;
			vector <int> answer = { 0, 1, 1, 0, 0, 0, 0 };
			vector <int> pr_answer = c.get_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}

		}
		TEST_METHOD(IntDiv2)
		{
			binaryCodeInt a(6);
			binaryCodeInt b(4);
			binaryCodeReal c;
			c = a / b;
			Assert::AreEqual(c.get_a(), 1.5);
		}


		TEST_METHOD(RealCode) 
		{
			binaryCodeReal a(6.45);
			vector <int> answer = { 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0,1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0};
			vector <int> pr_answer = a.get_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}
		}
		TEST_METHOD(RealSum)
		{
			binaryCodeReal a(6.45);
			binaryCodeReal b(3.05);
			binaryCodeReal c;
			c = a + b;
			vector <int> answer = { 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 };
			vector <int> pr_answer = c.get_code();
			for (int i = 0; i < answer.size(); i++)
			{
				Assert::AreEqual(pr_answer[i], answer[i]);
			}
		}
	};
}
