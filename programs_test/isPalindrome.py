class Solution:
      def isPalindrome(self, x: int): # -> bool:
          listInts = [number for number in str(x)]
          if listInts[0] == listInts[-1]:
             return True
          else:
             return False
x = -121
SolutionObj = Solution()
print(SolutionObj.isPalindrome(x))
