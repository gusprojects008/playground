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
  for (int i = 0; i < n - 2; i++) {
    res = pre1 + pre2;
    pre1 = pre2;
    pre2 = res;
  }
  return res;
}

int* twoSumBruteForce(int* nums, size_t numsSize, int target, size_t* returnSizePtr) {
  *returnSizePtr = 2;
  int* result = malloc(sizeof(int) * *returnSizePtr);
  for (int i = 0; i < numsSize; i++) {
    for (int j = i + 1; j < numsSize; j++) {
      int n1 = nums[i];
      int n2 = nums[j];
      if (n1 + n2 == target) {
        result[0] = i;
        result[1] = j;
        return result;
      };
    };
  };
  free(result);
  *returnSizePtr = 0;
  return NULL;
}

int* twoSumHashmapSolution(int* nums, size_t numsSize, int target, size_t* returnSizePtr) {
  typedef struct {
    int key;
    int value;
    bool used;
  } HashItem; // bucket == HashItem
  int hash(int key, size_t size) {
    if (key < 0) key = -key; // transforming key (which is already in negative form) into positive, example (key = 1): -(-1) == 1
    return key % size; // Returns a unique index used to locate the bucket in the hash table.
  };
  size_t tableSize = numsSize * 2; // Memory must be allocated for twice the number of elements to be mapped in the hash table, for reasons of reliability, stability, and security.
  HashItem* table = calloc(tableSize, sizeof(HashItem));
  for (int i = 0; i < numsSize; i++) {
    int complement = target - nums[i];
    int idx = hash(complement, tableSize);

    while (table[idx].used) {
      if (table[idx].key == complement) {
        int* result = malloc(sizeof(int) * 2);
        result[0] = table[idx].value;
        result[1] = i;
        *returnSizePtr = 2;
        free(table);
        return result;
      };
      idx = (idx + 1) % tableSize; 
    }

    idx = hash(nums[i], tableSize);
    while (table[idx].used) {
      idx = (idx + 1) % tableSize; // Moves one bucket forward in the hash table.
    }

    table[idx].key = nums[i];
    table[idx].value = i;
    table[idx].used = true;
  }
  free(table);
  *returnSizePtr = 0;
  return NULL;
}

int** findDifference(int* nums1, size_t nums1Size, int* nums2, size_t nums2Size, int* returnSize, int** returnColumnSizes) {
  typedef struct {
    int key; // is num value
    bool used;
  } bucket; // HashItem

  int hash(int key, size_t table_size) {
    if (key < 0) key = -key;
    return key % table_size;
  };

  int contains (bucket* table, size_t size, int target) {
    int idx = hash(target, size);
    while (table[idx].used) {
      if (table[idx].key == target) return true;
      idx = (idx + 1) % size;
    };
    return false;
  };

  void insert(bucket* table, size_t size, int key) {
    int idx = hash(key, size);
    while (table[idx].used) {
      if (table[idx].key == key) return;
      idx = (idx + 1) % size;
    };
    table[idx].key = key;
    table[idx].used = true;
  };

  size_t size1 = nums1Size * 2;
  size_t size2 = nums2Size * 2;

  bucket* hashtable1 = calloc(size1, sizeof(bucket));
  bucket* hashtable2 = calloc(size2, sizeof(bucket));

  int* res1 = calloc(nums1Size, sizeof(int));
  int* res2 = calloc(nums2Size, sizeof(int));

  for (int i = 0; i < nums1Size; i++) insert(hashtable1, size1, nums1[i]);
  for (int i = 0; i < nums2Size; i++) insert(hashtable2, size2, nums2[i]);

  int c1 = 0, c2 = 0; 

  size_t addedNumsSize = size1 + size2;
  bucket* addedNums = calloc(addedNumsSize, sizeof(bucket));

  for (int i = 0; i < nums1Size; i++) {
    if (!contains(hashtable2, size2, nums1[i]) && !contains(addedNums, addedNumsSize, nums1[i])) {
       res1[c1++] = nums1[i];
       insert(addedNums, addedNumsSize, nums1[i]); 
    };
  };

  for (int i = 0; i < nums2Size; i++) {
    if (!contains(hashtable1, size1, nums2[i]) && !contains(addedNums, addedNumsSize, nums2[i])) {
       res2[c2++] = nums2[i];
       insert(addedNums, addedNumsSize, nums2[i]);
    };
  };

  int** answer = malloc(sizeof(int*) * 2);
  answer[0] = res1;
  answer[1] = res2;
  
  *returnSize = 2;

  *returnColumnSizes = malloc(sizeof(int) * 2);
  (*returnColumnSizes)[0] = c1;
  (*returnColumnSizes)[1] = c2;
  
  free(hashtable1);
  hashtable1 = NULL;
  free(hashtable2);
  hashtable2 = NULL;
  return answer;
}

//int** findDifferecneBt(int* nums1, size_t nums1Size, int* nums2, size_t nums2Size, int* returnSize, int* returnColumnSizes) {};

int main() {
  int nums1[] = {0, 1, 4, 4};
  int nums2[] = {0, 1, 0, 1};
  size_t nums1Size = sizeof(nums1) / sizeof(nums1[0]), nums2Size = sizeof(nums2) / sizeof(nums2[0]);
  int returnSize;
  int* returnSizePtr = &returnSize;
  int* returnColumnSizes = NULL;
  int** returnColumnSizesPtr = &returnColumnSizes;
  int** result = findDifference(nums1, nums1Size, nums2, nums2Size, returnSizePtr, returnColumnSizesPtr);
  
  if (result != NULL) {
    int i = 0;
    while (i < *returnSizePtr - 1) {
      for (int j = 0; j < returnColumnSizes[0]; j++) {
        printf("%d ", result[i][j]);
      };
      i++;
      printf("\n");
      for (int k = 0; k < returnColumnSizes[1]; k++) {
        printf("%d ", result[i][k]);
      };
    };
    printf("\n");
  };
  free(result);  
  return 0;
}
