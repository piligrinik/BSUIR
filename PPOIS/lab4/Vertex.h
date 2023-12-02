#pragma once
#include <iostream>
#include <vector>

using namespace std;



namespace Orthogonal_adjacency {

	template <typename T>

	class Vertex
	{
	private:
		template <typename T>
		friend class Graph;
		T name_;
		vector<T> adjacency_list;
		Vertex(T name) : name_(name) {}
		void add_to_list(T new_vertex);
		void remove_from_list(T r_vertex);
		vector <T> get_adjacency_list();
		bool operator!=(Vertex < T> other);



	};
}