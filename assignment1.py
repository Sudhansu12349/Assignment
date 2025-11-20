# Name: Sudhansu Raj
# ID: 0157CS231200
# Batch: 6
# Time: 12:10-1:40

import math

# ==========================================
# SECTION 1: Basic If–Else Problems
# ==========================================

def basic_q1():
    """Question 1: Check whether a number is positive, negative, or zero."""
    print("\n--- Basic Q1 ---")
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

def basic_q2():
    """Question 2: Check whether a number is even or odd."""
    print("\n--- Basic Q2 ---")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

def basic_q3():
    """Question 3: Check if a given year is a leap year or not."""
    print("\n--- Basic Q3 ---")
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def basic_q4():
    """Question 4: Find the greatest of two numbers."""
    print("\n--- Basic Q4 ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num1 > num2:
        print(f"{num1} is greater")
    elif num2 > num1:
        print(f"{num2} is greater")
    else:
        print("Both are equal")

def basic_q5():
    """Question 5: Check whether a person is eligible to vote (age >= 18)."""
    print("\n--- Basic Q5 ---")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

def basic_q6():
    """Question 6: Check whether a given character is a vowel or consonant."""
    print("\n--- Basic Q6 ---")
    char = input("Enter a character: ").lower()
    if len(char) > 0 and char in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")

def basic_q7():
    """Question 7: Check if a number is divisible by 5."""
    print("\n--- Basic Q7 ---")
    num = int(input("Enter a number: "))
    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

def basic_q8():
    """Question 8: Determine number of digits (single, two, or more)."""
    print("\n--- Basic Q8 ---")
    num = int(input("Enter an integer: "))
    if -10 < num < 10:
        print("Single-digit number")
    elif -100 < num < 100:
        print("Two-digit number")
    else:
        print("More than two-digit number")

def basic_q9():
    """Question 9: Check whether a student has passed or failed (passing marks = 40)."""
    print("\n--- Basic Q9 ---")
    marks = int(input("Enter marks: "))
    if marks >= 40:
        print("Passed")
    else:
        print("Failed")

def basic_q10():
    """Question 10: Find whether the entered number is a multiple of both 3 and 7."""
    print("\n--- Basic Q10 ---")
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 7 == 0:
        print("Multiple of both 3 and 7")
    else:
        print("Not a multiple of both 3 and 7")


# ==========================================
# SECTION 2: Ladder If & Nested If
# ==========================================

def ladder_q1():
    """Question 1: Find the greatest among three numbers."""
    print("\n--- Ladder Q1 ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the greatest")
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest")

def ladder_q2():
    """Question 2: Classify a person based on age."""
    print("\n--- Ladder Q2 ---")
    age = int(input("Enter age: "))
    if age < 13:
        print("Child")
    elif 13 <= age <= 19:
        print("Teenager")
    elif 20 <= age <= 59:
        print("Adult")
    else:
        print("Senior")

def ladder_q3():
    """Question 3: Assign grades based on marks."""
    print("\n--- Ladder Q3 ---")
    marks = int(input("Enter marks: "))
    if 90 <= marks <= 100:
        print("Grade A")
    elif 75 <= marks <= 89:
        print("Grade B")
    elif 50 <= marks <= 74:
        print("Grade C")
    elif 35 <= marks <= 49:
        print("Grade D")
    else:
        print("Fail")

def ladder_q4():
    """Question 4: Check the type of triangle based on sides."""
    print("\n--- Ladder Q4 ---")
    s1 = float(input("Enter side 1: "))
    s2 = float(input("Enter side 2: "))
    s3 = float(input("Enter side 3: "))
    if s1 == s2 == s3:
        print("Equilateral")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Isosceles")
    else:
        print("Scalene")

def ladder_q5():
    """Question 5: Check if a character is uppercase, lowercase, digit, or special symbol."""
    print("\n--- Ladder Q5 ---")
    char = input("Enter a character: ")
    if len(char) == 1:
        if 'a' <= char <= 'z':
            print("Lowercase")
        elif 'A' <= char <= 'Z':
            print("Uppercase")
        elif '0' <= char <= '9':
            print("Digit")
        else:
            print("Special Symbol")
    else:
        print("Please enter a single character.")

def ladder_q6():
    """Question 6: Calculate electricity bill based on units."""
    print("\n--- Ladder Q6 ---")
    units = int(input("Enter units consumed: "))
    bill = 0
    if units <= 100:
        bill = units * 5
    elif 101 <= units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print(f"Total bill: Rs{bill}")

def ladder_q7():
    """Question 7: Determine the largest of four numbers using nested if."""
    print("\n--- Ladder Q7 ---")
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    n3 = int(input("Enter number 3: "))
    n4 = int(input("Enter number 4: "))
    
    largest = n1 
    if n1 > n2:
        if n1 > n3:
            if n1 > n4:
                largest = n1
            else:
                largest = n4
        else:
            if n3 > n4:
                largest = n3
            else:
                largest = n4
    else:
        if n2 > n3:
            if n2 > n4:
                largest = n2
            else:
                largest = n4
        else:
            if n3 > n4:
                largest = n3
            else:
                largest = n4
    print(f"Largest is {largest}")

def ladder_q8():
    """Question 8: Check if a given year is a century year and also a leap year."""
    print("\n--- Ladder Q8 ---")
    year = int(input("Enter a year: "))
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a century year and a leap year.")
        else:
            print("It is a century year but not a leap year.")
    else:
        print("It is not a century year.")

def ladder_q9():
    """Question 9: Classify BMI value."""
    print("\n--- Ladder Q9 ---")
    bmi = float(input("Enter BMI value: "))
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 24.9:
        print("Normal")
    elif 25 <= bmi <= 29.9:
        print("Overweight")
    else:
        print("Obese")

def ladder_q10():
    """Question 10: Display the smallest number among three using nested if."""
    print("\n--- Ladder Q10 ---")
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    n3 = int(input("Enter number 3: "))
    if n1 <= n2:
        if n1 <= n3:
            print(f"{n1} is the smallest")
        else:
            print(f"{n3} is the smallest")
    else:
        if n2 <= n3:
            print(f"{n2} is the smallest")
        else:
            print(f"{n3} is the smallest")


# ==========================================
# SECTION 3: For Loop Problems
# ==========================================

def for_q1():
    """Question 1: Print all Armstrong numbers between 100 and 999."""
    print("\n--- For Loop Q1 ---")
    print("Armstrong numbers between 100 and 999:")
    for num in range(100, 1000):
        sum_of_cubes = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum_of_cubes += digit ** 3
            temp //= 10
        if num == sum_of_cubes:
            print(num)

def for_q2():
    """Question 2: Generate and display the first n prime numbers."""
    print("\n--- For Loop Q2 ---")
    n = int(input("Enter the number of prime numbers to generate: "))
    count = 0
    num = 2
    print(f"First {n} prime numbers:")
    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
            count += 1
        num += 1
    print()

def for_q3():
    """Question 3: Display numbers from 1 to 500 divisible by 3, with digit sum <= 10."""
    print("\n--- For Loop Q3 ---")
    print("Numbers divisible by 3 with digit sum <= 10:")
    for num in range(1, 501):
        if num % 3 == 0:
            digit_sum = sum(int(digit) for digit in str(num))
            if digit_sum <= 10:
                print(num)

def for_q4():
    """Question 4: Print a pyramid of stars (*) of height n."""
    print("\n--- For Loop Q4 ---")
    n = int(input("Enter the height of the pyramid: "))
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

def for_q5():
    """Question 5: Check whether a string is a pangram."""
    print("\n--- For Loop Q5 ---")
    text = input("Enter a string: ").lower()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    is_pangram = True
    for char in alphabets:
        if char not in text:
            is_pangram = False
            break
    if is_pangram:
        print("It is a pangram.")
    else:
        print("It is not a pangram.")

def for_q6():
    """Question 6: Print all twin primes between 1 and 100."""
    print("\n--- For Loop Q6 ---")
    print("Twin primes between 1 and 100:")
    for num in range(3, 100):
        is_prime1 = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime1 = False
                break
        
        if is_prime1:
            num2 = num + 2
            is_prime2 = True
            for i in range(2, int(num2**0.5) + 1):
                if num2 % i == 0:
                    is_prime2 = False
                    break
            
            if is_prime2:
                print(f"({num}, {num2})")

def for_q7():
    """Question 7: Check if a number is a Harshad number."""
    print("\n--- For Loop Q7 ---")
    num_str = input("Enter a number: ")
    try:
        num = int(num_str)
        digit_sum = 0
        for digit in num_str:
            digit_sum += int(digit)
        if num % digit_sum == 0:
            print("It is a Harshad number.")
        else:
            print("It is not a Harshad number.")
    except ValueError:
        print("Please enter a valid integer.")

def for_q8():
    """Question 8: Generate Pascal's Triangle up to n rows."""
    print("\n--- For Loop Q8 ---")
    n = int(input("Enter the number of rows for Pascal's Triangle: "))
    for i in range(n):
        num = 1
        for j in range(1, i + 2):
            print(num, end=" ")
            num = num * (i - j + 1) // j
        print()

def for_q9():
    """Question 9: Display the sum of the series: 1^2 + 2^2 + ... + n^2."""
    print("\n--- For Loop Q9 ---")
    n = int(input("Enter the value of n: "))
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 2
    print(f"Sum of the series is: {total_sum}")

def for_q10():
    """Question 10: Check if a number is a Strong number."""
    print("\n--- For Loop Q10 ---")
    num_str = input("Enter a number: ")
    try:
        num = int(num_str)
        sum_of_facts = 0
        for digit_char in num_str:
            digit = int(digit_char)
            fact = 1
            if digit > 0:
                for i in range(1, digit + 1):
                    fact *= i
            sum_of_facts += fact
        
        if num == sum_of_facts:
            print("It is a Strong number.")
        else:
            print("It is not a Strong number.")
    except ValueError:
        print("Invalid input.")


# ==========================================
# SECTION 4: While Loop Problems
# ==========================================

def while_q11():
    """Question 11: Find reverse of a number and check if it is prime."""
    print("\n--- While Loop Q11 ---")
    num = int(input("Enter a number: "))
    rev_num = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        rev_num = rev_num * 10 + digit
        temp //= 10
        
    is_prime = True
    if rev_num < 2:
        is_prime = False
    else:
        i = 2
        while i * i <= rev_num:
            if rev_num % i == 0:
                is_prime = False
                break
            i += 1
            
    print(f"Reversed number is {rev_num}")
    if is_prime:
        print(f"{rev_num} is prime.")
    else:
        print(f"{rev_num} is not prime.")

def while_q12():
    """Question 12: Accept numbers until sum of digits > 100."""
    print("\n--- While Loop Q12 ---")
    total_digit_sum = 0
    while total_digit_sum <= 100:
        num_str = input("Enter a number: ")
        current_digit_sum = sum(int(d) for d in num_str if d.isdigit())
        total_digit_sum += current_digit_sum
        print(f"Current total digit sum: {total_digit_sum}")
    print("Total digit sum exceeded 100. Exiting.")

def while_q13():
    """Question 13: Check whether a number is a Duck number."""
    print("\n--- While Loop Q13 ---")
    num_str = input("Enter a number: ")
    if num_str.startswith('0'):
        print("Not a Duck number (starts with zero).")
    else:
        has_zero = False
        i = 0
        while i < len(num_str):
            if num_str[i] == '0':
                has_zero = True
                break
            i += 1
        if has_zero:
            print("It is a Duck number.")
        else:
            print("It is not a Duck number.")

def while_q14():
    """Question 14: Check if a number is a Happy number."""
    print("\n--- While Loop Q14 ---")
    num = int(input("Enter a number: "))
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        temp_num = num
        sum_sq = 0
        while temp_num > 0:
            digit = temp_num % 10
            sum_sq += digit ** 2
            temp_num //= 10
        num = sum_sq
    if num == 1:
        print("It is a Happy number.")
    else:
        print("It is not a Happy number.")

def while_q15():
    """Question 15: Find the largest prime factor of a given number."""
    print("\n--- While Loop Q15 ---")
    n = int(input("Enter a number: "))
    largest_factor = -1
    d = 2
    while d * d <= n:
        while n % d == 0:
            largest_factor = d
            n //= d
        d += 1
    if n > 1:
        largest_factor = n
    print(f"Largest prime factor is {largest_factor}")

def while_q16():
    """Question 16: Accept a string until it is a palindrome."""
    print("\n--- While Loop Q16 ---")
    while True:
        s = input("Enter a string: ")
        if s == s[::-1]:
            print("Palindrome detected! Exiting.")
            break
        else:
            print("Not a palindrome. Try again.")

def while_q17():
    """Question 17: Find the digital root of a number."""
    print("\n--- While Loop Q17 ---")
    num = int(input("Enter a number: "))
    while num > 9:
        sum_digits = 0
        temp = num
        while temp > 0:
            sum_digits += temp % 10
            temp //= 10
        num = sum_digits
    print(f"The digital root is: {num}")

def while_q18():
    """Question 18: Generate the Collatz sequence for a given number."""
    print("\n--- While Loop Q18 ---")
    n = int(input("Enter a number for Collatz sequence: "))
    while n != 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

def while_q19():
    """Question 19: Check whether it is a Kaprekar number."""
    print("\n--- While Loop Q19 ---")
    num = int(input("Enter a number: "))
    sq = num * num
    sq_str = str(sq)
    is_kaprekar = False
    i = 1
    while i < len(sq_str):
        part1_str = sq_str[:i]
        part2_str = sq_str[i:]
        # Ensure part2 is not zero if it's being converted (though int('00') is 0)
        if int(part1_str) + int(part2_str) == num and int(part2_str) != 0:
             is_kaprekar = True
             break
        i += 1
    
    # Edge case for 1
    if num == 1: is_kaprekar = True
        
    if is_kaprekar:
        print("It is a Kaprekar number.")
    else:
        print("It is not a Kaprekar number.")

def while_q20():
    """Question 20: Simulate an ATM machine."""
    print("\n--- While Loop Q20 ---")
    balance = 1000.0
    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            print(f"Your balance is Rs{balance}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited Rs{amount}. New balance: Rs{balance}")
            else:
                print("Invalid deposit amount.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance.")
            elif amount <= 0:
                print("Invalid withdrawal amount.")
            else:
                balance -= amount
                print(f"Successfully withdrew Rs{amount}. New balance: Rs{balance}")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# ==========================================
# MAIN EXECUTION BLOCK
# ==========================================
if __name__ == "__main__":
    # To run a specific question, uncomment the function call below.
    # Example: To run Question 1 from Basic section:
    
    # basic_q1()
    
    # You can call any function defined above. 
    # For example, to test the ATM machine:
    while_q20()
