#include <stdio.h>
#include <stdlib.h>

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

  *result  = 0;
  free(result);
  return NULL;
};

int main() {
  int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int target = 5;
  size_t numsSize = sizeof(nums) / sizeof(nums[0]);
  size_t returnSize;
  int* result = twoSum(nums, numsSize, target, &returnSize);
  
  if (result != NULL) {
    printf("first number from 'nums' array: %d\nsecond number from 'nums' array: %d\nresult of the sum: %d\n", result[0], result[1], result[0] + result[1]);
  }
}
