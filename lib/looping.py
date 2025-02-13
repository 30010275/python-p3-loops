def happy_new_year():
    count = 10
    while count > 0:
        print(count)  # Corrected indentation
        count -= 1  # This line was incorrectly indented
    print("Happy New Year!")  # This should print once after the loop ends

def square_integers(int_list):
    return [num ** 2 for num in int_list]

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
