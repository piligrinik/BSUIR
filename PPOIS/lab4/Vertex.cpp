#include "Vertex.h"
#include <iostream>
#include <vector>

using namespace std;

namespace Orthogonal_adjacency 
{

	template <typename T>

	void Vertex<T>::add_to_list(T new_vertex)
	{
			for (int i = 0; i < adjacency_list.size(); i++)
			{
				if (adjacency_list[i] != new_vertex)
					adjacency_list.push_back(new_vertex);
				else throw runtime_error("This element already exists");
			}

			adjacency_list.push_back(new_vertex);
	}

	template<typename T>
	void Vertex<T>::remove_from_list(T r_vertex)
	{
		for (auto i = adjacency_list.begin(); i != adjacency_list.end(); i++)
			if ((*i) == r_vertex)
			{
				adjacency_list.erase(i);
				break;
			}

	}

	template<typename T>
	vector<T> Vertex<T>::get_adjacency_list()
	{
		return adjacency_list;
	}

	template<typename T>
	bool Vertex<T>::operator!=(Vertex<T> other)
	{
		vector<T> other_adjacency_list = other.get_adjacency_list();
		if (adjacency_list.size() != other_adjacency_list.size()) return true;
		for (int i = 0; i < adjacency_list.size(); i++)
		{
			
			
				if (adjacency_list[i] == other_adjacency_list[i]) return false;

		}
		if (adjacency_list.size() == 0 && other_adjacency_list.size() == 0) return false;
		return true;
	}


}