#include <unistd.h> // file header library that contains the main syscalls to Unix-like systems
#include <stdio.h> // I/O library
#include <stdlib.h> // to malloc(), calloc(), realloc() and free()
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

int VariablesDataTypes() {
    int Int = 1; // 2 or 4 bytes. Stores a number without decimals. "%d", "%i".
    long int LongInt = 1000000;
    float Float = 1.0; // 4 bytes. Stores a number with decimals. "%f".
    double Double = 1.0; // 8 bytes. Stores a number with decimals. "%lf" long float.
    char Char = 'A'; // 1 bytes. Stores a character. "%c".
    char string[] = "AAA"; // characters array. "%s".
    bool boolean = false;
    size_t size = sizeof(Int); // size_t a data type returned by "sizeof()", "sizeof()" returns an integer unsigned.
    const int constInt = 10; // constant integer, the value cannot be changed
    static int staticInt = 10; // the keyword "static" allows the variable to keep its value even after the function ends
    printf("Decimal 2 or 4 bytes: %d\nLong int 4 or 8 bytes %ld\nFloat 4 bytes %f\nFloat 4 bytes (decimal precision) %.1f\nDouble (long float) 8 bytes %lf\nChar 1 bytes %c\nString (char array)%s\nBoolean %b\nsize_t data type returned by sizeof() %zu\n", Int, LongInt, Float, Float, Double, Char, string, boolean, size);
    return 0;
}

