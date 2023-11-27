#include "TeamMember.h"

TeamMember::TeamMember()
{
	age_ = 25;
	name_ = "Joshua";
	sex_ = "Male";
	sportType_ = Soccer;
	experience_ = "2 years";
	certificate_ = true;
	
}


TeamMember::TeamMember(Sport sportType, string experience, int age, string name, string sex) : sportType_(sportType), experience_(experience) 
{
	if (age >= 90) throw invalid_argument("We're afraid, it's too old to be in the Sport Club...");
	else age_ = age;
	string availablesex1 = "Male", availablesex2 = "Female";
	if (sex == availablesex1 || sex == availablesex2) {
		sex_ = sex;
	}
	else throw invalid_argument("recieved invalid sex");
	name_ = name;
	certificate_= true;

}


int TeamMember::PayFee()
{
	return 25;
}


TeamMember::~TeamMember()
{

}
