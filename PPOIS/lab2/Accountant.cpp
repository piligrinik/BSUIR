#include "Accountant.h"


Accountant::Accountant(): Admin()
{
    fees_ = 0;
}

Accountant::Accountant(string name, string password) : Admin(name, password)
{
    fees_ = 0;
}

int Accountant::collectFee()
{
    for (int i = 0; i < clubMembers_.size(); i++)
    {
        fees_+= clubMembers_[i].PayFee();
    }
    return fees_;
}
Accountant::~Accountant()
{

}
