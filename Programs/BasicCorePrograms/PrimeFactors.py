n=int(input("Enter an integer:"))#Take number from user

def PrimeFactors(n):#Define Function
    i=1 ;count=0#Initialize the i variable
    while (i <= n):#Travesing using While loop
        if (n % i == 0):#If number is divisible by i then assign j=1,else out if the loop
            j = 1
            while (j <= i):#Checking Condition
                count = count + 1  # Increment count
                if (i % j == 0 and count == 2):

                j = j + 1
                print(i)
        i = i + 1

PrimeFactors(n)