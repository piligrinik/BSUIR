#include "pch.h"
#include "CppUnitTest.h"
#include "/Users/User/Documents/PPOIS/Lab2ppois/Lab2ppois/SportClub.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;
using namespace std;

namespace SportClubTest
{
	TEST_CLASS(SportClubConstructor)
	{
	public:

		TEST_METHOD(SportClubNames)
		{
			SportClub sportClub;
			Assert::IsTrue(sportClub.getName() == "YALA");
			Assert::IsTrue(sportClub.getLocation() == "LA, USA");
		}
		TEST_METHOD(SportClubMembers)
		{
			SportClub sportClub;
			vector <ClubMember> members = { TeamMember(), TeamMember(Basketball,"1 year", 27, "Hanna", "Female"),
										   Fan(), Fan(Soccer, "3 years", 26,"Amanda", "Female"),
											Coach(), Coach(Volleyball, 45, "Maya", "Female") };
			vector <ClubMember> clubMembers = sportClub.getClubMembers();
			Assert::AreEqual(members.size(), clubMembers.size());
			for (int i = 0; i < clubMembers.size(); i++)
			{
				Assert::AreEqual(members[i].getName(), clubMembers[i].getName());
			}
		}
		TEST_METHOD(SportClubTeams)
		{
			SportClub sportClub;
			vector <Team> teams = { Team(), Team(Basketball, "Avangers"), Team(Volleyball, "Ramonki") };
			vector <Team> sportClubTeams = sportClub.getTeams();
			Assert::AreEqual(teams.size(), sportClubTeams.size());
			for (int i = 0; i < sportClubTeams.size(); i++)
			{
				Assert::AreEqual(teams[i].getName(), sportClubTeams[i].getName());
			}
		}
		TEST_METHOD(SportClubAdmins)
		{
			SportClub sportClub;
			vector <Admin> admins = { Manager("Loren", "lolkekcheburek") , Accountant("Bob", "334bob") };
			vector <Admin> clubAdmins = sportClub.getAdmins();
			Assert::AreEqual(admins.size(), clubAdmins.size());
			for (int i = 0; i < clubAdmins.size(); i++)
			{
				Assert::AreEqual(admins[i].getName(), clubAdmins[i].getName());
			}
		}
	};
	TEST_CLASS(SportClubFunctions)
	{
		TEST_METHOD(AddingNewAdmin)
		{
			SportClub sportClub;
			Accountant newAccountant("Luke", "ttt45r");
			sportClub.addNewAdmin(newAccountant);
			vector <Admin> clubAdmins = sportClub.getAdmins();
			bool exists = false;
			for (int i = 0; i < clubAdmins.size(); i++)
			{
				if (clubAdmins[i] == newAccountant) exists = true;

			}
			Assert::IsTrue(exists);
		}
		TEST_METHOD(AddingNewClubMember)
		{
			SportClub sportClub;
			Fan newFan(Volleyball, "1 year", 17, "Kate", "Female");
			sportClub.addNewClubMember(newFan);
			vector <ClubMember> clubMembers = sportClub.getClubMembers();
			bool exists = false;
			for (int i = 0; i < clubMembers.size(); i++)
			{
				if (clubMembers[i] == newFan) exists = true;
			}
			Assert::IsTrue(exists);
		}
		TEST_METHOD(AddingNewTeam)
		{
			SportClub sportClub;
			Team newTeam(Basketball, "Chicago Bulls");
			sportClub.addNewTeam(newTeam);
			vector <Team> sportClubTeams = sportClub.getTeams();
			bool exists = false;
			for (int i = 0; i < sportClubTeams.size(); i++)
			{
				if (sportClubTeams[i] == newTeam) exists = true;
			}
			Assert::IsTrue(exists);
		}
		TEST_METHOD(removingClubMember)
		{
			SportClub sportClub;
			vector <ClubMember> clubMembers = sportClub.getClubMembers();
			Fan removableFan(Soccer, "3 years", 26, "Amanda", "Female");
			bool exists = false;
			for (int i = 0; i < clubMembers.size(); i++)
			{
				if (clubMembers[i] == removableFan) exists = true;
			}
			Assert::IsTrue(exists);

			sportClub.removeClubMember(removableFan);
			vector <ClubMember> NEWclubMembers = sportClub.getClubMembers();
			for (int i = 0; i < NEWclubMembers.size(); i++)
			{
				Assert::IsFalse(NEWclubMembers[i].getName() == "Amanda");
			}
		}
		TEST_METHOD(removingTeam)
		{
			SportClub sportClub;
			vector <Team> teams = sportClub.getTeams();
			Team removableTeam(Basketball, "Avangers");
			bool exists = false;
			for (int i = 0; i < teams.size(); i++)
			{
				if (teams[i] == removableTeam) exists = true;
			}
			Assert::IsTrue(exists);

			sportClub.removeTeam(removableTeam);
			vector <Team> NEWteams = sportClub.getTeams();
			for (int i = 0; i < NEWteams.size(); i++)
			{
				Assert::IsFalse(NEWteams[i].getName() == "Avangers");
			}
		}
		TEST_METHOD(checkingCertificate)
		{
			SportClub sportClub;
			vector <ClubMember>& members = sportClub.getClubMembers();
			members[3].quitTheClub();
			sportClub.checkForCertificate();
		    Assert::IsFalse(members[3].getName() == "Amanda");
		}
	};
}
