#pragma once
#include "ClubMember.h"
#include "Sport.h"

using namespace std;

class Coach : public ClubMember
{
private:
	Sport specialization_;
public:
	Coach();
	Coach(Sport, int, string, string);
	int PayFee();

};
