num = int(input("Enter a number : "))

low = int(input("Enter lower limit : "))
up = int(input("Enter upper limit : "))

for i in range(1 , up + 1):
    if i**num in range(low , up):
        print(i)
