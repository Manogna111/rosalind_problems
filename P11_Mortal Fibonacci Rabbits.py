#Given: Positive integers n≤100 and m≤20.

#Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for months.

user_n = input("What is n:")
n = int(user_n)


user_m=input("What is m:")
m = int(user_m)
ages = [0]*(m)
ages[0] = 1

for i in range(1, n):
    newborns = sum(ages[1:])
    ages = [newborns] + ages[:-1] 

total_rabbits = sum(ages)
print(total_rabbits)