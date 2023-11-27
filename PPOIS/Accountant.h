#pragma once
#include "Admin.h"

class Accountant : public Admin
{
private :
	int fees_;
public:
	Accountant();
	Accountant(string, string);
	int collectFee();
	~Accountant();
};