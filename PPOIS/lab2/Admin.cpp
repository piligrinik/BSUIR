#include "Admin.h"
#include <vector>

using namespace std;

string Admin::makeAnId()
{
    string id{};
    for (int i = 0; i < 11; i++)
       id += (rand() % 10 + '0');
    return id;
}

Admin::Admin()
{
    name_ = "Cole";
    password_ = "Coleisthebest";
    id_ = makeAnId();
}

Admin::Admin(string name, string password)
{
    name_ = name;
    password_ = password;
    id_ = makeAnId();
}

void Admin::setClubMembers(vector <ClubMember> clubMembers)
{
    clubMembers_ = clubMembers;
}

void Admin::setTeams(vector <Team> teams)
{
    teams_ = teams;
}

string Admin::getName()
{
    return name_;
}
vector<ClubMember>& Admin::getclubMemers()
{
    return clubMembers_;
}
bool Admin::operator==(Admin other)
{
    return name_ == other.getName();
}

Admin::~Admin()
{

}
