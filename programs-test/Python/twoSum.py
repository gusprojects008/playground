# /usr/bin/python3.13.3

class Solution:
      #@staticmethod
      #def twoSum(InputNums: list[int], target: int) -> list[int]:
       #   return InputNums.append(target)

      def twoSum(self, InputNums: list[int], target: int) -> list[int]:
          ints_seen_mapped = {}
          index = 0

          for num in InputNums:             
              complement = target - num
              if complement in ints_seen_mapped.keys():
                 return ints_seen_mapped.get(complement), index, ints_seen_mapped, InputNums
              ints_seen_mapped[num] = index
              index += 1

#InputNums = [9, 9 ,7,11,15]
#target = 18
InputNums = [9, 9]
target = 18
solution_object = Solution() # embodies the class in an object in memory

print(solution_object.twoSum(InputNums, target)) #.twoSum(Nums, alvo))
