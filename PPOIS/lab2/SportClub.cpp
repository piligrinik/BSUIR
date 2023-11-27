#include "SportClub.h"

SportClub::SportClub()
{
    name_ = "YALA";
    location_ = "LA, USA";
    AllClubMembers_ = { TeamMember(), TeamMember(Basketball,"1 year", 27, "Hanna", "Female"), Fan(), Fan(Soccer, "3 years", 26,"Amanda", "Female"), Coach(), Coach(Volleyball, 45, "Maya", "Female")};
    AllTeams_ = { Team(), Team(Basketball, "Avangers"), Team(Volleyball, "Ramonki") };
    addNewAdmin(Manager("Loren", "lolkekcheburek"));
    addNewAdmin(Accountant("Bob", "334bob"));
}

string SportClub::getName()
{
    return name_;
}

string SportClub::getLocation()
{
    return location_;
}

vector<ClubMember>& SportClub::getClubMembers()
{
    return AllClubMembers_;
}

vector<Team> SportClub::getTeams()
{
    return AllTeams_;
}

vector<Admin> SportClub::getAdmins()
{
    return administration_;
}


void SportClub::addNewAdmin(Admin newAdmin)
{
    bool exist = false;
    for (int i = 0; i < administration_.size(); i++)
    {
        if (administration_[i] == newAdmin)
        {
            exist = true;
            break;
        }
    }
    if (!exist)
    {
        newAdmin.setClubMembers(AllClubMembers_);
        newAdmin.setTeams(AllTeams_);
        administration_.push_back(newAdmin);

    }
}

void SportClub::addNewClubMember(ClubMember newClubMember)
{
    bool exist = false;
    for (int i = 0; i < AllClubMembers_.size(); i++)
    {
        if (AllClubMembers_[i] == newClubMember)
        {
            exist = true;
            break;
        }
    }
    if (!exist) AllClubMembers_.push_back(newClubMember);
}

void SportClub::addNewTeam(Team newTeam)
{
    bool exist = false;
    for (int i = 0; i < AllTeams_.size(); i++)
    {
        if (AllTeams_[i] == newTeam) exist = true;
    }
    if (!exist) AllTeams_.push_back(newTeam);
}


void SportClub::removeClubMember(ClubMember removableClubMember)
{
    int index = -1;
    string remName = removableClubMember.getName();
    for (int i = 0; i < AllClubMembers_.size(); i++)
    {
        if (AllClubMembers_[i].getName() == remName)
            index = i;
    }
    if (index == -1) throw runtime_error("there is no such Club Member to kick out");
    else AllClubMembers_.erase(AllClubMembers_.begin() + index);
}

void SportClub::removeTeam(Team removableTeam)
{
    int index = -1;
    string remName = removableTeam.getName();
    for (int i = 0; i < AllTeams_.size(); i++)
    {
        if (AllTeams_[i].getName() == remName)
            index = i;
    }
    if (index == -1) throw runtime_error("there is no such Team to kick out");
    else AllTeams_.erase(AllTeams_.begin() + index);
}


void SportClub::checkForCertificate()
{
    int index = -1;
    for (int i = 0; i <this->AllClubMembers_.size(); i++)
    {
        if (AllClubMembers_[i].getCertificate()==false) index = i;
    }
    if (index == -1) throw runtime_error("there is no such Club Member to kick out because of non existing certificate");
    else AllClubMembers_.erase(AllClubMembers_.begin() + index);
}


SportClub::~SportClub()
{

}
