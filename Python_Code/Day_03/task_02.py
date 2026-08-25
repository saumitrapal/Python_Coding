# HEAD OR TAIL GAME USING RANDOMAIZATION

import random

random_number_0_to_1 = random.randint(0, 1) #print random integer number in between 0 to 1 

# print(type(random_number_0_to_1))

if random_number_0_to_1 == 0:
    print("Head!")
else:
    print("Tail")

