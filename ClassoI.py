print ("Hello All, Welcome to python programing")

a=10
b=20
c= a+b

print (c)

print ("Arithmatic Operations")

a= 10
b= 20

print ( a + b )
print ( a - b )
print ( a * b )
print ( a % b )
print ( a ** b )
print ( a // b )

print ("Assignment operations")

a = 30
b = 30

a=b

print (a)

a+=b
print (a)

a-=b
print(a)

a+=b
print (a)

a*=b
print(a)

a/=b
print(a)

a**=b
print(a)

print ("Condition Operations")

a=10
b=50

print (a==b)
print (a!=b)
print (a>b)
print (a<b)
print (a>=b)
print (a<=b)

print ("Logical Operations")

a=10
b=50

print (a and b)
print (a or b)
print (not a)

print ("Identity Operations")

a = [1, 3, 5, 7, 'Python']
a=b
print( b is a )
print (a is not b)

print ("Bitwise operations")

a=10
b=35
print(a&b)
print(a|b)
print(a^b)
print(-a)
print(a<<2)
print(a>>b)

print("Dictionaries")

print ("For Boolean")

number = [1,2,3,4,5]
boolean = 3 in number
print (boolean)
print("Numbers")
num1=5*3
num2=32//3
num3=32/3
print ("num1 is", num1)
print ("num2 is", num2)
print ("num3 is", num3)
print ("for string data type")
str1="Welcome "
str2="to python programming"
str3= str1 + str2
print("The string is", str3)
print(str3[0:10])
print(str3[-5:])
print(str3[:-5])
print("for list data structure")
countries=["Australia","China","Japan","USA","Canada"]
states=["Montreal","Toronto","Newyork"]
for st in states:
    print(st)
#print(countries)
countries.append("Russia")
countries.insert(2, "Brazil")
value=len(countries)
print(value)
countries.append(st)
countries.remove("Russia")
for count in countries:
    print(count)

print("Tuple data structure")
sports_score = ("cricket", 125, "basketball", 15, "football", 5)
print(sports_score)
print(type(sports_score))
for ss in sports_score:
    print(ss)
print(type(sports_score))
sport_list = list (sports_score) #converting tuple to list
sport_list.append("Baseball") #Updating list
for sl in sport_list:
    print (sl)
print(type(sport_list))
student=[{
    "name":"david",
    "student id":541254,
    "Course":"Python",
    "Address":"Toronto"
},{
    "name":"Mirella",
    "student id":1010586,
    "Course":"Python",
    "Address":"Montreal"
}
]
print("Details of student are:",student)
