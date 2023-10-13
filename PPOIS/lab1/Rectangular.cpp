
#include "Rectangular.h"
#include <iostream>
using namespace std;


	Rectangular::Rectangular(int x1, int x2, int y1, int y2)
	{
		this->x1 = 0;
		this->x2 = 1;
		this->y1 = 0;
		this->y2 = 1;

		if (x1 >= 0 && x2 >= 0 && y1 >= 0 && y2 >= 0)
		{
			this->x1 = x1;
			this->x2 = x2;
			this->y1 = y1;
			this->y2 = y2;
		}
		else
		{
			throw std::invalid_argument("AddPositiveIntegers arguments must be positive");
			
		}
	};
	void Rectangular::PrintDimentions()
	{
		cout << "======================" << endl;
		cout << "A(" << x1 << "," << y1 << ");" << endl;
		cout << "B(" << x1 << "," << y2 << ");" << endl;
		cout << "C(" << x2 << "," << y2 << ");" << endl;
		cout << "D(" << x2 << "," << y1 << ");" << endl;
	}
	int Rectangular::GetX1()
	{
		return x1;
	}
	int Rectangular::GetX2()
	{
		return x2;
	}
	int Rectangular::GetY1()
	{
		return y1;
	}
	int Rectangular::GetY2()
	{
		return y2;
	}
	void Rectangular::setDimentions(int x1, int x2, int y1, int y2)
	{
		if (x1 >= 0 && x2 >= 0 && y1 >= 0 && y2 >= 0)
		{
			this->x1 = x1;
			this->x2 = x2;
			this->y1 = y1;
			this->y2 = y2;
		}
		else throw std::invalid_argument("AddPositiveIntegers arguments must be positive");

	}
	void Rectangular::changeSize(int x1, int x2, int y1, int y2)
	{
		this->x1 += x1;
		this->x2 += x2;
		this->y1 += y1;
		this->y2 += y2;
	}
	Rectangular Rectangular::operator ++(int)
	{
		x2++;
		y2++;
		return *this;
	}
	Rectangular Rectangular::operator --(int)
	{
		x2--;
		y2--;
		return *this;
	}
	Rectangular& Rectangular::operator ++()
	{
		x2+= 1;
		y2 += 1;
		return *this;
	}
	Rectangular& Rectangular::operator --()
	{
		x2 -= 1;
		y2 -= 1;
		return *this;
	}
	void Rectangular::operator +=(const Rectangular& second)
	{
		int x1Min = 0, x2Max = 0, y1Min = 0, y2Max = 0;
		x1Min = this->x1 < second.x1 ? this->x1 : second.x1;
		y1Min = this->y1 < second.y1 ? this->y1 : second.y1;
		x2Max = this->x2 > second.x2 ? this->x2 : second.x2;
		y2Max = this->y2 > second.y2 ? this->y2 : second.y2;
		this->x2 = x2Max;
		this->x1 = x1Min;
		this->y1 = y1Min;
		this->y2 = y2Max;

	}
	Rectangular Rectangular::operator+(const Rectangular& second)
	{
		Rectangular sum(0, 1, 0, 1);
		int x1Min=0,x2Max=0, y1Min=0, y2Max = 0;
		x1Min = this->x1 < second.x1 ? this->x1 : second.x1;
		y1Min = this->y1 < second.y1 ? this->y1 : second.y1;
		x2Max = this->x2> second.x2 ? this->x2 : second.x2;
		y2Max = this->y2 > second.y2 ? this->y2 : second.y2;
		sum.x1 = x1Min;
		sum.y1 = y1Min;
		sum.x2= x2Max;
		sum.y2 = y2Max;
		return sum;
	}
	Rectangular Rectangular::operator -(const Rectangular& second)
	{
		Rectangular diff(0, 1, 0, 1);
		
		diff.x1 = this->x1 > second.x1 ? this->x1 : second.x1;
		diff.x2 = this->x2 < second.x2 ? this->x2 : second.x2;
		diff.y1 = this->y1 > second.y1 ? this->y1 : second.y1;
		diff.y2 = this->y2 < second.y2 ? this->y2 : second.y2;
		return diff;
	}
	void Rectangular:: operator -=(const Rectangular& second)
	{
		int x1Max = 0;
		int x2Min = 0;
		int y1Max = 0;
		int y2Min = 0;
		x1Max = this->x1 > second.x1 ? this->x1 : second.x1;
		x2Min = this->x2 < second.x2 ? this->x2 : second.x2;
		y1Max = this->y1 > second.y1 ? this->y1 : second.y1;
		y2Min = this->y2 < second.y2 ? this->y2 : second.y2;
		this->x1 = x1Max;
		this->x2 = x2Min;
		this->y1 = y1Max;
		this->y2 = y2Min;
	}
	Rectangular::~Rectangular()
	{
	}
