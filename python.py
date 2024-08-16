def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    
    name = input("Hello! What's your name? ")
    
    
    print(f"Nice to meet you, {name}! Let's explore some numbers together.")
    numbers = []
    for i in range(3):
        number = int(input(f"Enter favorite number {i+1}: "))
        numbers.append(number)
    
    print(f"\nThank you, {name}! You've chosen {numbers}. Let's analyze them!")


    even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    
    print("\nHere's what we found:")
    for num, eo in even_odd_list:
        print(f"The number {num} is {eo}.")
    
    squares_list = [(num, num ** 2) for num in numbers]
    
    print("\nLet's check out their squares:")
    for num, square in squares_list:
        print(f"The square of {num} is {square}. That's pretty cool, right?")
    
    total_sum = sum(numbers)
    
    
    print(f"\nThe sum of your numbers is {total_sum}. Great job!")
    
    if is_prime(total_sum):
        print(f"Wow! The sum {total_sum} is a prime number! That's awesome!")
    else:
        print(f"The sum {total_sum} is not a prime number, but it's still an interesting number!")

if __name__ == "__main__":
    main()
