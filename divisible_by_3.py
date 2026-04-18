start=int(input("Enter the starting no.: "))
end=int(input("Enter the ending no.: "))

print(f"Numbers divisible by 3 from {start} to {end}: ")
for num in range(start,end+1):
    if num % 3==0:
        print(num)