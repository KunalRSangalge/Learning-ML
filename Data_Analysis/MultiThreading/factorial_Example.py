'''
multiprocessing for heavy calculation
Factorial calculation for large numbers - improve performance
'''
import multiprocessing
import time
import sys
import math

#increase number of digits for integer conversion

# sys.set_int_max_str_digits(100000)

def compute_fact(num):
    print(f"factorial of {num}")
    result = math.factorial(num)
    print(result)
    return result

if __name__ == "__main__":
    numbers = [199,5000,2000,1221]
    start = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_fact,numbers)
    
    end = time.time()

    print(results)
    print(end-start)
    