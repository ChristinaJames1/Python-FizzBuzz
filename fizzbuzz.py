instructions = """This code will count from numbers 1 to 100;

   multiples of 3, will display 'Fizz'
   multiples of 5, will display 'Buzz' 
   multiples of 3 & 5, will display 'FizzBuzz' 
   
all other numbers will display as (n),themselves."""

print(instructions)
print()

for n in range (1,101):
    if n % 15 == 0:
        print ("FizzBuzz")
    elif n % 3 == 0:
        print ("Fizz")
    elif n % 5 == 0:
        print ("Buzz")
    else: print (n)