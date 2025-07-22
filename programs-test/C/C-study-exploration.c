#include <unistd.h> // ? file header library that contains the main syscalls to Unix-like systems
#include <stdio.h> // I/O library

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

int main() {
    // hello_friend();
    pointers_and_memory_addresses();
    return 0;
}
