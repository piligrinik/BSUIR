#include "Manager.h"

Manager::Manager(): Admin()
{

}

Manager::Manager(string name, string password) : Admin(name, password)
{

}
void Manager::pickHealthyTeams()
{
    for (int i = 0; i < teams_.size(); i++)
    {
        if (teams_[i].getHealthy()) healthyTeams_.push_back(teams_[i]);
    }
}

void Manager::organizeCompetition()
{
    srand(time(0));
    int firstPlace = 0 + rand() % healthyTeams_.size();
    cout << "Team " << healthyTeams_[firstPlace].getName() << " wins! Congrats!" << endl;


}
void Manager::reserveGym()
{
    gym_.setReserved(true);
}

vector<Team>& Manager::getHealthyTeam()
{
    return healthyTeams_;
}

Manager::~Manager()
{
}