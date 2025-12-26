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

int isPalindrome(int x) {
  if (x < 0) return 0;
  if (x < 10) return 1;

  int result = 0;
  int defaultNum = x;
  x = abs(x);

  while (x != 0) {
    result = result * 10 + (x % 10);
    x /= 10; 
  }

  return (result == defaultNum) ? 1 : 0;
}

int* twoSum(int* nums, size_t numsSize, int target, size_t* returnSize) {
  int* result = (int*)malloc(2 * sizeof(int)); // allocates an array for 2 integers
  *returnSize = 2; // indicates the size (number of value) that an array should return
  for (int i = 0; i < numsSize; i++) {
    for (int j = i + 1; j < numsSize; j++) {
      if (nums[i] + nums[j] == target) {
        result[0] = nums[i];
        result[1] = nums[j];
        return result;
      }
    }
  }
  *result = 0;
  free(result);
  return NULL;
};

struct ListNode {
  int val;
  struct ListNode* next;
};
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
  struct ListNode *p = list1, *q = list2;
  struct ListNode dummy;
  struct ListNode *tail = &dummy;
  while (p != NULL && q != NULL) {
    if (p->val <= q->val) {
       tail->next = p;
       p = p->next;
    } else {
      tail->next = q;
      q = q->next;
    }
    tail = tail->next;
  }
  if (p != NULL) tail->next = p;
  if (q != NULL) tail->next = q;
  return dummy.next;
}

bool isValid(char* s) {
  char stack[10000];
  int idx = -1;
  size_t len = strlen(s);
  for (int i = 0; i < len; i++) {
    if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
      stack[++idx] = s[i];
    } else {
      if (idx == -1) return false;
      if (s[i] == ')' && stack[idx] != '(') return false;
      if (s[i] == '}' && stack[idx] != '{') return false;
      if (s[i] == ']' && stack[idx] != '[') return false;
      idx--;
    } 
  }
  return idx == -1;
}

char* gcdOfStrings(char* str1, char* str2) {
  if (strlen(str2) > strlen(str1)) {
    char* tmp = str2;
    str2 = str1;
    str1 = tmp;
  }
  size_t len1 = strlen(str1);
  size_t len2 = strlen(str2);
  size_t total = len1 + len2;
  char* concat1 = malloc(total + 1);
  char* concat2 = malloc(total + 1);
  strcpy(concat1, str1);	
  strcat(concat1, str2);	
  strcpy(concat2, str2);
  strcat(concat2, str1);
  if (strcmp(concat1, concat2) != 0) {
    free(concat1);	
    free(concat2);
    return "";
  };
  free(concat1);	
  free(concat2);
  if (len1 == len2) return str1;
  return gcdOfStrings(str1 + len2, str2);
}

char* mergeAlternately(char* word1, char* word2) {
  size_t w1len = strlen(word1);
  size_t w2len = strlen(word2);
  size_t total = w1len + w2len;
  char* result = /*(char*)*/malloc(total + 1);
  int p1 = 0, p2 = 0;
  while (p2 < w1len || p2 < w2len) {
    if (p2 < w1len) {
      result[p1] = word1[p2];
      p1++;
    };
    if (p2 < w2len) {
      result[p1] = word2[p2];
      p1++;
    };
    p2++;
  }
  result[p1] = '\0';
  return result;
}

bool* kidsWithCandies(int* candies, size_t candiesSize, int extraCandies, int* returnSize) {
  *returnSize = candiesSize;
  bool* result = /*(bool*)*/malloc(sizeof(bool) * candiesSize);
  int max = candies[0];
  for (int i = 0; i < candiesSize; i++) {
    int candy = candies[i];
    if (candy > max) {
      max = candy;
    }
  }
  for (int i = 0; i < candiesSize; i++) {
    result[i] = (candies[i] + extraCandies >= max);
  }
  return result;
}

int fibonacci_number(int n) {
  if (n == 0) return 0;
  if (n == 1) return 1;
  int pre1 = 1, pre2 = 1, res = 1;
  for (int i = 0; i < n - 2; i++;) {
    res = pre1 + pre2;
    pre1 = pre2;
    pre2 = res;
  }
  return res;
}

int main() {
  int n = 6;
  int result = fibonacci_number(n);
  printf("Result: %d\n", result);
  return 0;
}
