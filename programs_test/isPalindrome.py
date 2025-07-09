class Solution:
      def isPalindrome(self, x: int) -> bool:
          # WTF?
          #listInts = [number for number in str(x)]
          #if listInts[0] == listInts[-1]:
          #   return True
          #else:
          #   return False

          # i thought of something (my solution)
          if x < 0:
             return False 

          listInts = [number for number in str(x)]
          reverseList = []
          i = 0

          for numberstr in listInts:
              reverseList.insert(i, numberstr)
              i -= 1

          return True if (reverseList == listInts) else False

          # Good and ideal solution
          #if x < 10:
          #   return False
          #result = 0
          #default = x
          #x = abs(x)
          #while x != 0:
            #    result = result * 10 + (x % 10)
           #     x //= 10
          #return result == default

x = 121
SolutionObj = Solution()
print(SolutionObj.isPalindrome(x))
