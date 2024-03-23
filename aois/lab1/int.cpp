#include"../AOIS1/int.h"



binaryCodeInt::binaryCodeInt(int newA) : a(newA) {
	if (a < 0) sign = 1;
	else sign = 0;
	make_straigt_code();
	make_reverse_code();
	make_additional_code();
}

binaryCodeInt::binaryCodeInt()
{
	a = 0;
	sign = 0;
	straight_code = { 0,0,0,0,0,0,0,0 };
	reverse_code = { 0,0,0,0,0,0,0,0 };
	additional_code = { 0,0,0,0,0,0,0,0 };
}

void binaryCodeInt::make_straigt_code()
{
	straight_code = { 0, 0, 0, 0, 0, 0, 0, 0 };
	int k = straight_code.size()-1;
	auto iter{ straight_code.end() -1};
	int quotient = abs(a);
	while (quotient != 0)
	{
		int t = quotient % 2;
		straight_code[k--] = t;
		quotient=quotient / 2;
	}
	straight_code[0]=sign;
}

vector<int> binaryCodeInt::get_straight_code()
{
	return straight_code;
}

void binaryCodeInt::make_reverse_code()
{
	reverse_code = { 0,0,0,0,0,0,0,0 };
	if (straight_code[0] == 0) reverse_code=straight_code;
	else
	{
		for (int i = 1; i < straight_code.size(); i++)
		{
			if (straight_code[i] == 0) reverse_code[i] = 1;
			else reverse_code[i]=0;
		}
	
		reverse_code[0] = 1;
	}
}

vector<int> binaryCodeInt::get_reverse_code()
{
	return reverse_code;
}

void binaryCodeInt::make_additional_code()
{
	if (straight_code[0] == 0) additional_code=straight_code;
	else
	{
		additional_code = reverse_code;
		for (auto iter{ additional_code.rbegin() }; iter != additional_code.rend(); ++iter)
		{
			if (*iter == 1) *iter = 0;
			else
			{
				*iter = 1;
				break;
			}
		}
		additional_code[0] = 1;
	}
}

void binaryCodeInt::make_quotient_code(binaryCodeReal &q)
{
	vector <int> fixed_point = q.get_fixed_point_code();
	vector <int> new_code(32);
	auto iterator = fixed_point.begin();
	for (int i = 0; i < fixed_point.size(); i++)
	{
		new_code[i] = fixed_point[i];
	}
	int iter = q.point;
	if (iter > 0)
	{
		iterator = new_code.begin() + iter;
	}
	else
	{
		iterator = new_code.begin();
	}
	new_code.erase(iterator+6, new_code.end());
	q.code = new_code;
}

vector<int> binaryCodeInt::get_additional_code()
{
	return additional_code;
}

binaryCodeInt binaryCodeInt::operator-(binaryCodeInt b)
{
	binaryCodeInt b1(-(b.a));
	vector <int> add1 = this->additional_code;
	vector <int> add2 = b1.additional_code;
	binaryCodeInt substraction;
	substraction=this->operator+(b1);
	//vector <int> straight = substraction.straight_code;
	//int actS = 0, buffer = 0;
	//for (int i = add1.size() - 1; i >= 0; i--)
	//{
	//	actS = add1[i] + add2[i];
	//	switch (actS + buffer)
	//	{
	//	case 0:
	//		straight[i] = 0;
	//		buffer = 0;
	//		break;
	//	case 1:
	//		straight[i] = 1;
	//		buffer = 0;
	//		break;
	//	case 2:
	//		straight[i] = 0;
	//		buffer = 1;
	//		break;
	//	case 3:
	//		straight[i] = 1;
	//		buffer = 1;
	//		break;
	//	}
	//}
	//substraction.straight_code = straight;
	////if(summary.straight_code[0]==0)
	//substraction.make_reverse_code();
	//substraction.make_additional_code();
	//substraction.straight_code = substraction.get_additional_code();
	return substraction;
}

