from leonhard import leonhard

# Get the factors of 10
# [1, 2, 5, 10]
print(leonhard.get_factors_of_positive_integer(10))

# Default fibonacci sequence
# Two terms, starting with 0 and 1
# [0, 1]
print(leonhard.generate_fibonacci_sequence())

# Fibonacci sequence with 5 terms, starting with 0 and 1
# [0, 1, 1, 2, 3]
print(leonhard.generate_fibonacci_sequence(5))

# Fibonacci sequence with 5 terms, starting with 3 and 6
# [3, 6, 9, 15, 24]
print(leonhard.generate_fibonacci_sequence(5, 3, 6))

# 600851475143 is not prime
print(leonhard.is_prime(600851475143))

# 7652413 is prime
print(leonhard.is_prime(7652413))

# Is a Pythagorean triplet
print(leonhard.is_pythagorean_triplet(3, 4, 5))

# Is not a Pythagorean triplet
print(leonhard.is_pythagorean_triplet(1, 2, 3))

# Number of digits is 3
print(leonhard.count_digits(256))

# Collatz sequence
print(leonhard.generate_collatz_sequence(10, []))

# Cyclic permutation
print(leonhard.generate_cyclic_permutation(123))

# Triangle numbers
print(leonhard.is_triangle_number(3))
print(leonhard.is_triangle_number(4))