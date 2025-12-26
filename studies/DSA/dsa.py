def fibonacci_sequence():
    int_user = int(input("Type it a number: "))
    zero, one = 0, 1
    while zero < int_user:
          print(one)
          zero, one = one, zero + one

def isPalindrome(self, x: int) -> bool:
    if x < 0:
       return False 

    listInts = [number for number in str(x)]
    reverseList = []
    i = 0

    for numberstr in listInts:
        reverseList.insert(i, numberstr)
        i -= 1

    return True if (reverseList == listInts) else False

def mergeStringsAlternately(word1, word2):
    lenw1 = len(word1)
    lenw2 = len(word2)
    i = 0
    result = []
    while i < lenw1 or i < lenw2:
       if i < lenw1:
           result.append(word1[i])
       if i < lenw2:
           result.append(word2[i])
       i += 1
    return ''.join(result)

def gcdOfStrings(str1, str2):
    str1,str2 = (str1,str2) if len(str1) <= len(str2) else (str2,str1)
    str1len, str2len = len(str1), len(str2)
    if str1 + str2 != str2 + str1:
        return ""
    if len(str1) == len(str2):
        return str1
    if len(str1) > len(str2):
        return gcdOfStrings(str1[len(str2):], str2)
    return gcdOfStrings(str1, str2[len(str1):])

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    candidatoMajor = candies[0]
    result = []
    for candy in candies:
        if candy + extraCandies >= candidatoMajor:
            candidatoMajor = candy + extraCandies
    for candy in candies:
        candy += extraCandies
        if candy + extraCandies >= candidatoMajor:
            result.append(True)
        else:
           result.append(False)
    print(result)

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    i = 0
    length = len(flowerbed)
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            left_empty = (i == 0) or flowerbed[i - 1] == 0
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            if left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
                i += 2
                continue
            i += 1
        
def reverseVowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    wl = list(s)
    start = 0
    end = len(s) - 1

    while start < end:
        while start < end and vowels.find(wl[start]) == -1:
            start += 1
        while start < end and vowels.find(wl[end]) == -1:
            end -= 1
        wl[start], wl[end] = wl[end], wl[start]
        start += 1
        end -= 1

    return "".join(wl)
        
s = "eguavoa"
print(reverseVowels(s))
