#pragma once
#include <string>
#include "ClubMember.h"
#include "Sport.h"
#include <iostream>
using namespace std;


class TeamMember : public ClubMember 
{
private:
	Sport sportType_;
	string experience_;
public:
	TeamMember();
	TeamMember(Sport, string, int, string, string);
	int PayFee() override;
	
	~TeamMember();
};
