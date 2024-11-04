import random 

def get_fibonacci_number(position):
    if position < 0:
        return 0
    elif position == 0:
        return 0
    elif position == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, position + 1):
        a, b = b, a + b
    return b

def get_fibonacci_number_sequence(number):
    fibonacci_sequence = []
    if number >= 1:
        fibonacci_sequence.append(1)
    if number >= 2:
        fibonacci_sequence.append(1)
    for i in range(2, number):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
        
    return fibonacci_sequence

if __name__ == "__main__":
    # Testing the get_fibonacci_number function
    position = 8
    print(f"Fibonacci number position is {position}:", get_fibonacci_number(position))

    # Testing the get_fibonacci_number_sequence function
    number = 10
    print(f"Fibonacci sequence for {number} elements:", get_fibonacci_number_sequence(number))

