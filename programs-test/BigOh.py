"""
This program attempts to explain and explore the different Big O notations.
The (Big Oh) notation is used to describe the performance/efficiency or complexity of an algorithm.
Therefore, there are severak common notations that describe specific algorithms.
But the best way to understand this concept is to put it into practice and understand
the logic behind it, so you can analyze algorithms yourself and identify thair Big O notation.
In the end, it basically describes the behavior of the algorithm with respect to (perfomance or complexity) as the
input data increases.
"""
class BigOFunctions:
      """"
      first example O(n).
      This function has a complexity and efficiency of O(n) because the execution time of a specific 'print()'
      operation is linear and proportional to the amount of "numbers" in 'listNumbers', that is, if "listNumbers"
      has 8 numbers, the 'print()' operation will be executed 8 times.
      """
      def print_numbers(self, listNumbers: list[int]):
          for number in listNumbers:
              print(number)

# class realized and defined in memory as an object
BigOFunctions_instance = BigOFunctions()
listNumbers = [1, 2, 3, 4, 5, 6, 7, 8]
BigOFunctions_instance.print_numbers(listNumbers)
