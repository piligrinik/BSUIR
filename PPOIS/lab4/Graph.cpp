#include "Graph.h"
#include <iterator>
#include <vector>
#include <iostream>
#include "Vertex.h"
using namespace std;

namespace Orthogonal_adjacency {

	template<typename T>
     bool Orthogonal_adjacency::Graph<T>::operator==(Graph<T> other)
	{
			vectorVertexes other_vertexes = other.get_vertexes();
			if (other_vertexes.size() != vertexes_.size()) return false;
			for (int i = 0; i < vertexes_.size(); i++)
			{


				if (vertexes_[i] != other.vertexes_[i]) return false;

			}
			return true;
		
	}
	 template<typename T>
	 Graph<T> Graph<T>::operator=(Graph<T> other)
	 {
			 vectorVertexes other_vertexes = other.get_vertexes();
			 this->vertexes_ = other_vertexes;
			 return *this;
	 }

	 template<typename T>
	 void Graph<T>::add_vertex(T name)
	 {
		 for (int i = 0; i < vertexes_.size(); i++)
		 {
			 if (vertexes_[i].name_ == name)
			 {
				 throw runtime_error("This element already exists");
				 break;
			 }

		 }
		 Vertex<T> new_vertex(name);
		 vertexes_.push_back(new_vertex);
	 }

	 template<typename T>
	 void Graph<T>::remove_vertex(T name)
	 {
		 int index = 0;
		 for (int i = 0; i < vertexes_.size(); i++)
		 {
			 if (vertexes_[i].name_ == name) index = i;
		 }
		 if (index != -1)
		 {
			 vertexes_.erase(index + vertexes_.begin());
			 for (int i = 0; i < vertexes_.size(); i++)
			 {
				 vertexes_[i].remove_from_list(name);
			 }
		 }

		 else
		 {
			 throw runtime_error("There's no element to remove");
		 }
	 }

	 template<typename T>
	 void Graph<T>::add_edge(T name1, T name2)
	 {
		 int index1 = -1, index2 = -1;
		 for (int i = 0; i < vertexes_.size(); i++)
		 {
			 if (vertexes_[i].name_ == name1) index1 = i;
			 if (vertexes_[i].name_ == name2) index2 = i;

		 }
		 if (index1 != -1 && index2 != -1) vertexes_[index1].add_to_list(name2);
		 else throw runtime_error("There're no vertexes to add edge to");
	 }

	 template<typename T>
	 void Graph<T>::remove_edge(T name1, T name2)
	 {
		 int index1 = -1, index2 = -1;
		 for (int i = 0; i < vertexes_.size(); i++)
		 {
			 if (vertexes_[i].name_ == name1) index1 = i;
			 if (vertexes_[i].name_ == name2) index2 = i;
			 if (index1 != -1 && index2 != -1) vertexes_[index1].remove_from_list(name2);
			 else throw runtime_error("There-s no edge to remove");
		 }
	 }

	 template<typename T>
	 bool Graph<T>::vertex_existence(T name)
	 {
		 for (int i = 0; i < vertexes_.size(); i++)
		 {
			 if (vertexes_[i].name_ == name) return true;
			 else return false;
		 }
	 }

	 template<typename T>
	 bool Graph<T>::edge_existence(T name1, T name2)
	 {
		 int index1 = -1, index2 = -1;
		 for (int i = 0; i < vertexes_.size(); i++)
		 {
			 if (vertexes_[i].name_ == name1) index1 = i;
			 if (vertexes_[i].name_ == name2) index2 = i;
		 }
		 if (index1 != -1 && index2 != -1)
		 {


			 for (int i = 0; i < vertexes_[index1].adjacency_list.size(); i++)
			 {
				 if (vertexes_[index1].adjacency_list[i] == name2) return true;
				 else return false;

			 }
		 }
		 else return false;
	 }

	 template<typename T>
	 int Graph<T>::vertex_degree(T name)
	 {
		 int index = -1;
		 for (int i = 0; i < vertexes_.size(); i++)
		 {
			 if (vertexes_[i].name_ == name) index = i;
		 }
		 if (index != -1)
		 {
			 return vertexes_[index].adjacency_list.size();
		 }
	 }

	 template<typename T>
	 int Graph<T>::vertexes_number()
	 {
		 return vertexes_.size();
	 }

	 template<typename T>
	 int Graph<T>::edges_nuber()
	 {
		 int num = 0;
		 for (int i = 0; i < vertexes_.size(); i++)
		 {
			 num += vertexes_[i].adjacency_list.size();
		 }
		 return num;
	 }

}