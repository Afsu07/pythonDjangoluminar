num = input("Enter a number : ")
i = 1
data = 0
while i <= int(num):
    res = num * i
    print( res ," + ",end=" ")

    data = data + int(res)

    i = i + 1

print("=", data)
