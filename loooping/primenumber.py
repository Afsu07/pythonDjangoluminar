low = int(input("Enter the lower number : "))
up = int(input("Enter the upper number : "))

for number in range (low,up+1):
        flag=0
        for i in range(2,number):
            if(number%i==0):
                flag=1
                break
            else:
               flag=0
        if(flag==0):
            print(number)
