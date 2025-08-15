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
    int Int = 1; // 2 or 4 bytes. Stores a number without decimals. "%d", "%i".
    long int LongInt = 1000000;
    float Float = 1.0; // 4 bytes. Stores a number with decimals. "%f".
    double Double = 1.0; // 8 bytes. Stores a number with decimals. "%lf" long float.
    char Char = 'A'; // 1 bytes. Stores a character. "%c".
    char string[] = "AAA"; // characters array. "%s".
    bool boolean = false;
    size_t size = sizeof(Int); // size_t a data type returned by "sizeof()", "sizeof()" returns an integer unsigned.
    
    printf("Decimal 2 or 4 bytes: %d\nLong int 4 or 8 bytes %ld\nFloat 4 bytes %f\nFloat 4 bytes (decimal precision) %.1f\nDouble (long float) 8 bytes %lf\nChar 1 bytes %c\nString (char array)%s\nBoolean %b\nsize_t data type returned by sizeof() %zu\n", Int, LongInt, Float, Float, Double, Char, string, boolean, size);
    return 0;
}

int arrays() {
  int* returnArray() {
    static int arrayNum[] = {1, 2, 3, 4, 5}; // Vector
    return arrayNum;
  }
  int printArray(int* array, int size) { // Could it be "void" function
    int i;
    for (i=0;i<size; i++) {
      printf("%d ", array[i]);
    }
    printf("\n");
  }
  /*int* array = returnArray();
  for (int i=0; i<5; i++) {
    printf("%d ", array[i]);
  }
  printf("\n");*/
  int array[] = {1, 2, 3, 4, 5};
  size_t size = sizeof(array) / sizeof(array[0]);
  int* ptrArray = array;
  printArray(ptrArray, size);
  //printArray(array, size);
  printf("Access element in the array: %d \n", array[0]);
  printf("Get element in array using pointer: %d \n", *(ptrArray + 1));
}

//int consts

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
    dataTypes();
    // ifElse();
    // shortHandIfElse();
    //arrays();
    return 0;
}