void binaryCodeInt::convert()
{
	vector <int> reverse_straight = straight_code;
	reverse(reverse_straight.begin(), reverse_straight.end());
	for (int i = reverse_straight.size() - 2; i >= 0; i--)
	{
		if (reverse_straight[i] != 0) a += pow(2, i);
	}
	if (reverse_straight[reverse_straight.size() - 1] == 1) a *= -1;
}

int binaryCodeInt::get_a()
{
	return a;
}

binaryCodeInt binaryCodeInt::operator*(binaryCodeInt b)
{
	binaryCodeInt product;
	vector <int> buffer(8);
	vector <int> summary(8);
	//binaryCode buffer;
	vector <int> str1 = this->straight_code;
	vector <int> str2 = b.straight_code;
	int actS = 0, buff = 0, sdvig=0;
	for (int i = str1.size()-1; i > 0; i--)
	{
		if (str2[i] == 1)
		{
			buffer = { 0,0,0,0,0,0,0,0 };
			for (int j = str1.size() - 1; j > 0; j--)
			{
				sdvig = j - (str1.size() - 1 - i);
				if (sdvig>0) buffer[sdvig] = str1[j];
			}


			for (int j = summary.size()-1; j >0; j--)
			{
				actS = summary[j] + buffer[j];
				switch (actS+buff)
				{
				case 0:
					summary[j] = 0;
					buff = 0;
					break;
				case 1:
					summary[j] = 1;
					buff = 0;
					break;
				case 2:
					summary[j] = 0;
					buff = 1;
					break;
				case 3:
					summary[j] = 1;
					buff = 1;
					break;
				}
			}
		}
	}
	int sign1 = str1[0];
	int sign2 = str2[0];
	switch (sign1+sign2)
	{
	case 0:
		summary[0] = 0;
		break;
	case 1:
		summary[0] = 1;
		break;
	case 2:
		summary[0] = 0;
		break;
	}
	product.straight_code = summary;
	product.make_reverse_code();
	product.make_additional_code();
	product.convert();
	return product;
}

binaryCodeReal binaryCodeInt::operator/(binaryCodeInt b)
{
	
	vector <int> str1 = this->straight_code;
	vector <int> str2 = b.straight_code;
	int dividend = 0, divisor = 0;
	double q = 0;
	for (int i = 1; i < 8; ++i)
	{
		dividend += str1[i] * pow(2, 7 - i);
		divisor += str2[i] * pow(2, 7 - i);
	}
	if (divisor != 0) {
         q = static_cast<double>(dividend) / divisor;
		
	}
	else {
		cout << "Error: Division by zero" << endl;
	}
	double absQ = abs(q);
	binaryCodeReal quotient(absQ);
	make_quotient_code(quotient);
	if (q < 0) quotient.code.insert(quotient.code.begin(), 1);
	else quotient.code.insert(quotient.code.begin(), 0);                 //знаковая часть 
	return quotient;
}

binaryCodeInt binaryCodeInt::operator+(binaryCodeInt b)
{

	vector <int> add1 = this->additional_code;
	vector <int> add2 = b.additional_code;
	binaryCodeInt summary;
	vector <int> straight= summary.straight_code;
	int actS=0, buffer = 0;
	for (int i = add1.size() - 1 ;i>=0; i--)
	{
		actS = add1[i] + add2[i];
		switch (actS + buffer)
		{
		case 0:
			straight[i] = 0;
			buffer = 0;
			break;
		case 1:
			straight[i] = 1;
			buffer = 0;
			break;
		case 2:
			straight[i] = 0;
			buffer = 1;
			break;
		case 3:
			straight[i] = 1;
			buffer = 1;
			break;
		}
	}
	summary.straight_code = straight;
	//if(summary.straight_code[0]==0)
	summary.make_reverse_code();
	summary.make_additional_code();
	summary.straight_code = summary.get_additional_code();
	summary.convert();
	return summary;
}


