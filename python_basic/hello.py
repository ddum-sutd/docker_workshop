# hello.py
import random
from lorem_text import lorem

def generate_random_number():
    return random.randint(1, 100)

def say_hello():
    print("Hello world ..");
    
def generate_lorem_ipsum_text():
    return lorem.sentence()
    
def main():
    say_hello()
    print()
    random_number1 = generate_random_number()
    print("Random number 1:", random_number1)
    
    random_number2 = generate_random_number()
    print("Random number 2:", random_number2)
    
    sum_value = random_number1 + random_number2
    print("Sum of the above 2 random numbers: ", sum_value)
    
    print()
    lorem_ipsum_text = generate_lorem_ipsum_text()
    print("Lorem Text generated:", lorem_ipsum_text)
    
   
if __name__ == "__main__":
    main()
