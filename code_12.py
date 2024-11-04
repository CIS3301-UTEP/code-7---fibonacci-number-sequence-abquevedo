import random 
def get_fibonacci_number(position):
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)

def get_fibonacci_number_sequence(number):
    fibonacci_sequence = []
    for i in range(number): 
        fibonacci_sequence.append(get_fibonacci_number(i))
    return fibonacci_sequence

if __name__ == "__main__":
    # Testing the get_fibonacci_number function
    position = 8
    print(f"Fibonacci number position is {position}:", get_fibonacci_number(position))

    # Testing the get_fibonacci_number_sequence function
    number = 10
    print(f"Fibonacci sequence for {number} elements:", get_fibonacci_number_sequence(number))

