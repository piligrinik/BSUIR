#include "Coach.h"
#include <stdexcept>

Coach::Coach()
{
	age_ = 40;
	name_ = "Roman";
	sex_ = "Male";
	specialization_ = Soccer;
}

Coach::Coach(Sport specialization, int age, string name, string sex) : specialization_(specialization)
{
	age_ = age;
	name_ = name;
	string availablesex1 = "Male", availablesex2 = "Female";
	if (sex == availablesex1 || sex == availablesex2) {
		sex_ = sex;
	}
	else throw invalid_argument("recieved invalid sex");
}

int Coach::PayFee()
{
	return 10;
}
