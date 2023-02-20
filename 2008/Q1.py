'''
start by finding all primes 3 - 10000
then for each number, subtract each prime and see if result is in primes
'''
prime_numbers = []

def is_prime(number):
    '''tests to see if a number is prime'''

    divider = 2
    while divider < number:
        if not number%divider:
            return False
        divider += 1
    
    return True

for next_number in range(2, 10001):
    result = is_prime(next_number)
    if result:
        prime_numbers.append(next_number)
    #print(f'{next_number} is prime: {result}')

#print(prime_numbers)

test_number = int(input('enter even number between 4 and 10,000: '))

goldbach_count = 0
for index, each in enumerate(prime_numbers):
    remainder  = test_number - each
    if remainder in prime_numbers[index:]:
        'we have a hit'
        print(f'goldbach_count: {test_number} = {each} + {remainder}')
        goldbach_count += 1

print(goldbach_count)

print(f'\n\nFind numbers which cannot be expressed as sum 2 primes 4-50')

for find_non_goldbachs in range(4, 50):
    goldbach_count = 0
    for index, each in enumerate(prime_numbers):
        remainder  = find_non_goldbachs - each
        if remainder in prime_numbers[index:]:
            'we have a hit'
            #print(f'goldbach_count: {find_non_goldbachs} = {each} + {remainder}')
            goldbach_count += 1
    if not goldbach_count:
        print(f'{find_non_goldbachs} is not a Goldbach number')