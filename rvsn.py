from cgitb import small
from curses import KEY_SAVE
from locale import currency
from re import A
from traceback import print_list


a=30
b=10
print(a+b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)
print(a**b)
print(a*b)
3==3
print(3==3)
4!=3
print(4==3)
6<3
print(6<3)
6>3
print(6>3)
a="angela"
print(a)
a=20
print(a)
a=20
a+=10
print(a)
b=40
b-=10
print(b)
c=18
c*=23
print(c)
d=12
d/=31
print(d)
d=9
d//=4
print(d)
#escaping strings
print("hello\b Nina")
print("hello\r Mima")
print("hello\n Rehema")
print("hello\t Angie")
print("hello\v Joy")
print("hello\a Gabu")
print("hello\f jojo")

#String methods
school="Akirachix"
print(school.upper())
print(school.lower())
print(school.title())
print(school.capitalize())
print(school.count("a"))
print(school.replace("i","y"))
print(school.endswith("a"))
print(school.startswith("A"))
print(school.islower())
print(school.isupper())
print(school.isalpha())
print(school.isalnum())
print(school.index("c"))

#Check if a string exists
name="Watermelon"
print("melon" in name)
print("Water" not in name)
 #string formating
people="school{:>5} students"
print(people.format(27))
txt="the price is {:5f} dollars"
print(txt.format(31))
txt="the price is {:=5} dollars"
print(txt.format(-3))
txt="the price is {:+} and {:+} dollars"
print(txt.format(-2,4))
txt="the price is {:,} dollars"
print(txt.format(1000000000000099999089))
txt="the price is {:5f} dollars"
print(txt.format(31))
#indexing
school="AKIRACHIX"
print(school[2:5])
print(school.index('C'))
print(school[5])
campus="KALPATAS"
print(campus[1:6])
print(campus[ :5])
amount=1300
balance=600
amount=input("enter amount to withdraw")
print("confirmed you have withdrawn" , amount, "your new balance is", amount-balance)



x = [100,110,120,130,140,150]
# for n in x:print(n*5)
new_list=[m*5 for m in x]
print(new_list)

#  a function named divisible_by_three that accepts a number n and 
#prints all numbers from 1 to n that are divisible by 3. 
divisible_by_three = int(input("Enter a number"))
if(divisible_by_three%3==0):
    print("{} is divisiblenby :".formart(divisible_by_three))
else:
    print("{} is not divisible by :".format(divisible_by_three))    
def divissible_by_three(n):
    new=[]
    for num in range (1,n):
        if(num%3==0):
            print(new)
            divissible_by_three(60)


y=[[1,2],[3,4],[5,6]]
flat_list=y[0]+y[1]+y[2]
print(flat_list)

smallest=[3,6,8,2,4,1,5,0,7]
# smallest.sort()
x=min(smallest)
print(x)



#A function that accepts list x below and uses a set to remove
x=["a","b","c","d","c","e","f","g","h"]
xx=list(set(x))
print(xx)

#Write a function named divisible by seven
divisible_by_seven=[]
for num in range(100,200):
    if (num%7==0):
        divisible_by_seven.append(num)
print(divisible_by_seven)

amount=5000
balance=3200
name="angela"
print(f"{name} your balance is{balance} and the amount withdrawn is {amount}")
print(name, "your current balance is",balance)
print("{} your balance is {}".format(name,balance))
student=[{"age":19,"name":"Eunice"},{"age":21,"name":"Agnes"},{"age":18,"name":"Teresa"},{"age":22,"name":"Asha"}]

def divissible_by_three(n):
    new=[]
    for num in range (1,n):
        if(num%3==0):
            new.append(num)
    print(new)
divissible_by_three(90)
