#pragma once
#include <string>
using namespace std;

class ClubMember 
{
protected:
	bool certificate_;
	int age_;
	string sex_;
	string name_;
	
	
public:
	ClubMember();
	ClubMember(bool, int, string, string);
	
	string getName() const;
	bool operator==(ClubMember);
	bool getCertificate() const;
	void quitTheClub();
	virtual int PayFee();
	~ClubMember();
};



