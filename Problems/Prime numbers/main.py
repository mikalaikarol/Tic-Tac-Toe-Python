prime_numbers = []
for i in range(2, 1000):
    numbers = [i % number for number in range(2, i)]
    if all(numbers):
        prime_numbers.append(i)
