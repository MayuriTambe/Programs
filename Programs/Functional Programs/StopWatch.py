# To find Start,Stop and Elapsed time for StopWatch

import time  # import time Function to calculate Start,Stop and Elapsed Time

class Time1:
    def Elapsed(self, start, stop):
        start = 0
        stop = 0
        start = int(input("Enter 1 to start"))  # Take input to start Time
        start = time.time()  # time()function returns the number of seconds passed
        print(start)  # Display result

        stop = int(input("Enter 2 to stop"))  # Take input to stop Time
        stop = time.time()
        print(stop)  # Display Result

        Elapsed = (stop - start)  # Take Diffrence between Stop and Start time
        print("The Elapsed Time:", Elapsed)  # Display Elapsed time

start=0
stop=0
time1=Time1()
time1.Elapsed(start,stop)

