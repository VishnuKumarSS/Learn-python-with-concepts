# prime number is a number which is divisible by 1 and itself. (condition: It should be divisible by exactly 2 numbers (i.e) 1,itself) 
def prime_checker(number):
    if number>0:
        if number==1:
            print("Its not a prime number.")
        elif number>1:
            for i in range(2,number):
                if number%i==0:
                    print("Its not a prime number.")
                    break
            else:
                print("its a prime number.")
    else:
        print("Enter a valid number.")
n=int(input("Enter a number to check for the prime number: "))
prime_checker(n) # or prime_checker(number=n)