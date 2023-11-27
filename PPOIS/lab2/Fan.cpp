#include "Fan.h"

Fan::Fan()
{
	age_ = 30;
	name_ = "Jessica";
	sex_ = "Female";
	favSport_ = Volleyball;
	membershipTime_ = "2 years";
	certificate_ = true;
	
}

Fan::Fan(Sport favSport, string membershipTime, int age, string name, string sex) : favSport_(favSport), membershipTime_(membershipTime) 
{
	if (age >= 90) throw invalid_argument("We're afraid, it's too old to be in the Sport Club...");
	else age_ = age;
	string availablesex1 = "Male", availablesex2 = "Female";
	 if (sex == availablesex1 || sex == availablesex2) {
		sex_ = sex;
	}
	else throw invalid_argument("recieved invalid sex");
	name_ = name;
	certificate_ = true;
	
}

int Fan::PayFee()
{
	return 50;
}

