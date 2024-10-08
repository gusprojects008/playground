if __name__ == '__main__':
   x = int(input())
   y = int(input())
   z = int(input())
   n = int(input())

   list_inters = []

   val_sum_inters = sum(list_inters)

   # EXPRESSION: I, J, K
   for i in range(x):
       for j in range(y):
           for k in range(z):
               if i + j + k != n:
                  list_inters.append((i, j, k))
   #print(list_inters)

   # LIST COMPREHENSION METHOD
   list_comprehension_int = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range (z+1)]
#   list_inters_comprehension = [possibles_int for possibles_int in list_]

   value_list = [sum_list for sum_list in list_comprehension_int if sum(sum_list) != n]
   
   print([sum_list for sum_list in list_comprehension_int if sum(sum_list) != n])
 
   #print(f"\n{list_inters}\n{sum(x, y, z)}")
