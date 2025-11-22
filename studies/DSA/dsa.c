#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// vectors
int arrays() {
  int array[5] = {1, 2, 3, 4, 5}; /* are contiguous blocks of memory. They have a fixed size, and type of data they 
  will store is definded by the first data added to the list, which will have index 0. */
  /* Example if the array stores integers of 4 bytes:
  array[0] memory address example: 0x1000, array[1] 0x1004, array[2] 0x1008 ... */
  // each element in array is a sub-block of fixed size, according to its type.
  /* For access is O(1) constant. For removing or inserting elements is O(n) as will be need to shift all the other
  elements in the list */
  return 0;
}

int linkedList() {
  // in a linked list, each element has a value and pointer to the next or previous one
  typedef struct Node {
    int value;
    struct Node* next;
  } myNode;

  myNode node;
  node.value = 10;
  node.next = NULL;

  myNode* addNode (myNode* node, int newValue) {
    myNode* newNode = malloc(sizeof(*newNode));
    // struct Node* newnode = (struct Node*) (malloc(sizeof(struct Node));

    newNode->value = newValue;
    newNode->next = NULL;
    node->next = newNode;

    return newNode;
  };

  myNode* newNode = addNode(&node, 20);

  printf("%p %d\n", node.next, node.next->value);

  return 0;
}

int minimumOperations(int* nums, size_t numsSize) {
  int minimumOperationsRes = 0;
  for (int i=0;i<numsSize;i++) {
    int result = (nums[i] % 3) != 0;
    if (result == 1) {
      minimumOperationsRes++;
    };
  };
  return minimumOperationsRes;
}

int romanToInt(char* s) {
  int value(char c) {
      switch(c) {
          case 'I': return 1;
          case 'V': return 5;
          case 'X': return 10;
          case 'L': return 50;
          case 'C': return 100;
          case 'D': return 500;
          case 'M': return 1000;
      }
      return 0;
  }
  int result = 0;
  size_t slength = strlen(s);
  /*if ((1 <= slength <= 15) == 0) {
    return 1;
  };*/
  for (size_t i=0;i<slength;i++) {
    int curr = value(s[i]);
    /*if (curr == 0) {
      return 1;
    }*/
    int next = (i + 1 < slength) ? value(s[i + 1]) : 0;
    if (curr < next) {
      result -= curr;
    } else {
      result += curr;
    }
  }
  /*if ((1 <= result <= 3999) == 0) {
    return 1;
  }*/
  return result;
}

char* longestCommonPrefix(char** strs, size_t strsSize) {
  if ((strsSize < 1) || (strsSize > 200)) return "";
  size_t minLen = strlen(strs[0]);
  for (int i=1;i<strsSize;i++) {
    size_t len = strlen(strs[i]);
    if (len < minLen) minLen = len;
  };
  char* prefix = malloc(sizeof(char) * (minLen + 1));
  int index = 0;
  for (int i=0;i<minLen;i++) {
    char c = strs[0][i];
    for (int j=1;j<strsSize;j++) {
      if (strs[j][i] != c) {
        prefix[index] = '\0';
        return prefix;
      }
    }
    prefix[index++] = c;
  }
  prefix[index] = '\0';
  return prefix;
}

int main() {
  char* strs[] = {"fly", "flamengo", "flanelinha"}; 
  size_t strs_len = strlen(strs[0]);
  char* result = longestCommonPrefix(strs, strs_len);
  printf("%s\n", result);
  free(result);
  return 0;
}

/*
0011 + 2
0101
&
1101 == ~ 0010
0101
*/
