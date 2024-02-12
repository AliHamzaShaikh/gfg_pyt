#Geometric Progression
'''A person gets 5000 as salary on 1 Jan 2020 The salary
doubles every year  Find the salary that the person will get on 1 Jan 2030'''

a = int(input("Enter a: "))
r = int(input("Enter r: "))
n = int(input("Enter n: "))
res = a*r**(n-1)
print(res)