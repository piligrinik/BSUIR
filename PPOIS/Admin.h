#pragma once
#include <iostream>
#include "Team.h"
#include "ClubMember.h"
#include <vector>
#include <ctime>
#include "Gym.h"

using namespace std;

class Admin
{
protected:
	string name_;
	string password_;
	string id_;
	vector <Team> teams_;
	vector <ClubMember> clubMembers_;
	Gym gym_;
	string makeAnId();
public:
	Admin();
	Admin(string, string);
	void setClubMembers(vector <ClubMember>);
	void setTeams(vector <Team>);
	string getName();
	vector <ClubMember>& getclubMemers();
	bool operator==(Admin);
	~Admin();
};
