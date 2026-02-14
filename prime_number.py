'''
Check if a number is prime or not.
Takes user input and validates input.
Continues until the user decides to exit.
'''
def is_prime(num):
    '''
    This function checks if a number is prime or not.
    
    Args:
        (num) User input number
    Returns:
        (True) if the number is prime, (False) otherwise
    '''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    try:
        # Get user input
        user_input = input("Enter a number (e)-to exit): ")

        if user_input.lower() == 'e':
            print("Exiting the program.")
            break
        number = int(user_input)

        # Check if the number is prime with the function
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Please enter a valid integer.")
