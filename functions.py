import random

# from my_functions import greet
import my_functions

#a = append
#w = write

with open("data.txt", "a") as file: # opens a txt file
    # file.write("90\n")
    # file.write("68\n")
    for temp in range(100):
        # file.write(str(temp)+"\n")
        # x = random.randint(1,100)
        x = random.randint(-1, 15)
        file.write(str(x) + "\n")

with open("data.txt", "r") as file:
    content = file.read() # 0 params 0 args
    print(content)

# my_functions.greet()
# print(my_functions.greet())

from my_functions import greet
greet()