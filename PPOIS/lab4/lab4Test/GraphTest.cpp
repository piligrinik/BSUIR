#include "pch.h"
#include "CppUnitTest.h"
#include "../lab4/Graph.h"
#include "../lab4/Vertex.cpp"
#include "..//lab4/Graph.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;
using namespace std;

namespace Orthogonal_adjacency 
{
	TEST_CLASS(GraphTest)
	{
	public:
		
		TEST_METHOD(OperatorAssignment)
		{
			Graph<int> a;
			a.add_vertex(1);
			a.add_vertex(9);
			a.add_edge(1, 9);
			Graph<int> b;
			b= a;
			Assert::IsTrue(b == a);
		}

		TEST_METHOD(OperatorEquals)
		{
			Graph<int> g;
			g.add_vertex(1);
			g.add_vertex(2);
			g.add_edge(1, 2);
			Graph<int> c;
			c.add_vertex(1);
			c.add_vertex(2);
			c.add_edge(1, 2);
			Assert::IsTrue(g == c);
			
		}
		TEST_METHOD(Exception)
		{
			Graph<int> a;
			a.add_vertex(1);
			a.add_vertex(9);
			auto func = [&] { a.add_edge(1, 2); };
			Assert::ExpectException<std::runtime_error>(func);
		}
	};
}
