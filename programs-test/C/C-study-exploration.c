#include <unistd.h> // ? file header library that contains the main syscalls to Unix-like systems
#include <stdio.h> // I/O library
#include <stdbool.h>

int hello_friend() {
    char textStr[] = "Hello Friend";
    printf("%s\n", textStr); /* function call to a syscall write(), to display "hello friend" on the program standard
output (stdout) which is by default file descriptor "1" which represents the terminal console.
    can be done too:
    write(1, textStr, sizeof(textStr));
    A function from unistd.h that makes a "write" syscall to the terminal console (standard output (fd 1)) of this program! */

   return 0;
}

int pointers_and_memory_addresses() {
    // "*" is used to declare a pointer variable, or access the value associated with the memory address that the pointer stores.
    int myInt = 1;
    int* ptr = &myInt;
    int* ptrtoptr = ptr;
    printf("%p\n", ptr);
    write(1, ptrtoptr, sizeof(*ptrtoptr)); /* prints the value of "ptrtoptr", which stores the memory address of
    "myInt". Thus, the value of myInt is printed. However, write() is a syscall that prints binary data that is not
    readable on the termina. */

    return 0;
}

int dataTypes() {
    int numInt = 1; // 2 or 4 bytes. Stores a number without decimals. "%d", "%i".
    float numFloat = 1.0; // 4 bytes. Stores a number with decimals. "%f".
    double numDouble = 1.0; // 8 bytes. Stores a number with decimals. "%lf" long float.
    char mychar = 'A'; // 1 bytes. Stores a character. "%c".
    char string[] = "AAA"; // characters array. "%s".
    bool boolean = false;

    printf("%d\n%f\n%lf\n%c\n%s\n%b\n\n", numInt, numFloat, numDouble, mychar, string, boolean); // prints the values.
    return 0;
}

int ifElse() {
    int num0 = 100;
    float num1 = 100.1;
    if (num0 == num1) {
       printf("%b\n", false);
    } else if (num0 < num1) {
      printf("%b\n", true);
    } else {
      printf("%b\n", false);
    }
    return 0;
}

int shortHandIfElse() {
    /* ternary operators are used to shorten if and else statements. Check statements, and perform operations based
       on a condition.
    */
    int num = 100;
    (num == 100) ? printf("%s\n", "Is equal") : printf("%s\n", "Not equal");
    // (condition) ternary operator (?) operation ternary operator (:) operation;
    return 0;
}

int switchfunc() {
    return 0;
}

int loopWhile() {
    return 0;
}

int main() {
    // hello_friend();
    // pointers_and_memory_addresses();
    // dataTypes();
    // ifElse();
    shortHandIfElse();
    return 0;
}
