def collatz(number):
    if number % 2 == 0:
        result= number // 2
    else:
        result= 3 * number + 1
    return result
try:
        user_input = int(input("Please enter a Number: "))
        while user_input != 1:
            user_input = collatz(user_input)
            print(user_input)
except ValueError:
     print("You need to pass an Integer!")



