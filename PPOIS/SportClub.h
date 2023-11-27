#pragma once
#include <string>
#include <vector>
#include <ctime>
#include <iostream>
#include "ClubMember.h"
#include "Sport.h"
#include "Team.h"
#include "TeamMember.h"
#include "Fan.h"
#include "Coach.h"
#include "Admin.h"
#include "Gym.h"
#include "Accountant.h"
#include "Manager.h"
using namespace std;

class SportClub {
private:
	string name_;
	string location_;
	vector <ClubMember> AllClubMembers_;
	vector <Team> AllTeams_;
	vector <Admin> administration_;
	
public:
	SportClub();
	string getName();
	string getLocation();
	vector <ClubMember>& getClubMembers();
	vector <Team> getTeams();
	vector <Admin> getAdmins();
	void addNewAdmin(Admin);
	void addNewClubMember(ClubMember);
	void addNewTeam(Team);
	void removeClubMember(ClubMember);
	void removeTeam(Team);
	void checkForCertificate();
	~SportClub(); 

};
