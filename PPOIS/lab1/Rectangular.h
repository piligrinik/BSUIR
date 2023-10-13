#pragma once

//namespace RectLibrary
//{
	class Rectangular
	{
	private:
		int x1;
		int x2;
		int y1;
		int y2;

	public:
		Rectangular(int x1, int x2, int y1, int y2);
		void setDimentions(int x1, int x2, int y1, int y2); int GetX1();
		int GetX2();
		int GetY1();
		int GetY2();
		void PrintDimentions();
		void changeSize(int x1, int x2, int y1, int y2);
		Rectangular operator ++(int);
		Rectangular operator --(int);
		Rectangular& operator ++();
		Rectangular& operator --();
		void operator +=(const Rectangular& second);
		Rectangular operator +(const Rectangular& second);
		Rectangular operator -(const Rectangular& second);
		void operator -=(const Rectangular& second);
		~Rectangular();
	};
//}

