# TRYING UNDERSTAND THE WORKING OF FUNCTIONS SPECIALLYS AS __init__ __main__ AND self
# THIS FUNCTIONS THEY ARE USEDS IN CLASS FOR MANIPULATION DE VALUES AND FUNCTIONS IN OTHERS CLASS ABOUT HIERARCHY

# THE FUNCTION __init__ IS USED FOR CALL AND INIT A CLASS AND EXECUTE THE FUNCTION THATS IN IT

# THE FUNCTION __main__ IS USED FOR EXECUTE A CODE IF THE FILE WITH CODE BE EXECUTING AS PROGRAM MAIN, IF A CODE WITH FUNCTION:
# if __name__ == '__main__': code block         HE ONLY BE EXECUTED IF GO RUNNIG AS PROGRAM PRINCIPAL AND DON'T BE EXECUTED IF IMPORTED AS MODULE
# WHY LIKE THIS WILL BE EXECUTED WITH PROGRAM SECUNDARY IN A FILE SECUNDARY

# self IS A ARG USED FOR REFERENCE A OBEJECTS AND INSTANCIES OF THE CLASS ACTUALLY 

#import sys
import subprocess

# self IS USED FOR REFERECIE OF THE OBJECTS PARAMETERS OF FUNCTION THAT INIT WITH IN CLASS Person
class Person:
      def __init__(self, age, name, sex):
          self.age = age
          self.name = name
          self.sex = sex

idade = 16
nome = "gustavo" 
sexo = "masculino"

# PERSONALIDA
identity = Person(idade, nome, sexo)

print(identity.name)
          
if __name__ == '__main__':
   print("Executed the program as instancie main!!!")
