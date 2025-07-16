def fibonacci_sequence():
    int_user = int(input("Type it a number: "))
    zero, one = 0, 1
    while zero < int_user:
          print(one)
          zero, one = one, zero + one
fibonacci_sequence()
