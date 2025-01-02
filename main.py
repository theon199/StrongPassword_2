#This program generates a strong password

import random as rand

#These lists were generated using the help of AI, that is it
letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
numbers = [str(i) for i in range(10)]
symbols = [chr(i) for i in range(ord('!'), ord('/')+1)] + [chr(i) for i in range(ord(':'), ord('@')+1)] + [chr(i) for i in range(ord('['), ord('_')+1)] + [chr(i) for i in range(ord('{'), ord('~')+1)]
password = []

def generator():
    start = input("Hello, would you like to generate a password? ").lower()
    if start == "yes" or "y":
        length = int(input("How long would you like your password to be? "))
        for i in range(length):
            password.append(rand.choice(letters).upper())  #Only uppercase, need to fix, reference the OneNote
    end = "".join(password)
    print(f"Here is your password: {end}")

generator()