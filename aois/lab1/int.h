#pragma once
#include <iostream>
#include <vector>
#include "real.h"
using namespace std;



class binaryCodeInt {
	friend class binaryCodeReal;
private:
	int a;
	int sign;
	vector<int> straight_code;
	vector<int> reverse_code;
	vector<int> additional_code;
	void make_straigt_code();
	void make_reverse_code();
	void make_additional_code();
	void make_quotient_code(binaryCodeReal&);
	void convert();
public:
	binaryCodeInt();
	binaryCodeInt(int);
	vector <int> get_straight_code();
	vector <int> get_reverse_code();
	vector <int> get_additional_code();
	binaryCodeInt operator+(binaryCodeInt b);
	binaryCodeInt operator-(binaryCodeInt b);
	binaryCodeInt operator*(binaryCodeInt b);
	binaryCodeReal operator/(binaryCodeInt b);
	int get_a();
};