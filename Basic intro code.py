print("Hello World")
name="Karina" 
age= 21
price =2211.12
print(type (name))
print(type (age))
print(type (price))
name1= 'K'
name2="KARINA"
name3='''Kareena'''
print(name1)
print(name2)
print(name3)
old=False
a=None
print(type(old))
print(type(a))

a=2
b=5
sum=a+b
print(sum)

c=500
d=800
diff=d-c
print(diff)

first = int(input("enter first:"))
second = int(input("enter second:"))
print("sum=", first + second)

side= float(input("enter square side:"))
print("area=", side**2)

# Wap to input 2 floating point numbers & print their average.
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
print("Average of two float numbers=",(a+b)/2)

# Wap to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.
a =int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
print(a >= b)

# radain into degree.
π= 22/7
radian= float(input("Input radians:"))
degree= radian*(180/π)
print("degree=",degree)

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=a+b
print("Addition=",c)

#wap to calculate area of rectangle, perimeter of rectangle, area of square, perimeter of square, area of circle, circumference of circle
#area of rectangle
Side1=5
Side2=6
print("Area of rectangle=", Side1*Side2)

#area of rectangle
Length=10
Width=10
Area= Length*Width
print("Area of rectangele=", Area)

#area and perimeter of rectangle
Length= int(input("Enter length of rectangle:"))
Breadth= int(input("Enter breadth of rectangle:"))
Area= Length*Breadth
Perimeter= Length*2 + Breadth*2
print("Area of rectangele=", Area)
print("Perimeter of rectangle=", Perimeter)

#area and perimeter of square
Side=int(input("Enter side of square:"))
Area= Side*Side
Perimeter= Side*4
print("Area of square=", Area)
print("Perimeter of square=", Perimeter)


#area of circle
r=int(input("Enter the radius of circle:"))
π=3.14
Area= π*(r**2)
Circumference= 2*π*r
print("Area of circle=", Area)
print("Circumference of circle=", Circumference)


#wap to accept electricity unit consumption and calculate total price at the rate  of 5rs per  unit and give 10% discount on total bill;
units_consumed=int(input("Enter the number of electricity units consumed:"))
total_price=units_consumed*5 
discount=10 
total_afterdiscount=total_price - (total_price*discount/100)
print("bill amount before discount=",total_price) 
print("Final bill amount after discount=",total_afterdiscount) 

#Identity operator
x=5
if("type (x) is int"):
    print("correct")
else:
    print("incorrect")
    
y=6.66
if("type (y) is not int"):
    print("True")
else:
    print("False")
y=6.66
if ("type(y)is not float"):
    print("True")
else:
    print("False")

y=6
if("type(y)is float"):
    print("True")
else:
    print("False")
a=10
list=[1,2,3,4,5,6]
if(a in list):
    print("Yes a is present in the list.")
else:
    print("No a is not present in the list")
b=4
list=[1,2,3,4,5,6,7]
if(b in list):
    print("Yes b is present in the list")
else:
    print("No b is not present in the list")


#pyramid of stars
rows = int(input("Enter number of rows: "))

for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(" ", end="")
    for j in range(0,i + 1):
         print("* ", end="")
    print()


#If and else conditions:
# Wap to find max between two numbers?
a= int(input("Enter 1st number:"))
b= int(input("Enter 2nd number:"))
if a>b:
    print("Max Number=",a)
else:
    print("Max Number=", b)

#Wap a program to find max between three numbers?
a= int(input("Enter 1st number:"))
b= int(input("Enter 2nd number:"))
c= int(input("Enter 3rd number:"))
if a>b and a>c:
   print("Max number =:", a)
elif b>a and b>c:
   print("Max number =:",b)
else:
    print("Max number =:",c)

# Wap to check a given number is positive, negative, or zero.
a= int(input("Enter 1st number:"))
if a>0:
   print("The number is positive.")
elif a<0:
   print("The number is negative.")
else:
    print("Zero")


a= int(input("Enter 1st number:"))
b= int(input("Enter 2nd number:"))
c= int(input("Enter 3rd number:"))
if (a>b and a<c) or(a<b and a>c):
   print("Middle number=", a)
elif (b>a and b<c) or (b<a and b>c):
    print("Middle number=", b)
else:
    print("Middle numbet=", c)

#Wap to calculate total marks in 5 subjects (Full marks per subject= 100) as well as percentage of marrks and division as per the following condition:
#percentage>=80-Grade A,  percentage>=60-Grade B, percentage>=40-Grade C, percentage
#    #Solution:
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
d = int(input("Enter 4rth number:"))
e = int(input("Enter 5th number:"))
Obtained = a+b+c+d+e
total = 500
percentage = (Obtained/total)*100
print("Obtained marks=",Obtained,"Percentage=",percentage) 
if percentage>=80:
    print("You have got grade A.") 
elif percentage>=60:
    print("You have got grade B.") 
elif percentage>=40:
    print("You have got grade c.") 
else:
    print("You have got grade c.")

#Wap to accept marks of 5 subjects and find total marks and percentage assuming full marks as 100 in each subject;
#percentage calculator;
print("Percentage calculator=")
num1=int(input("Enter your marks in Hindi:"))
num2=int(input("Enter your marks in English:"))
num3=int(input("Enter your marks in Maths:"))
num4=int(input("Enter your marks in Physics:"))
num5=int(input("Enter your marks in Chemistry:"))
total=num1+num2+num3+num4+num5
print(" Total marks=",total)
per=total/500
per1=per*100
print("percentage =",per1,"%")

#Wap to accept total sales amount and find the profit amount @ 5%.
Sales=int(input("Enter amount of Sales:"))
profit_5percent_sale= Sales*(5/100)
print("Profit at 5 % of Sales=",profit_5percent_sale)

a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
print("Before swap a=",a)
print("Before swap b=",b)
c=a
a=b
b=c
print("After swap a=",a)
print("After swap b=",b)

#Exit the loop when i is 3:
i = 1 
while i < 6:
  print(i)
  if i == 3:
    break 
  i += 1

count = 0 
while (count < 16):
    count = count+1
    print ("Hello Geek") 

i = 0 
while i < 8:
  i += 1
  if i == 3:
     continue
  print(i)

#print as long as i is less than 6
i = 1
while i < 7:
  print(i)
  i +=1













