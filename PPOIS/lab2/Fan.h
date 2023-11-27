#pragma once
#include "ClubMember.h"
#include "Sport.h"
#include <string>
#include <iostream>

using namespace std;

class Fan : public ClubMember 
{
private:
	Sport favSport_;
	string membershipTime_;
public:
	Fan();
	Fan(Sport, string, int, string, string);
	int PayFee() override;

};

