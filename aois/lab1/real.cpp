#include "real.h"

int binaryCodeReal::make_int_code(int part)
{
	int quotient = part;
	while (quotient != 0)
	{
		int t = quotient % 2;
		fixed_point_code.push_back(t);
		quotient = quotient / 2;
	}
	reverse(fixed_point_code.begin(),fixed_point_code.end());
	return fixed_point_code.size()-1;
}

vector <int> binaryCodeReal::make_exponent(int e)
{
	
	vector <int> exponent={ 0, 0, 0, 0, 0, 0, 0, 0 };
	int k = exponent.size() - 1;
	int quotient = e;
	while (quotient != 0)
	{
		int t = quotient % 2;
		exponent[k--] = t;
		quotient = quotient / 2;
	}
	return exponent;
}

void binaryCodeReal::make_code()
{
	vector <int> final(32, 0);
	int int_part = static_cast<int>(a);
	point = make_int_code(int_part);            
	double diff = a - int_part;
	while (diff != 1)
	{
		diff = diff * 2;
		if (diff > 1)
		{
			diff -= 1;
			if (fixed_point_code.size() < 22) fixed_point_code.push_back(1);
			else break;
		}
		else if(diff!=1) if (fixed_point_code.size() < 22)  fixed_point_code.push_back(0);
		else break;
	}
	fixed_point_code.push_back(1);
	int n_point = 0;
	for (int i = 0; i <fixed_point_code.size(); i++)
	{
		if (fixed_point_code[i] == 1)
		{
			n_point = i;
			break;
		}
	}
	int e = point - n_point;
	exponent = 127 + e;
	vector <int> expV = make_exponent(exponent);
	vector <int> result(32);
	result[0] = 0; auto iter = fixed_point_code.begin();
	if (fixed_point_code[0] != 0)
	{
		fixed_point_code.erase(iter);
	}
	else {
		fixed_point_code.erase(iter+1);
		fixed_point_code.erase(iter);
	}
	for (int i = 0; i < expV.size(); i++)
	{
		result[i+1] = expV[i];
	}
	for (int i = 0; i < fixed_point_code.size(); i++)
	{
		result[i + 9] = fixed_point_code[i];
	}
	code = result;
}

vector<int> binaryCodeReal::get_code()
{
	return code;
}

double binaryCodeReal::get_a()
{
	return a;
}

binaryCodeReal::binaryCodeReal(double number)
{
	a = number;
	make_code();
}

binaryCodeReal::binaryCodeReal()
{
	a = 0;
	exponent = 0;
	point = 0;
	fixed_point_code = { 0 };
	code = { 0 };
}

binaryCodeReal binaryCodeReal::operator+(binaryCodeReal other)
{
	binaryCodeReal sum;
	sum.a = this->a + other.a;
	vector <int> sumCode(32);
	int new_exp = 0;
	int exp1 = this->exponent;
	int exp2 = other.exponent;
	vector <int> str1=this->fixed_point_code;
	vector <int> str2 = other.fixed_point_code;
	int sizeDiff = str1.size() - str2.size();
	auto iter1 = str1.cbegin();
	auto iter2 = str2.cbegin();
	auto k1 = str1.cend();
	auto k2 = str2.cend();
	if (sizeDiff > 0)
	{
		str2.insert(k2, sizeDiff, 0);
	}
	if (sizeDiff < 0)
	{
		str1.insert(k1, abs(sizeDiff), 0);
	}
	vector <int> result(23);
	str1.insert(str1.begin(), 1);
	str2.insert(str2.begin(), 1);
	str1.insert(str1.begin(), 0);
	str2.insert(str2.begin(), 0);
	
	int dif = abs(exp1 - exp2);
	if (exp1 > exp2)
	{
		str2.insert(str2.begin(), dif, 0);
		str1.insert(str1.end(), dif, 0);
		new_exp = exp1;
	}
	if (exp2 > exp1)
	{
		str1.insert(str1.begin(), dif, 0);
		str2.insert(str2.end(), dif, 0);
		new_exp = exp2;
	}
	else new_exp = exp1;
	int actS = 0, buffer = 0;
	int sizeNorm=str1.size()-23;
	if (sizeNorm > 0)
	{
		while (sizeNorm!= 0)
		{
			str1.pop_back();
			str2.pop_back();
			sizeNorm--;
		}
	}
	
	for (int i = str1.size() - 1; i >= 0; i--)
	{
		actS = str1[i] + str2[i];
		switch (actS + buffer)
		{
		case 0:
			result[i] = 0;
			buffer = 0;
			break;
		case 1:
			result[i] = 1;
			buffer = 0;
			break;
		case 2:
			result[i] = 0;
			buffer = 1;
			break;
		case 3:
			result[i] = 1;
			buffer = 1;
			break;
		}
	}
	if (result[0] == 1) new_exp++;
	vector <int> sumExponent = this->make_exponent(new_exp);
	for (int i = 0; i < sumExponent.size(); i++)
	{
		sumCode[i + 1] = sumExponent[i];
	}
	if (result[0] == 0) result.erase(result.begin());
	result.erase(result.begin());
	
	for (int i = 0; i <result.size(); i++)
	{
		sumCode[i + 1 + sumExponent.size()] = result[i];
	}
	sum.code = sumCode;
	return sum;
}

binaryCodeReal binaryCodeReal::operator/(binaryCodeReal)
{
	binaryCodeReal division;

	return division;
}

vector<int> binaryCodeReal::get_fixed_point_code()
{
	fixed_point_code.insert(fixed_point_code.begin(), 1);
	return fixed_point_code;
}
