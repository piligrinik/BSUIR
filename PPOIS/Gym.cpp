#include "Gym.h"

Gym::Gym()
{
	name_ = "superJim";
	reserved_ = false;
}

bool Gym::getReserved()
{
	return reserved_;
}

void Gym::setReserved(bool reserved)
{
	reserved_ = reserved;
}
Gym::~Gym()
{

}