int switchs() {
  printf("Switchs:\n");
  int day = 1;
  switch (day) {
    case 1:
      printf("Today is day: %d\n", day);
      break;
    default:
     printf("Default code block (;");
  }
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

int loops() {
  printf("Loops:\n");
  int a = 10, b = 5;
  int c = 0;
  printf("While loop:\n");
  while (a > b) {
    if (c == a) {
      break;
    } else {continue;}; // Unnecessary
    printf("%d\n", c);
    c++;
  }
  return 0;
}

int arrays() {
  int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  size_t arraySize = sizeof(array) / sizeof(array[0]);
  printf("Simple loop in array: ");
  for (int i = 0; i < arraySize; i++) {
    printf("%d ", array[i]);
  };
  printf("\n");

  // Multidimensional arrays
  // 2D Array
  int array2D[2][3] = { {1, 2, 3}, {4, 5, 6} }; // Two arrays, each with 3 elements
  printf("Multidimensional arrays\n2D Array\n"); /* This 2D array can be represented as a table,
  with 2 rows and 3 columns */
  printf("First line:   ");
  int i, j;
  for (i = 0; i < 3; i++) {
    printf("%d ", array2D[0][i]);
  }
  printf("\nSecond line:  ");
  for (j = 0; j < 3;  j++) {
    printf("%d ", array2D[1][j]);
  }

  printf("\nSimple nested loop in array:\n");
  for (i = 1; i <= 3; i++) {
    for (j = 1; j <= 3; j++) {
      printf("%d ", i * j);
    };
    printf("\n");
  }
  return 0;
}

// User input
int userInput() {
  char arrayName[8];
  printf("Type it a name: ");
  // scanf("%s", arrayName); // buffer overflow risk
  scanf("%7s", arrayName); // limited to 7 characters
  printf("Hello %s", arrayName);
  printf("\n");

  while (getchar() != '\n'); // clean the buffer

  // Read a text with white spaces from input user:
  char arrayNamefgets[8];
  printf("Using fgets! Type it a name: ");
  fgets(arrayNamefgets, sizeof(arrayNamefgets), stdin);
  printf("Hello %s\n", arrayNamefgets);
  return 0;
}

int memory_management() {
  /* Memory management: allocation, deallocation and release (freeing) in Heap.
  Heap is the memory space used by the program to allocate memory at runtime, data allocated in the heap can only be accessed/managed by pointers */

  int array[10]; // alocation in stack, is automatically free after the function ends

  // Alocating memory
  size_t arraySize = 10;
  int* ptr1 = malloc(arraySize); /* malloc() returns the memory address for the memory block allocated on
  the heap, which is 10 bytes in size */
  int* ptr2 = calloc(1, arraySize); /* idem. But calloc() write zeros to the allocated memory block.
  The first argument is the number of items to be allocated */

  // The best way:
  int* ptr3;
  int* ptr4;
  ptr3 = malloc(sizeof(*ptr3)); // get the size in byte of the data type associated with the pointer
  ptr4 = calloc(1, sizeof(*ptr4));

  int* numbers;
  size_t numbersAmount = 10;
  numbers = calloc(numbersAmount, sizeof(*numbers));
  printf("%ld\n", numbersAmount * sizeof(*numbers));

  // Access memory
  int* ptrBytes;
  size_t allocateSize = 4;
  ptrBytes = malloc(allocateSize * sizeof(*ptrBytes)); // pointer to 4 bytes

  if (ptrBytes == NULL) {
     printf("Realocation failure!\n");
     return 1;
     exit(1);
  };

  printf("Reallocating memory! current pointer: %p size: %zu\n", ptrBytes, allocateSize * sizeof(*ptrBytes));

  char* ptrBytesChar = (char*)ptrBytes; // pointer to 4 chars bytes
  // ptrBytes[0] = 71117115; // access the first set of 4 bytes and writes an integer value (4 bytes) into the 4 bytes allocated by malloc(). The same as:
  *ptrBytes = 71 + (117 << 8) + (115 << 16); // Because "[0]" causes the pointer to automatically dereference itself
  printf("%d is %c %c %c\n", *ptrBytes, ptrBytesChar[0], ptrBytesChar[1], ptrBytesChar[2]);
  
  // Reallocate memory
  allocateSize += 1;
  int* newPtrBytes = realloc(ptrBytes, allocateSize * sizeof(*newPtrBytes)); /* "realloc" resize the memory
  associated with a pointer to a specific size. realloc() can return another pointer, so use the pointer it returns. */
  printf("Reallocated memory! current pointer: %p size: %zu\n", newPtrBytes, allocateSize * sizeof(*ptrBytes));

  if (newPtrBytes == NULL) {
     printf("Realocation failure!\n");
     free(ptrBytes);
     return 1;
     exit(1);
  }

  *newPtrBytes = 1684234849;
  char* newPtrBytesChar = (char*)newPtrBytes;
  printf("%d is %c %c %c %c\n", *newPtrBytes, newPtrBytesChar[0], newPtrBytesChar[1], newPtrBytesChar[2], newPtrBytesChar[3]);

  // Free memory (Deallocate)
  printf("Deallocating memory! with free()\n");
  free(newPtrBytes); 
  newPtrBytes = NULL;
  return 0;
}

// structs
int structs() {
  // in a struct, each member has its own memory
  struct myStruct { // Structure declaration
    // Members
    int myNum; 
    char myLetter;
  };

  void updateLetter(struct myStruct *structPtr) {
     structPtr->myLetter = 'C';
  };

  // Creates the struct and stores it in the variable struct1
  struct myStruct struct1;

  // Assing values to members of struct1
  struct1.myNum = 10;
  struct1.myLetter = 'A';

  printf("struct1: myNum: %d\nstruct1: myLetter: %c\n", struct1.myNum, struct1.myLetter);

  // assign a new values to members in struct. In order!
  struct myStruct struct2 = {20, 'B'};

  // declare a pointer to it
  struct myStruct *ptr = &struct2;

  // The "->" operator automatically dereferences the pointer to the struct. You clould also use (*ptrStruct).member

  printf("Accessing the new members values correctly! with the '->' operator. Struct pointer: %p values: myNum: %d myLetter: %c\n", ptr, ptr->myNum, (*ptr).myLetter);

  printf("Update myLetter with a void function!\n");

  updateLetter(ptr);

  printf("myLetter updated: %c\n", ptr->myLetter);

  return 0;
}

int unions() {
  // in a union, all members share the same memory
  // "typedef" is a keyword that allow you to create aliases for existing data types
  // typedef is similar to "#define" but "#define" is global

  typedef union {
    int myInt;
    bool myBool;
  } myUnion;

  myUnion union1; // Create a union
  
  // only the last value is defined in the union is defined in memory!

  union1.myInt = 1000;

  union1.myBool = true; // now the value of myNum is no longer valid!

  printf("Created union and updated myBool: %b\nmyInt (Unavailable): %d\nUnion size: %zu\n", union1.myBool, union1.myInt, sizeof(union1));

  return 0;
}

int enums() {
  enum alphabet {
    a,
    b,
    c
  };
  enum alphabet firstLetter = a;
  enum alphabet nextLetter = b;
  printf("Print 'a' letter from enum: %d\n next letter %d\n", firstLetter, nextLetter);
  enum newAlphabet {
    new_a = 5,
    new_b,
    new_c
  };
  enum newAlphabet newfirstLetter = new_a;
  enum newAlphabet newnextLetter = new_b;
  printf("Updated first letter. Print 'a' letter from enum: %d\n next letter %d\n", newfirstLetter, newnextLetter);
  return 0;
}

// file handling and sockets
int fileHandling() {
  FILE *ptrFile;
  ptrFile = fopen("./fileHandling.txt", "w"); // fopen() returns a pointer if the file exists, otherwise, NULL. User "w+"
  if (ptrFile == NULL) {
    printf("The file not exist );\n");
    return 1;
  } else {
    fprintf(ptrFile, "Olá amigo!\nEstudar é bom!\n");
    printf("See the file created!\n");
    fclose(ptrFile);
    ptrFile = NULL;

    ptrFile = fopen("./fileHandling.txt", "r"); // fopen() returns a pointer if the file exists, otherwise, NULL
    if (ptrFile != NULL) {
      printf("Reading file!\n");
      char textFile[100];
      while (fgets(textFile, 100, ptrFile)) { // fgets() reads only one line from the file. fgets() returns NULL on file token.
        printf("%s", textFile);
      };
      fclose(ptrFile);
      ptrFile = NULL;
    } else {
      printf("Could not open file in read-only mode!\n");
      return 1;
    };
  }
  return 0;
}

// sockets

int main() {
    // hello_friend();
    // pointers_and_memory_addresses();
    // dataTypes();
    // ifElse();
    // shortHandIfElse();
    // switchs();
    // loops();
    // arrays();
    // userInput();
    // memory_management();
    // structs();
    // unions();
    // enums();
    // fileHandling();
    return 0;
}
