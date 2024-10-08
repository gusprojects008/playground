if __name__ == '__main__':
   x = int(input())
   y = int(input())
   z = int(input())
   n = int(input())

   list_inters = []

   # LIST COMPREHENSION METHOD
   list_comprehension_int = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range (z+1)]

   all_list_inters = [list_int for list_int in list_comprehension_int if sum(list_int) != n]

   print(all_list_inters)
 
   #print(f"\n{list_inters}\n{sum(x, y, z)}")
