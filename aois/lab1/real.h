#pragma once
#include <iostream>
#include <vector>
using namespace std;

class binaryCodeReal {
	friend class binaryCodeInt;
private:
	double a; 
	int point;
	int exponent;
	
	vector <int> fixed_point_code;
	vector <int> code;
	int make_int_code(int);
	vector <int> make_exponent(int);
	void make_code();
public:
	binaryCodeReal(double);
	binaryCodeReal();
	vector <int> get_code();
	double get_a();
	binaryCodeReal operator+(binaryCodeReal);
	binaryCodeReal operator/(binaryCodeReal);
	vector <int> get_fixed_point_code();
};