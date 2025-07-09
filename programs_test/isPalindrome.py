class Solution:
      def isPalindrome(self, x: int) -> bool:
          # Bad solution
          #listInts = [number for number in str(x)]
          #if listInts[0] == listInts[-1]:
          #   return True
          #else:
          #   return False

          # Good solution
          if x < 10:
             return False
          result = 0
          default = x
          x = abs(x)
          while x != 0:
                result = result * 10 + (x % 10)
                x //= 10
          return result == default

x = -1421
SolutionObj = Solution()
print(SolutionObj.isPalindrome(x))
