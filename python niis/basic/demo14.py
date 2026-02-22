"""wap to calculate compound intrest"""
print("enter principle")
p=float(input())
print("enter rate")
r=float(input())
print("enter time")
t=float(input())
print("enter number of times compound")
n=int(input())
CI=p*(1+r/n)**(n*t)-p
print("compound intrest=",CI)