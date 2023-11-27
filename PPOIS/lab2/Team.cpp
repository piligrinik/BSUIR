#include "Team.h"
#include <iostream>

Team::Team() {
	teamName_ = "Cmoki";
	sportType_ = Soccer;
	readyToCompete_ = false;
	isHealthy = true;
}


Team::Team(Sport sportType, string teamName) : sportType_(sportType), teamName_(teamName) 
{
	readyToCompete_ = false;
	isHealthy = true;
}

string Team::getName() const
{
	return teamName_;
}

bool Team::Train(Gym gym)
{
	if (gym.getReserved())
	{
		std::cout << "*Working out*... Now we're ready for a competition!" << endl;
		readyToCompete_ = true;
	}
	return readyToCompete_;
}



bool Team::GetReadyToCompete()
{
	return readyToCompete_;
}

void Team::TrainTooHard()
{
	std::cout << "*Aggressively working out*... Oops! One of the team members broke their leg!" << endl;
	isHealthy = false;
}


bool Team::operator==(Team other)
{
	return teamName_==other.getName();
}


bool Team::getHealthy() const
{
	return isHealthy;
}

Team::~Team()
{

}


