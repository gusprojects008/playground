#include <stdlib.h>
#include <stdio.h>

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

int main() {
  int x;
  printf("Type it a number: ");
  scanf("%d", &x);
  int result = isPalindrome(x);
  if (result == 1) {
    printf("Is a Palindrome! %d %d\n", result, x);
  } else {
    printf("Isn't a Palindrome! %d %d\n", result, x);
  }
}
