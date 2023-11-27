#pragma once
#include <string>
#include <vector>
#include "TeamMember.h"
#include "Sport.h"
#include "Gym.h"
using namespace std;


class Team 
{
private:
	Sport sportType_;
	string teamName_;
	bool readyToCompete_;
	bool isHealthy;
public:
	Team();
	Team(Sport, string);
	string getName() const;
	bool Train(Gym);
	void TrainTooHard();
	bool getHealthy() const;
	bool GetReadyToCompete(); 
	bool operator==(Team);
	~Team();
};

