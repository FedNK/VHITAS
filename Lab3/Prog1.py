import random
import numpy as np

DEFAULT_ACCURACY = 3

def summ(first, second):
    """returns sum of 2 numbers"""
    return first + second

def div(x, y, accuracy):
    """returns round of 2 numbers"""
    return round(x/y, accuracy)

def get_rand():
    """returns rnd number from 1 to 10"""
    return random.randint(1, 10)

def rand_array():
    """returns array of rnd numbers"""
    a = [get_rand(), get_rand(), get_rand()]
    return np.array(a)

def main():
    """returns nothing"""
    pass

main()
