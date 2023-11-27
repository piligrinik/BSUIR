#include "ClubMember.h"
#include <iostream>
using namespace std;




ClubMember::ClubMember()
{
	certificate_ = true;
	age_ = 30;
	name_ = "Thomas";
	sex_ = "Male";
}

ClubMember::ClubMember(bool certificate, int age, string name, string sex)
{
	if (certificate) {
		if (age >= 90) throw invalid_argument("We're afraid, it's too old to be in the Sport Club...");
		else age_ = age;
		string availablesex1 = "Male", availablesex2 = "Female";
		if (sex == availablesex1 || sex == availablesex2) {
			sex_ = sex;
		}
		else throw invalid_argument("recieved invalid sex");
		name_ = name;
		
	}
	else throw invalid_argument("received false bool value");
}


string ClubMember::getName() const
{
	return name_;
}
bool ClubMember::operator==(ClubMember other)
{
	return name_ == other.getName();
}

bool ClubMember::getCertificate() const
{
	return certificate_;
}

void ClubMember::quitTheClub()
{
	this->certificate_ = false; 
}

int ClubMember::PayFee()
{
	return 0;
}

ClubMember::~ClubMember() {

}



