#include <iostream>
#include "int.h"
#include "real.h"
#include <vector>
using namespace std;

int main()
{
	int number = 0;
	cout << "Enter the first number: " << endl;
	cin >> number;
	binaryCodeInt a(number);
	vector <int > straight=a.get_straight_code();
	cout << "You entered: " <<number<< endl;
	cout << "straight code: " << endl;
	for (int i : straight)
	{
		cout << i << " ";
	}
	cout << endl;
	vector <int> reverse = a.get_reverse_code();
	cout << "reversed code: " << endl;
	for (int i : reverse)
	{
		cout << i << " ";
	}
	cout << endl;
	vector <int> additional = a.get_additional_code();
	cout << "additional code: " << endl;
	for (int i : additional)
	{
		cout << i << " ";
	}


	cout << endl;

	cout << "Enter the second number: " << endl;
	int number2 = 0;
	cin >> number2;
	binaryCodeInt b(number2);
	vector <int > straight2 = b.get_straight_code();
	cout << "You entered: " << number2 << endl;
	cout << "straight code: " << endl;
	for (int i : straight2)
	{
		cout << i << " ";
	}
	cout << endl;
	vector <int> reverse2 = b.get_reverse_code();
	cout << "reversed code: " << endl;
	for (int i : reverse2)
	{
		cout << i << " ";
	}
	cout << endl;
	vector <int> additional2 = b.get_additional_code();
	cout << "additional code: " << endl;
	for (int i : additional2)
	{
		cout << i << " ";
	}
	cout << endl;
	binaryCodeInt c=a.operator+(b);
	vector <int > straight3 = c.get_additional_code();
	cout << "straight code of the summary: " << endl;
	for (int i : straight3)
	{
		cout << i << " ";
	}
	cout << endl << c.get_a();
	cout << endl;
	binaryCodeInt d= a.operator-(b);
	vector <int > straight4 = d.get_additional_code();
	cout << "straight code of the substraction: " << endl;
	for (int i : straight4)
	{
		cout << i << " ";
	}
	cout << endl << d.get_a() << endl;

	binaryCodeInt e = a.operator*(b);
	vector <int > straightE = e.get_additional_code();
	cout << "straight code of the product: " << endl;
	for (int i : straightE)
	{
		cout << i << " ";
	}
	cout << endl << e.get_a()<<endl;
	binaryCodeReal realDivision;
	realDivision = a / b;
	vector <int> strDivision = realDivision.get_code();
	cout << "Division in decimal: " << endl << realDivision.get_a() << endl;
	cout << "code of the division of two reals: " << endl;
	for (int i : strDivision)
	{
		cout << i << " ";
	}
	cout << endl;
	
	double realN = 0;
	cout << "Enter real number: " << endl;
	cin >> realN;
	binaryCodeReal real(realN);
	cout << "You entered: " << realN << endl;
	vector <int> real_code =real.get_code();
	cout << "code: " << endl;
	for (int i : real_code)
	{
		cout << i << " ";
	}
	cout << endl;
	double realN2 = 0;
	cout << "Enter real number: " << endl;
	cin >> realN2;
	binaryCodeReal real2(realN2);
	cout << "You entered: " << realN2 << endl;
	vector <int> real_code2 = real2.get_code();
	cout << "code: " << endl;
	for (int i : real_code2)
	{
		cout << i << " ";
	}
	cout << endl;
	binaryCodeReal realSum;
	realSum = real + real2;
	vector <int> sumCode = realSum.get_code();
	cout << "Summary in decimal: " << endl << realSum.get_a() << endl;
	cout << "code of the summary of two reals: " << endl;
	for (int i : sumCode)
	{
		cout << i << " ";
	}
	cout << endl;
	
}
