
# UNDERSTEND THE FUNCTION __init__ AND self IN CLASS PYTHON

# __init__ IS A FUNCTION EXECUTED ALWAYS THAT THE CLASS IS USED IN NEW OBJECT THROUGH THE FUNCTION.
class Person:
      # self IS PARAMETER USED FOR REFERENCE THE VALUES FROM INSTANTIATED CLASS AND FUNCTIONS  
      def __init__(self, color, name, age): # THE FUNCTION __Init__ IS INITIALIZED ALWAYS THAT THE CLASS Person IS USED AND INTANTIATED
          self.color = color                # AS A OBJECT IN A NEW VARIABLE, THEN THE FUNCTION __init__
          self.name = name                  # RECEIVE 3 VALUES color, name, age. AND EXECUTED THIS VALUES.
          self.age = age                  # WITH self WE CAN REFERENCE THE VALUES CLASS AND FUNCTION
          print(f"Person: {self.color}, {self.name}, {self.age}")

# __init__ IS A FUNCTION CALLED AUTOMATICALLY ALWAYS THAT THE CLASS Person IS USED FOR CREATE A NEW OBJECT
define_person = Person("Black", "Gustavo", "16") # EXECUTE THE FUNCTION __init__ AND STORE THE RESULT OF: print(f"Person: {self.color}, {self.name}, {self.age}")

print(define_person)
