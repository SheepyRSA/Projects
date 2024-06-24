# include <iostream>
# include <cassert>
using namespace std;

int main() {

	int firstNum = 0;
	int secondNum = 0;
	int evenSum = 0;
	int i,b;
	int sqrtCompare[11];
	string exitPoint;
	double oddSqrt = 0.0;

	do
	{
		cout << "We will calculate the total of all numbers between the selected numbers" << endl;
		cout << "This program requires 2 numbers" << endl;
		cout << "if the second number is less than the first it will prompt you again for input" << endl;
		
		// ask user for numbers

		do
		{
			cout << "Insert first number:" << endl;
			cin >> firstNum;
			cout << endl;
			cout << "Insert second number:" << endl;
			cin >> secondNum;
			cout << endl;

		} while (secondNum < firstNum);

		cout << "Thank you for the numbers" << endl;
		cout << endl;
		
		// creating Array with squareroot between 1 and 10

		cout << "The numbers and their squares:" << endl;
		cout << "Squre" << "\t" << "Root" << endl;

		for (b = 1; b <= 10; b++) {
			sqrtCompare[b] = b * b;
			cout << sqrtCompare[b] << "\t" << b << endl;
		}

		cout << endl;
		cout << endl;

		// testing numbers between first and last number entered

		cout << "All odd numbers between numbers selected:" << endl;

		for (i = firstNum+1; i < secondNum; i++) {
			if (i % 2 == 0) {
				evenSum += i;
			}
			else {
				cout << "odd:" << i << endl;
				oddSqrt += sqrt(i);
			}
		}
		cout << endl;
		cout << "Sum of all even numbers:" << evenSum << endl;
		cout << "Sum of the square root of all odd numbers:" << oddSqrt << endl;

		// Asking if program needs to be ended.
		cout << endl;
		cout << "Would you like to exit? enter Y/N" << endl;
		cin >> exitPoint;

		cout << endl;

	} while (exitPoint == "N");

	/*
	string nameCollector;
	string collectionNames[6];
	int counterA;
	int counterB;

	cout << "This program is getting people in a groups names:" << endl;

	for (counterA = 1; counterA <= 5; counterA++) {
		cout << "Insert the name" << endl;
		cin >> nameCollector;
		collectionNames[counterA] = nameCollector;
	};
	
	cout << "Thank you for the names" << endl;
	cout << endl;
		
	for (counterB = 1; counterB <= 5; counterB++) {
			cout << "Group 1: " << collectionNames[counterB] << endl;
	};
	*/

	/*
	int numCollector = 0;
	int sum = 0;
	int counter;

	cout << "This program is calculating 5 numbers:" << endl;

	for (counter = 1; counter <= 5; counter++) {
		cout << "Insert your number" << endl;
		cin >> numCollector;
		sum = sum + numCollector;
	};

	cout << "Your total is: " << sum << endl;
	*/

	/*string nameOfPerson;
	string surnameOfPerson;
	int counter;

	cout << "Insert your name" << endl;
	cin >> nameOfPerson;

	cout << "Insert your surname" << endl;
	cin >> surnameOfPerson;

	cout << "  Name \t\t Surname" << endl;

	for (counter = 1; counter <= 7; counter++) {
		cout << counter << " " << nameOfPerson << "\t\t " << surnameOfPerson << endl;
	};
	*/

	/*string password;
	 int attempTimes;

	cout << "Enter your password" << endl;
	cin >> password;

	do {
		cout << "Password Incorrect!" << endl;
		cout << "Enter your password" << endl;
		cin >> password;
		if (password != "c++") {
			cout << "Sorry password is incorrect" << endl;
		}
	
	} while (password != "c++");

	do {
		cout << "Password Incorrect!" << endl;
		cout << "Enter your password" << endl;
		cin >> password;
		if (password != "c++") {
			cout << "Sorry password is incorrect" << endl;
		} else if (attempTimes > 7) {
			cout << "Too Many attempts" << endl;
		}

	} while (password != "c++");


	while (password != "c++") {
		cout << "Password Incorrect!" << endl;
		cout << "Enter your password" << endl;
		cin >> password;
		if (password != "c++") {
			cout << "Sorry password is incorrect" << endl;
		}
	};

	cout << "Password correct!" << endl;
	*/

	/* SIMPLE WHILE
	const double maxTemp = 102.5;
	double vatTemp;


	cout << "Enter tempreture" << endl;
	cin >> vatTemp;


	while (vatTemp > maxTemp) {
		cout << "Tempreture is too High!" << endl;
		cout << "Decrease the vat temp" << endl;
		cout << "Enter new tempreture after 5 min" << endl;
		cin >> vatTemp;
	};

	cout << "Tempreture nominal" << endl;
	cout << "Check again in 15min" << endl;
	*/

	return 0;
}