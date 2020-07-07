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