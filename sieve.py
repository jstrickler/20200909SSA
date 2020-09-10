

LIMIT = 100000

LIMIT += 1

is_prime = [True] * LIMIT

for num_to_check in range(2, LIMIT):
    if is_prime[num_to_check]:  # check if prime
        print(num_to_check, end=' ')
        for multiple in range(2 * num_to_check, LIMIT, num_to_check):
            is_prime[multiple] = False  # mark as non-prime
print()
