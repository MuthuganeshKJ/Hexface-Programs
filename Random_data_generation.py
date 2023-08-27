import random
from fractions import Fraction 

def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

def generate_pythagorus_triplet(complexity):
   
    complexity_list = [(1, 5), (6, 10), (11, 15), (16, 20), (21, 25)]

    starting_range = complexity_list[complexity-1][0]
    ending_range = complexity_list[complexity-1][1]
    m = random.randint(starting_range+1, ending_range)
    n = random.randint(starting_range, m-1)

    while(rdg.compute_hcf(m, n)==0):
        m = random.randint(starting_range+1, ending_range)
        n = random.randint(starting_range, m-1)

    a = abs((m*m)-(n*n))
    b = 2*m*n
    c = abs((m*m)+(n*n))

    print(a, b, c)

def get_random_integer(complexity):
    complexity_value_range = [(-5, 5), (-10,10), (-15,15), (-20, 20)]
    
    starting_range = complexity_value_range[complexity][0]
    ending_range = complexity_value_range[complexity][1]

    a = random.randint(starting_range, ending_range)
    return a

def get_random_complexnumber(complexity):

    a = get_random_integer(complexity)
    b = get_random_integer(complexity)
    cn = complex(a, b)
    return cn

def get_random_fraction(complexity):
    
    startRange = (10**(complexity-1))
    endRange = 10**complexity + 1
    a = random.randint(startRange, endRange)
    b = random.randint(startRange, endRange)
    while(a==b):
        b = random.randint(startRange, endRange)
    
    return Fraction(a, b)


def get_random_vector(complexity):

    i = get_random_integer(complexity)
    j = get_random_integer(complexity)
    k = get_random_integer(complexity)

    return [i, j, k]