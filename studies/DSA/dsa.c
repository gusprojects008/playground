#include <stdio.h>
#include <stdlib.h>

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

int main() {
  linkedList();
  return 0;
}
