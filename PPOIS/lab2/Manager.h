#pragma once
#include "Admin.h"

class Manager :public Admin
{
private:
	vector <Team> healthyTeams_;
public:
	Manager();
	Manager(string, string);
	void pickHealthyTeams();
	void organizeCompetition();
	void reserveGym();
	vector <Team>& getHealthyTeam();
	~Manager();
};
