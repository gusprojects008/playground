#include <iostream>
#include <string>

//using namespace std; // tells the compiler that it is not necessary to specify the prefix "std::" to refer to function, classes or objects from included libraries. And that the compiler should automatically consider the "cout, endl, string" identifiers and belonging to the std namespace. 

int main() {  // main function used to start others functions!
    std::string hello = "Hello world\n"; // "std::" indicates that it is reffering to a function, class or object from included libraries.
    //std::cout << hello; // std::endl breaks the line and flushes the O.I buffer, sending the data in the buffer to the FD and clearing the O.I buffer.

    std::string* ptr = &hello; // pointer related to the "hello" variable, it can also be understood as a virtual memory address related to it. In other words, a memory address used by the memory space and execution of the program itself. Within the program process's own page table. "ptr" stores the virtual memory address of the "hello" variable. "*" is used to indicate that we are referring to the objetct's pointer (its virtual memory address). A pointer stores the virtual memory address of an object and is necessary for the program to be able to manipulate its value.

    std::cout << hello << &hello << "\n" << ptr << "\n" << *ptr << std::endl; // "*ptr" gets the value associated with the memory address that the pointer stores.

    int num1 = 0, num2 = 1;
    std::cout << "Antes do swap() para a troca de endereços:\n" << "num1 = " << num1 << "\n" << "num2 = " << num2 << "\n";
    std::swap(num1, num2); // changes the memory address of the first variable "num1" to the other "num2", thus changing their values.
    std::cout << "Depois:\n" << "num1 = " << num1 << "\n" << "num2 = " << num2 << std::endl;

    // summarize user input:
    int x, y;
    int sum;
    std::cout << "\nType it a number: ";
    std::cin >> x; // "std::cin" is the standard program input, which is the keyboard!
    std::cout << "Type it other number: ";
    std::cin >> y;
    sum = x + y;
    std::cout << sum << std::endl;

    return 0; // signals that the function has been successfully executed to the end.
}
