def generate_collatz_sequence(n):
    sequence = [n]  
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
n = 5
collatz_sequence = generate_collatz_sequence(n)
print(collatz_sequence)
