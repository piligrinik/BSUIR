#pragma once
#include <iterator>
#include <vector>
#include <iostream>
#include "Vertex.h"

using namespace std;
namespace Orthogonal_adjacency {
	template <typename T>
	class Graph {
	public:
		typedef typename vector <Vertex<T>>::iterator vertexes_iterator;
		typedef typename vector <Vertex<T>>::reverse_iterator vertexes_reversed_iterator;
		typedef vector<Vertex<T>> vectorVertexes;

		vertexes_iterator begin_iter();

		vertexes_iterator end_iter() { return vertexes_.end(); }

		vertexes_reversed_iterator rbegin_iter() { return vertexes_.rbegin(); }

		vertexes_reversed_iterator rend_iter() { return vertexes_.rend(); }

		vectorVertexes get_vertexes() { return vertexes_; }

		bool operator==(Graph<T> other);
		Graph<T> operator=(Graph<T> other);
	    void add_vertex(T name);
		void remove_vertex(T name);
		void add_edge(T name1, T name2);
		void remove_edge(T name1, T name2);
		bool vertex_existence(T name);
		bool edge_existence(T name1, T name2);
		int vertex_degree(T name);
		int vertexes_number();
		int edges_nuber();
		
	private:
		vector <Vertex<T>> vertexes_;

	};
}
