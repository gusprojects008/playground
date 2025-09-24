// Variables and data types
#include <iostream>

int myInt = 1; //  
double myDouble = 1.5; // 8 bytes
float myFloat = 1.5; // 4 bytes
char myChar = 'G'; // stores single characters (in quotes "")
std::string myString = "Gustavo";
bool myBoolean = true;

int myTest1, myTest2 = 16;

int a, b, c;

int test() {
    a = b = c = 50;
    std::cout << myString;
    return 0;
}

int main() {
    int (*functestPtr)() = &test;
    myTest1 = 10;
    std::cout << myTest1 << "\n" << myTest2 << "\n" << &functestPtr << std::endl << std::flush;
    return 0; // status code
}
