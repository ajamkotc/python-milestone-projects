'''Sieve of Eratosthenes

Used to find all prime numbers less than an inputted number

1. Create a list of numbers from 2 to n
2. Start with 2
3. Mark/Remove all numbers that are a multiple of 2 AND greater than or equal to its square
4. Move to next available number'''

import pdb

def display_sieve(prime_list):
    '''Displays a sieved list where disqualified nums are set to 0

    Params
    ------
    prime_list : list'''


    for num in prime_list:
        if num != 0:
            print(num)

def sieve(n):
    '''Method to carry out Sieve of Eratostehenes algorithm.

    Params
    ------
    n : int
        number to which primes should be counted

    Returns
    -------
    number_list : list
        List of prime numbers where non-prime are set to 0'''

    number_list = [i for i in range(2,n+1)]

    for index, number in enumerate(number_list):
        if number == 0:
            continue
        else:
            for index2, num in enumerate(number_list[index+1:]):
                # pdb.set_trace()
                if num%number == 0 and num >= number**2:
                    number_list[index2+index+1] = 0

    return number_list

if __name__ == '__main__':
    display_sieve(sieve(997))
