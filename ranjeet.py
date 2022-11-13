#print ('hello')

'''x = 10
y = 45
print(x+y)'''

#x = 89
#print(complex(x))

'''a = 0

while a < 20:
	print('a')
	a+=1'''

'''a = 10
while a > 0:
	print(a)
	a-=1'''
'''a = int(input('Enter any number: '))
while a < 20:
	print(a)
	a+=1'''

'''a = int(input('Enter any number: '))
while a > 0:
	print(a)
	a-=1'''
'''Break statement
o = int(input('Enter any number: '))
m = int(input('Which number want to print: '))
while o < m:
	print(o)
	if o == 12:
		break
	o += 1'''

'''o = int(input('Enter any number: '))
m = int(input('Which number want to print: '))
while o < m:
	o += 1
	if o == 12:
		continue
	print(o)'''
#Print a table with the help of user input. use while loop
#Print alist with the help of while loop.

'''a = 0
while a < 20:
	print(a)
	a+=1
else:
	print('Completed')'''

'''t = int(input('Enter any number: '))
n = 1
while n < 11:
	print(t*n)
	n=n+1'''

'''days = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
for i in days:
	print(days)'''

'''counting = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
for i in counting:
	print(i)'''

'''state = 'UTTAR PRADESH'
for i in state:
	print(state)'''

#Print a list using continue
'''days = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
for i in days:
	if i == 'Tue':
		continue
	print(i)'''

#Print a list using break
'''days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
for i in days:
	if i == 'Wed':
		break
	print(i)'''

#use of range
'''for a in range(1, 26):
	print(a)'''

#range function using step
'''for a in range(1, 26, 2):
	print(a)'''

'''for a in range(1, 16):
	print(a)
else:
	print('Completed')'''

#nested loop function
'''days = ['O', 'M', 'K', 'A', 'R']
months = ['K', 'A', 'U', 'S', 'H', 'I', 'K']
for a in days:
	for b in months:
		print(a,b)'''


'''days = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
a = 0
while a < len(days):
	print(days[a])
	a+=1'''

'''days = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
a = 0
while a < 7:
	print(days[a])
	a+=1'''

#dic with for loops
#keys
'''o = {'name' : 'omkar', 'add': 'india', 'age': 24, 'YOB' : 1998 }
for i in o.keys():
	print(i)'''

#vlues
'''o = {'name' : 'omkar', 'add': 'india', 'age': 24, 'YOB' : 1998 }
for d in o.values():
	print(d)'''

#items
'''o = {'name' : 'omkar', 'add': 'india', 'age': 24, 'YOB' : 1998 }
for d,i in o.items():
	print(d,i)'''

#Print table of 5.
'''y = 5
z = 1
while z < 11:
	print(y*z)
	z=z+1'''

#Print a table of user's choice.
'''a = int(input('Enter any number: '))
b = 1
while b < 11:
	print(a*b)
	b=b+1'''

''' Calculate simple interest                    (Need to ask)
pa = int(input('Enter the Principal amount: '))
r = int(input('Enter the rate: '))
t = int(input('Enter the time: '))
z = pa(1+(r*t))
print(z)'''

'''a = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
print(a)'''

#List
'''d = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
print(d)'''

#List check len
'''d = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
print(len(d))'''

#List check type
'''d = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
print(type(d))'''

'''d = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat',1,2,3,True,False,]
print(len(d))'''

'''d = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat',1,2,3,True,False, 'Sun', 'Mon', 'Tue']
print(d)'''

#constructors of type
'''a = set(('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'))
print(a)'''

#List items are indexed and you can access them by referring to the index number. (Positive & Negative Indexing)
'''d = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
print(d[-1])'''

'''d = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
print(d[1:7:3])'''

#Return the 2nd, 3rd, 4th.
'''x = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(x[-5:-2])'''

#Append
'''d = ['Sun', 'Mon', 'Tue', 'Wed']
d.append('Thurs')
print(d)'''

#Insert
'''d = ['Sun', 'Mon', 'Tue', 'Wed']
d.insert(0,'Thurs')
print(d)'''

#Extend
'''d = ['Sun', 'Mon', 'Tue', 'Wed']
e = [1,2,3,4]
f = [True,False]
d.extend(e+f)


z = [5,6,7]
d.extend(z)
print(d) '''

#Remove method
'''d = ['Sun', 'Mon', 'Tue', 'Wed']
d.remove('Mon')
print(d)'''


#Pop method
'''d = ['Sun', 'Mon', 'Tue', 'Wed']
d.pop(0)
print(d)
'''
#Del method
'''d = ['Sun', 'Mon', 'Tue', 'Wed']
del d[0]
print(d)'''

#Clear method
'''d = ['Sun', 'Mon', 'Tue', 'Wed']
d.clear()
print(d)'''

'''d = ['Sun', 'Mon', 'Tue', 'Wed']
e = [1,2,3,4]
print(d+e)'''


#Nested list
'''x = [1,2,['sun', 'mon',['apple', 'banana'],'tues'],5,6]
x[2][2][0]='mango'
print(x)'''

#append method in nested list
'''x = [1,2,['sun', 'mon',['apple', 'banana'],'tues'],5,6]
x[2][2].append('mango')
print(x)'''

#insert method in nested list
'''x = [1,2,['sun', 'mon',['apple', 'banana'],'tues'],5,6]
x[2].insert(4,'wed')
print(x)'''

#extend method in nested list
'''x = [1,2,['sun', 'mon',['apple', 'banana'],'tues'],5,6]
x[2][2].extend(['mango'])
print(x)
'''
#need to do remove, pop, del


#use of reverse
'''a = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
a.reverse()
print(a)'''

#use of sort (Ascending)
'''a = ['c', 'e', 'a', 'f', 'b', 'd', 'h', 'g', 'i']
a.sort()
print(a)'''

#use of reverse=true (Descending)
'''a = [45,23,12,1,0,89,65,76]
a.sort(reverse=True)
print(a)'''

#use of index
'''a = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
b = a.index('monday')
print(b)'''

#use of index in nested list
'''a = [1,2,['sun', 'mon',['apple', 'banana'],'tues'],5,6]
b = a[3][2].index('banana')
print(b)'''

#Replace the element in list without any method
'''a = ['sunday', 'monday', 'wednesday', 'wednesday']
a[2] = 'tuesday'
print(a)
'''
#Replace the multiple elements in the list 
'''a = ['sun', 'mon', 'wednesday', 'wednesday']
a[:3] = ['sunday', 'monday', 'tuesday']
print(a)'''

#print days name using for loop
'''a = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
for b in a:
	print(b)'''

#for check len using for loop
'''a = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
for b in range(len(a)):
	print(b)'''


'''a = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
for b in range(len(a)):
	print(a[b])'''

#use of while loop to print days
'''a = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
b = 0
while b < (len(a)):
	print(a[b])
	b+=1'''

#Dictionary
'''a = {
'Name' : 'Ranjeet', 
'S. Name' : 'Chauhan', 
'Add' : 'India', 
'Age' : 6, 
'Language' : 'Aligarhiya', 
'Class' : 'UKG', 
'Gender' : 'Male',
'Status' : 'True'}
print(a)'''



#Set
#unordered, duplicates are not allowed, unchangable
#but we can add and remove the eliments

'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'friday'}
print(x)
#print(type(x))
#print(len(x))'''

#Boolean data type are not accepted
'''x = {'sunday', 'monday', 'tuesday', 1,2,3,4,True,False}
print(x)'''

#Set constructor: It's use for type casting
'''a = set(('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'friday'))
print(a)'''


#Use of for loop in set
'''a = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'}
for i in a:
	print(i)'''

#Use of IF condition with "in" or "not in" operator in set.   (Membership operator)
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'}
#if 'sunday' in x:
if 'sunday' not in x:
	print('yes, its there')
else:	
	print('No, its not there')'''

#To add any element using "add method" in set.
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
x.add('saturday')
print(x)'''


#To update any element/list/tuple using "update method" in set.
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
#y = {'Jan','Feb'} #set to set
#y = ['Jan','Feb'] # list to set
y = ('Jan','Feb') # tuple to set
x.update(y)
print(x)'''

# To remove any element using of "remove/discard" method in set. 
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
#x.remove('sunday')   # if element doesn't exist it shows an error. 
x.discard('tuesday') # it doesn't show error weather element exist or not exist.
print(x)'''

#The pop method uses for delete the last element.
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
y = x.pop()
print(y)
print(x)'''

#use of clear method.
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
x.clear()
print(x)'''


#use of del keyword
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
del x
print(x)'''

#The union method uses for add one or more sets/list/tuple/dict(only keys) in single set.
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
y = {'Jan','Feb','Mar'}
w = {1,2,3,4}
t = ['Tejasvi','Sharma']
d = {'name':'omkar' , 'sr name':'kaushik'}
#z = x.union(y)
z = x.union(y,w,t,d)
print(z)'''

#The "intersection_update()" method shows duplicate elements in a single or multiple set/list/tuple/dic. (if not found common elements it shows a blank set() ). 
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
y = {'sunday', 'monday', 'tuesday', 'Jan', 'Feb', 'Mar'}
z = {'sunday', 'monday', 1,2,3,4}
d = ['sunday','tuesday' 'Omkar','kaushik']
c = {'sunday':'day', 'name':'omkar' , 'sr name':'kaushik'}
x.intersection_update(y,z,d,c)
print(x)'''

#To create a new set by using "intersection()" method. 
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'} 
y = {'sunday', 'monday', 'tuesday', 'Jan', 'Feb', 'Mar'}
z = x.intersection(y)
print(z)'''

# To create/update a new/main set by using "symmetric_difference()" method.
'''x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
y = {'sunday', 'monday', 'tuesday', 'Jan', 'Feb', 'Mar'}
#x.symmetric_difference_update(y) # To update the main set by using "symmetric_difference_update()" method.
z = x.symmetric_difference(y) # To create a new set by using "symmetric_difference()" method.
print(z)'''




#23-Apr-2022 Saturday

#Tuple: Tuples are allow duplicates, ordered, unchangeble

'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','sunday')
#print(t)
#print(type(t))
#print(len(t))'''

'''t = ('sunday','monday','tuesday',1,2,3,True,False) # All types of data are acceptable.
print(t)'''

'''t=('monday',) # If we create a tuple with single element 
print(type(t))'''

'''t = tuple(('sunday','monday','tuesday','wednesday'))
print(t)'''

#############
'''t = tuple('sunday','monday','tuesday','wednesday')
l = ['monday','tuesday','wednesday']
s = tuple(l)
print(s)'''


# Indexing
'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
 #print(t[2:9])  
 #print(t[-9]) #indexing from the last
 #print(t[0:6:2]) #alternative indexing''' 


'''# indexing with 'not in' and 'in' operator. (Membership operator). 
t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
#if 'sunday' in t:
if 'sunday' not in t:
	print('yes')
else:
	print('No')'''


# Replace an element in a tuple.

'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
s = list(t)
s[3] = "wednesday"
t=tuple(s)
print(t)'''

# Add an element in a tuple using append method.
'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
s = list(t)
s.append('july')
t = tuple(s)
print(t)'''

# Add another tuple in main tuple.
'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
s = ('august','september')
t += s
print(t)'''


# Remove an element in a tuple using remove method.
'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
s = list(t)
s.remove('june')
t = tuple(s)
print(t)'''

'''# Remove an element in a tuple using 'del' keyword.
t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
s = list(t)
del s[1]
t = tuple(s)
print(t)'''


# Unpacking tuple.
'''t = ('sunday','monday','tuesday')
s,w,x = t
print(s)
print(w)
print(x)'''


'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
(s,m,*w) = t
print(s)
print(m)
print(w)'''


# using 'for loop'
'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
for i in t:
	print(t)'''

# using for loop with 'range' function.
'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
for i in range(len(t)):
	print(t[i])'''

# using while loop
'''t = ('sunday','monday','tuesday','Jan','Feb','Mar','apr','may','june')
s = 0
while s < (len(t)):
	print(t[s])
	s+=1'''

'''# Join tuples.
t = ('sunday','monday','tuesday')
s = ('Jan','Feb','Mar','apr','may','june')
w = t+s
print(w)'''

'''# Multiply tuples
t = ('sunday','monday','tuesday')
w = t*3
print(w)'''

# Count elements in a tuple.
'''t = ('sunday','monday','tuesday','sunday','Feb','Mar','sunday','may','june')
s = t.count('sunday')
print(s)'''


# Check index of any element in a tuple.
'''t = ('sunday','monday','tuesday','sunday','Feb','Mar','sunday','may','june')
s = t.index('tuesday')
print(s)'''



##### 24-Apr-2022
# Dictionary

# To find values in the dict
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
#y = x['age'] # without method
y = x.get('name')  # with .get() method
print(y)'''



# To print keys and values in the dict.
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
#y = x.keys()  # Print keys with .key() method
y = x.values()  # Print values with .values() method
print(y)'''

# To add key and values in a dict.
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
x['job'] = 'noida'
print(x)'''

# update() menthod.
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
x.update({'birth place':'Bareilly'})
print(x)'''

# pop() method.
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
#x.pop('name')    # desired item will be deleted. 
x.popitem()       # It removes the last items. 
print(x)'''

# del keyword
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
#del x['name']  # desired item will be deleted. 
del x     # it will delete the whole dictionary. 
print(x)'''


# clear() method
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
x.clear()
print(x)'''

# loops through dictionary

# Print all keys name in the dictionary, one by one. (without method)
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
for i in x:
    print(i)'''


# Print all values name in the dictionary, one by one. (without method)
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
for i in x:
    print(x[i])'''

# Print all values name in the dictionary, one by one. (with method)
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
for i in x.values():
    print(i)'''
    

# Print all keys name in the dictionary, one by one. (with method)
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
for i in x.keys():
    print(i)'''

# Print all keys and values name in the dictionary with method x.items() method)
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
for i, y in x.items():
    print(i,y)'''


# Make a copy of a dictionary with a copy() method
'''x = {'name':'ranjeet','age':25,'address':'Delhi','qualification':'BCA'}
# y = x.copy()
y = dict(x)
print(y)'''

# Nested Dictionaries. 

# Assignment
'''a = {'emp name':'omkar','emp code':1021,'emp salary':85000,'emp dept':'data management'}
#a.popitem()                # last item removed. 
#a.update({'emp age':'23'})
#del a['emp salary']
print(i)'''

# Nested dictionary.

# To add multiple dict in a signle dict. 
'''emp details = {'emp 1':{'emp name':'omkar','emp code':1021,'emp salary':185000,'emp dept':'data management'},
'emp 2':{'emp name':'ranjeet','emp code':1022,'emp salary':150000,'emp dept':'computer science'},
'emp 3':{'emp name':'deepak','emp code':1023,'emp salary':80000,'emp dept':'digital marketing'}}
print(a)'''


# To add multiple dict in a signle dict. 
'''emp_1 = {'emp name':'omkar','emp code':1021,'emp salary':185000,'emp dept':'data management'}
emp_2 = {'emp name':'ranjeet','emp code':1022,'emp salary':150000,'emp dept':'computer science'}
emp_3 = {'emp name':'deepak','emp code':1023,'emp salary':80000,'emp dept':'digital marketing'}

emp_final_details = {
    'emp_1':emp_1,
    'emp_2':emp_2,
    'emp_3':emp_3}
print(emp_final_details)'''


# Print a dict with duplicate items. 
'''emp_1 = {'emp name':'omkar','emp code':1021,'emp salary':185000,'emp dept':'data management','emp code':1021}
print(emp_1)'''

# print a dict without copy method.
'''a = {'emp name':'omkar','emp code':1021,'emp salary':185000,'emp dept':'data management','emp age':23}
b = dict(a)'''

'''# To search  value by giving key name.
a = {'emp name':'omkar','emp code':1021,'emp salary':185000,'emp dept':'data management','emp age':23}
b = a['emp salary']     # without method
print(b)'''


#### Functions
#There are two types of functions:

#Built in Function

'''def x():
	print('Hello')
x()'''

# Multiply

'''def mul(a,b):
	print(a*b)
mul(3,4)'''


'''# Sum
def sum(a,b):
	print(a+b)
sum(9,11)'''

'''# Subtract
def sub(a,b):
	print(a-b)
sub(15,11)'''

'''# exponentiation
def sub(a,b):
	print(a**b)
sub(2,4)'''


'''def sum(a,b):
	print(a+b)

def sub(c,d):
	print(c-d)

def exp(e,f):
	print(e**f)

def mul(g,h):
	print(g**h)

sum(15,11)
sub(15,11)
exp(4,4)
mul(5,4)
sub(20,12)
exp(3,6)
mul(10,3)'''


'''def calculation():
	x = int(input('Enter the first number: '))
	y = int(input('Enter the second number: '))
	print(x*y)
	print(x+y)
	print(x/y)
	print(x-y)
	print(x%y)
	print(x//y)
calculation()'''


'''def fd(a,b):
	print(a//b)

def exp(c,d):
	print(c**d)

def mod(e,f):
	print(e%f)

fd(3,5)
exp(4,4)
fd(4,2)
exp(2,4)
mod(5,4)
fd(5,6)
fd(4,8)'''


# Arbitrary Arguments: *args
'''If you don't know how many Arguments that will be passed in to your function, add an astrisk* before the parameter name in the function definition. 
 This way the function wil recieve a tuple of arguments and can access the items accordingly index.''' 

'''def x(*names):
	print('I am good' + names[0])
	print('Hello wrold' + ' '+ names[3])
	print('Good morning' + ' '+ names[5])
	print('I am indian officer' + ' '+ names[2])
	print('I am an army officer' + ' '+ names[4])
x('ABC','XYZ','IBM','GOOGLE','REF','INDIAN')'''

'''def x(Name,Age,Class):
	print('My name is' +' ' + Name)
	print('My class is ' + Class)
	print('My age is ' + Age)
x(Name = 'Ranjeet', Age = '26', Class = 'MBA')'''

#Arbitrary keyword Arguments, **a
# If you don't know how many keywords arguments 

'''def x(**a):
	print('My name is' +' ' + a['Name'])
	print('My class is ' , a['Class'])
	print('My age is ' , a['Age'])
x(Name = 'Ranjeet', Age = '26', Class = 'MBA')'''


# Assignment:
# 1. Create a function to print a list using while loop. 
'''def days():
	a = ['sun','mon','tue','wed','thurs','fri','sat']
	b = 0
	while b < 7:
		print(a[b])
		b+=1
days()'''


# 3. Create two function print a table any random number with the help of user input 
# and in second funtion do type casting, print a tuple with the 5 elements 
# and add tow elements in this tuple. Call these functions in the suffling way.


'''def table():
	a = int(input('Enter any number: '))
	b = 1
	while b < 11:
		print(a,'x',b,'=',a*b)
		b=b+1

def tup():
	a = ('sunday','monday','tuesday','wednesday','thursday')
	b = set(a)
	c = {'friday','saturday'}
	d = b.union(c)
	print(d)
tup()
table()
tup()
table()'''


# Default Parameter
'''def x(city = 'Delhi'):
	print('I am from' , city)
x('Lucknow')
x()
x('Mumbai')
x('Agra')
x('Bareilly')
x()'''



# The 'pass' Statement
# Function cannot be empty but if you want for some reason have a function definition with no content, put in the pass statement to avoid a getting error.  
'''def x():
	pass'''

# The 'return' values

'''def a():
	return 5 * x

(a(3))
print(a(5))
print(a(9))'''

'''x = lambda a : a + 10
print(x(5))'''

'''x = lambda a , b : a * b
print(x(5,6))'''

'''x = lambda a, b, c : a + b - c
print(x(5,6,3))'''

'''x = lambda a, b, c, d, e : a + b - c / d ** e
print(x(5,6,2,4,2))'''



## 7th May 2022    'Saturday'

'''Create three function and print a statement in first function do multiplication in second function and find modulas in third function.''' 

'''def a():
	print('Hello world')

def b(c,d):
	print(c*d)
def e(f,g):
	print(f%g)

a()
b(4,5)
e(4,2)'''


###  OOPS (Object orineted programming statement) Concept
## 8 May 2022

# Example: 1
'''class x:
	a = 15
b = x()
print(b.a)'''


# Example: 2
'''class x:
	a = 3
	b = 4
	z = a*b
mul = x()
print (mul.z)'''

# Example: 3
'''class x:
	def c (self,a,b):
		self.a=a
		self.b=b
		self.z=a+b

x1=x()
x1.c(5,15)
print(x1.z)'''


# Example: 4

'''class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

p1 = Person('Ranjeet',26)

print(p1.name)
print(p1.age)'''


# Example: 5
'''class add:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.c = a+b
z = add(10,15) 
print(z.c)'''

# Example: 6
'''class mul:
	def __init__(math,a,b):
		math.a = a
		math.b = b
		math.c = a*b
z = mul(5,10) 
print(z.c)
'''

# Example: 7

'''class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def x(self):
		print('My name is ' + self.name)

p1 = Person('Ranjeet',26)
p1.x()
print(p1.name)
print(p1.age)'''


# Example: 8
'''class Person:
	def x(self):
		print('My name is ' + self.name)
	def __init__(self,name,age):
		self.name = name
		self.age = age

p1 = Person('Ranjeet',26)
print(p1.name)
print(p1.age)
p1.x()'''



# Example: 9

'''class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def x(self):
		print('My name is ' + self.name)

p1 = Person('Ranjeet',26)
p1.age = 25
print(p1.name)
print(p1.age)'''


# Example 10:

'''class Person:
	def __init__(self,name,age,salary):
		self.name = name
		self.age = age
		self.salary = salary
	def x(self):
		print('My name is ' + self.name)
		print('My age is ' , self.age)

	p1 = Person('Ranjeet',26,500000)
p1.age = 25
print(p1.name)
print(p1.age)
print(p1.salary)
p1.x()'''


# Example: 11
'''class Person:
	def __init__(self,name,age,salary):
		self.name = name
		self.age = age
		self.salary = salary
	def x(self):
		print('My name is ' + self.name)
		print('My age is ' , self.age)

p1 = Person('Ranjeet',26,500000)
del p1.age
print(p1.name)
#print(p1.age)
print(p1.salary)
#p1.x()'''

# Example 12:

# The pass statement
'''class Person:
	pass'''

# Assignment:

'''Create a class and make three methods in this class in first method do exponent, in second method print any statement and 
in third method find the modulas. take different argument for all methods, and use __init__() function in this class.'''  


'''class test:
	def __init__(self,a,b,e,f):
		self.a = a
		self.b = b
		self.c = a**b
		self.e = e
		self.f = f
		self.g = e%f
	def x(self):
		print('My name is Ranjeet.')
	def z(self):
		print(self.g)
d = test(2,4,10,10)
print(d.c)
d.x()
d.z()'''

#Assignment:

'''class test:
	def __init__(self):
		a = int(input('Please enter any number: '))
		b = int(input('Please enter any number: '))
		self.a = a 
		self.b = b 
		self.c = a**b
	def x(self):
		print('You are correct.')
d = test()
print(d.c)
d.x()'''


#  Inheritence in Python

# Example: 1
'''class parent():
	def first(self):
		print('Good Morning')
class child(parent):
	def second(self):
		print('Good Night')
ob = child()
ob.first()
ob.second()'''


# Example: 2

'''class mobile():
	def __init__(self,brand,model,ram,rom):
		self.brand = brand
		self.model = model
		self.ram = ram
		self.rom = rom
	def Q (self):
		return('I have a Mobile.')
class laptop(mobile):
	def __init__(self,brand,model,ram,rom,colour):
		super(). __init__(brand,model,ram,rom)
		self.colour = colour
z = laptop('Apple','Iphone 13','12GB','256 GB','Green')
print(z.Q())
print(z.brand)
print(z.model)
print(z.ram)
print(z.rom)
print(z.colour)'''

'''Create two classes first parent class and second child class and do single level inheritance, 
use __init()__ and super(). function. create two method in first class and create one method in second class.'''


'''class emp1():
	def __init__(self,name,company,department,designation,salary):
		self.name = name
		self.company = company
		self.department = department
		self.designation = designation
		self.salary = salary
	def Q (self):
		return('I am working in IBM.')
class emp2(emp1):
	def __init__(self,name,company,department,designation,salary,location):
		super(). __init__(name,company,department,designation,salary)
		self.location = location
z = emp2('Omkar','IBM','Research and development','Data Analyst','50,000','Noida')
print(z.Q())
print(z.name)
print(z.company)
print(z.department)
print(z.designation)
print(z.salary)
print(z.location)'''



### 14-May-2022

# Multilevel Inheritance


'''Question: 1
Create a program and make three classes in this program, in first class make two methods, 
in first method do any calculation and in second method print any statement. In second 
and third class do one methods in each class and perform any calculation. use multilevel 
inheritance and use '__init__'  constructor and super function as per your requirment.'''


'''class Tree:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.c = a+b
	def x (self):
		return('You are correct.')
class Fruit_1(Tree):
	def __init__(self,a,b,d,e):
		super(). __init__(a,b)
		self.d = d
		self.e = e
		self.f = d*e
class Fruit_2(Fruit_1):
	def __init__(self,a,b,d,e,g,h):
		super(). __init__(a,b,d,e)
		self.g = g
		self.h = h
		self.i = g**h
z = Fruit_2(5,6,7,4,5,8)
print(z.c)
print(z.x())
print(z.f)
print(z.i)'''



#### Program: 2

'''class Tree:

	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.c = a+b
	def x (self):
		return('You are correct.')
class Fruit_1(Tree):
	def __init__(self,d,e):
		self.d = d
		self.e = e
		self.f = d*e
class Fruit_2(Fruit_1):
	def __init__(self,a,b,d,e,g,h):
		Tree. __init__(self,a,b)
		Fruit_1. __init__(self,d,e)
		self.g = g
		self.h = h
		self.i = g**h
z = Fruit_2(5,6,7,4,5,8)
print(z.x())
print(z.c)
print(z.f)
print(z.i)'''


####  Multiple Inheritance

# Program: 1

'''class Parent_1:
	def x1(self):
		print('Good Morning.')
class Parent_2:
	def x2(self):
		print('Good Afternoon.')
class Child(Parent_1,Parent_2):
	def x3(self):
		print('Good Evening.')
z = Child()
z.x1()
z.x2()
z.x3()'''

# Program: 2

# Create a multiple inheritance, and make two methods in base class, and one methods another two class. Do any calculation.

'''class Base:
	def m1(self,a,b):
		self.a = a
		self.b = b
		self.c = a+b
		print(self.c)
	def m2(self):
		print('You are correct.')
class Parent(Base):
	def m3(self,d,e):
		self.d = d
		self.e = e
		self.f = d*e
		print(self.f)
class Child(Base,Parent):
	def m4(self,g,h):
		self.g = g
		self.h = h
		self.i = g**h
		print(self.i)	
z = Child()
z.m1(2,4)
z.m2()
z.m3(4,6)
z.m4(5,8)'''


## 15th May 2022

########################## Question: 1
################    Incomplete
'''Create a program and do multiple inheritance in this program and find the multiply in first class, 
return a list and iterate it with the while loop, and in third program find the factorial of any random 
number, use _init_ constructor and super function in this program.''' 


'''class First_class:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.c = a*b
class Second_class:	
	def x (self):
		month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
		a = 0 
		while a < 7:
			print(month[a])
			a+=1
class Third_class(First_class,Second_class):
	def fact(self,a,b,n):
		super(). __init__()
		n = int(input('Please enter any number.'))	
		if n == 0:
			return 1 
		else:
			return n*fact(n-1)	
			print(fact(n))		
z = Third_class(2,3)
print(z.c)
z.x()'''



### 21st May 2022


# Program: 1
 
'''Create a program with the help of multilevel inheritance and make three classes, in first class make two method and in 
first method do any calculation and in second method print any statement in second class create two methods and do 
calculation as you want, and in third class make two methods in frist a table of any random number and in seocond method 
print any statement you can use __init__ constructor and super function in this program.'''



'''class First_Class:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.c = a*b
	def x1(self):
		return('You are awesome.')
class Second_Class(First_Class):
	def __init__(self,a,b,d,e):
		super().__init__(a,b)
		self.d = d
		self.e = e
		self.f = d+e
	def x2(self,g,h):
		self.g = g
		self.h = h
		self.i = g+h
class Third_Class(Second_Class):
	def __init__(self,a,b,d,e):
		super().__init__(a,b,d,e)
		m = int(input('Enter any number: '))
		n = 1
		while n < 11:
			print(m,'x',n,'=',m*n)
			n=n+1`
	def x3(self):
		return('Your program completed.')
z = Third_Class(2,3,10,20)
print(z.c)
print(z.x1())
print(z.f)
z.x2(5,10)
print(z.i)
print(z.x3())'''




##  Program: 2

'''Create a program with the help of multilevel inheritance and make three classes, in first class make two method and in 
first method do any calculation and in second method print any statement in second class create two methods and do 
calculation as you want, and in third class make two methods in frist a table of any random number and in seocond method 
print any statement you can use __init__ constructor and super function in this program.''' 

'''class First_Class:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.c = a*b
	def x1(self):
		return('You are awesome.')
class Second_Class(First_Class):
	def __init__(self,a,b,d,e):
		self.d = d
		self.e = e
		self.f = d+e
	def x2(self,g,h):
		self.g = g
		self.h = h
		self.i = g+h
class Third_Class(Second_Class):
	def __init__(self,a,b,d,e):
		First_Class.__init__(self,a,b)
		Second_Class.__init__(self,a,b,d,e)
		m = int(input('Enter any number: '))
		n = 1
		while n < 11:
			print(m,'x',n,'=',m*n)
			n=n+1
	def x3(self):
		return('Your program completed.')
z = Third_Class(2,3,10,20)
print(z.c)
print(z.x1())
print(z.f)
z.x2(5,10)
print(z.i)
print(z.x3())'''


###  Muliple Inheritance 

'''Create a program with the help of multiple inheritance, and make three classes in this program in all classes make two 
methods and perform any calculation as you want. use super(). function and __init__ constructor as you want.'''


'''class First_Class:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.c = a+b
	def x1(self,d,e):
		self.d = d
		self.e = e
		self.f = d-e
		return(self.f)
class Second_Class:
	def x4(self,g,h):
		self.g = g
		self.h = h
		self.i = g-h
		return(self.i)
	def x2(self,j,k):
		self.j = j
		self.k = k
		self.l = j**k
		return(self.l)
class Third_Class(First_Class,Second_Class):
	def __init__(self,a,b,m,n,g,h):
		super().__init__(a,b)
		super().x4(g,h)
		self.m = m
		self.n = n
		self.o = m%n
	def x3(self):
		return('Your program completed.')
z = Third_Class(10,15,1,100,2,2)
print(z.c)
print(z.x1(20,5))
print(z.x2(10,15))
#print(z.x4(5,10))
#print(z.i)
print(z.o)
print(z.x3())
'''

'''class First_Class:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.c = a+b
	def x1(self,d,e):
		self.d = d
		self.e = e
		self.f = d-e
		return(self.f)
class Second_Class:
	def __init__(self,g,h):
		self.g = g
		self.h = h
		self.i = g*h
	def x2(self,j,k):
		self.j = j
		self.k = k
		self.l = j**k
		return(self.l)
class Third_Class(First_Class,Second_Class):
	def __init__(self,a,b,g,h,m,n):
		First_Class.__init__(self,a,b)
		Second_Class.__init__(self,g,h)
		self.m = m
		self.n = n
		self.o = m%n
	def x3(self):
		return('Your program completed.')
z = Third_Class(10,15,5,10,20,10)
print(z.c)
print(z.x1(20,5))
print(z.i)
print(z.x2(10,15))
print(z.o)
print(z.x3())'''



# Python program to create a “Vehicle” class with max_speed and mileage instance attributes.

'''class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed+modelX.mileage)'''

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.

'''class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Car(Vehicle):
    pass

Personal_Car = Car("Grand i10", 250, 25)
print("Vehicle Name:", Personal_Car.name, "Speed:", Personal_Car.max_speed, "Mileage:", Personal_Car.mileage)'''



######    22th May 2022


## Polymorphism 

'''class Parrot:
	def fly(self):
		print("I can fly.")
	def swim(self):
		print("I cannot swim.")
class Penguin:
	def fly(self):
		print("I can't fly.")
	def swim(self):
		print("I can swim.")
def flying_test(self):
	self.fly()
	self.swim()

bird = Parrot()
peggy = Penguin()

flying_test(bird)
flying_test(peggy)'''


'''class A:
	def exp(self,a,b):
		self.a = a
		self.b = b
		self.c = a+b
	def st(self):
		print("You are awesome.")
class B:
	def exp(self):
		self.t = ('1','2','a','b')
		print(self.t)
	def st(self,x,y):
		self.x = x
		self.y = y
		self.z = x*y
		print("Addition",self.z)
class C:
	def sum(self,e,f):
		self.e = e
		self.f = f
		self.g = e+f
def madrid(self):
	self.exp(2,4)
	self.st(12,10)

x1 = A()
x2 = B()
x3 = C()
madrid(x1)
madrid(x2)
madrid(x3)

'''


### 28th May 2022

# Program 1:

'''from abc import ABC,abstractmethod
class employee(ABC):
	def emp_id(self,id,name,age,salary):
		pass

class employee1(employee):
	def emp_id(self,id):
		print('emp_id is 12345')

emp1 = employee1()
emp1.emp_id(id)'''


# Program 2:

'''from abc import ABC,abstractmethod
class employee(ABC):
	def emp_id(self,id,name,age,salary):
		pass
class employee1(employee):
	def x1(self,a,b):
		self.a = a 
		self.b = b
		self.c = a*b
		return(self.c)
class employee2(employee):
	def x2(self,d,e):
		self.d = d 
		self.e = e
		self.f = d+e
		return(self.f)
emp1 = employee1()
emp2 = employee2()
print(emp1.x1(2,4))
print(emp2.x2(5,6))'''


'''from abc import ABC,abstractmethod
class employee(ABC):
	def emp_id(self,id,name,age,salary):
		pass
class employee1(employee):
	def x1(self,a,b):
		self.a = a 
		self.b = b
		self.c = a*b
		return(self.c)
class employee2(employee):
	def x2(self,d,e):
		self.d = d 
		self.e = e
		self.f = d+e
		return(self.f)
class employee3(employee):
	def x3(self):
		g = int(input('Enter any number: '))
		h = 1
		while h < 11:
			print(g,'x',h,'=',g*h)
			h=h+1
emp1 = employee1()
emp2 = employee2()
emp3 = employee3()
print(emp1.x1(2,4))
print(emp2.x2(5,6))
print(emp3.x3())'''


'''from abc import ABC,abstractmethod
class employee(ABC):
	def emp_id(self,id,name,age,salary):
		pass
class employee1(employee):
	def x1(self,a,b):
		self.a = a 
		self.b = b
		self.c = a*b
		return(self.c)
class employee2(employee):
	def x2(self,d,e):
		self.d = d 
		self.e = e
		self.f = d+e
		return(self.f)
class employee3(employee):
	def x3(self):
		g = int(input('Enter any number: '))
		h = 1
		while h < 11:
			print(g,'x',h,'=',g*h)
			h=h+1
emp1 = employee1()
emp2 = employee2()
emp3 = employee3()
print(emp1.x1(2,4))
print(emp2.x2(5,6))
print(emp3.x3())'''





#######   Data Encapsulation ######


'''class Employee:
	def __init__(self,name,salary,project):
		self.name = name
		self.salary = salary
		self.project = project
	def show(self):
		print("Name: ",self.name,'salary',self.salary)
	def work(self):
		print(self.name,'is working on',self.project)

emp = Employee('Omkar',500000,'Data Science')

emp.show()
emp.work()'''


##  Assignment:

# Program 1:
'''Create three class with the help of abstractmethod, in second class create two functions, in first function create
a set and add two elements in this set, in second function print any statement, in third class first function find
the factorial of any random number, and in second method print any statement.'''

'''from abc import ABC,abstractmethod
class first_class(ABC):
	def x1(self):
		pass
class second_class(first_class):
	def x2(self):
		self.x = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday'}
		return(self.x)
	def x3(self):
		print("You are awesome.")
			
class third_class(first_class):
	def x5(self,fact):
		n = int(input('Enter any number: '))
		self.fact= fact
		if n == 1:
			return 1
		else:
			fact = n*fact
			n-=1
		#print('factorial of',n, 'is',fact)
		print(self.fact)
	def x4(self):
		print("Program Completed.")			
z1 = second_class()
z2 = third_class()
print(z1.x2())
print(z1.x3())
#print(z2.fact)
print(z2.x5(1))
'''

# Program:2

'''Create three classes and use polymorphism in these classes, in each class make two method, in first method print a list
with the help of for loop, and in second method print any statement, in second class do any calculation and in first
method and print any statement in second method as in third class.'''


'''class first():
	def A(self,l,k):
		a = ['mango', 'apple', 'banana', 2]
		for i in range(len(a)):
			print(a [i])

	def B(self):
		print('Good Morning')

class second():
	def A(self,b,c):
		self.b=b
		self.c=c
		self.d=b+c
	
	def B(self):
		print('Good Afternoon')

class third():
	def A(self,g,h):
		self.g=g
		self.h=h
		self.j=g+h
	
	def B(self):
		print('Good Night')

def om(self):
	self.A(4,5)
	self.B()
	

O1 = first()
O2 = second()
O3 = third()
om(O1)
om(O2)
print(O2.d)
om(O3)
print(O3.j)
'''



###################   Exception Handeling

'''When an error occurs '''

##  Program: 1
'''try:
	print(x)
except:
	print("x should be defind")'''




## Program :2

'''try:
	x = 4
	print(x)
except:
	print("x should be defind")
finally:
	print("Have a nice day!")'''



## Program: 3

'''x = 4
y = 0
z = x/y
print(z)'''



'''try:
	x = 4
	y = 0
	z = x/y
	print(z)
except ZeroDivisionError:
	print("Put right integer")
finally:
	print("Have a nice day!")'''


#  Program: 4

'''try:
	x = 3
	y = "Hello"
	z = x+y
	print(z)
except TypeError:
	print("Put right data type.")
finally:
	print("Have a nice day!")'''


# Program 5:

'''try:
		print("Honesty")
	except:
		print("Every thing is good.")
	else:
		print("Nothing is wrong.")'''	



'''Take a user input 
Create a program in try block, find voter is eligible for voting or not.'''

'''try:	
a = int(input('Enter your age: '))
	if a >= 18:
		print("You are eligible for voting.")
	else:
		print('You are not eligible for voting.')
except:
	print("Enter the correct age.")
finally:
	print("Have a nice day!")'''


 # Program to check the entered number is even or odd. 


'''try:	
	x = int(input("Enter any number: "))
	if x <= 0:
		print("Enter the positive number.")
	elif (x%2) == 0:
		print("Number is even.")
	else:
		print("Number is odd.")
except:
	print("Enter the positive number.")
finally:
	print("Have a great day!")'''


######################   04-June-2022   #########################

# Raise an execution

'''As a python developer you can choose to throw an exception if a condition occurs. 
 To thorw (or raise) an exception, use the raise keyword.''' 

# Example: Raise an error and stop the program if x is lower than 0. 

'''x = -1
if x<0:
	raise exception ("Sorry, no numbers excepted below zero.")'''



######%%%%%%%%%%%%%%######   File Handling   ######%%%%%%%%%%%%%%######

'''file = open("test_file.py","r")
 print(file.read())''' 




# 'rt' stands for read text
'''file = open("test_file.py","rt")
print(file.read())'''




'''file = open("test_file.py","w")
print(file.write("Have a nice day!"))'''




# To read no. of characters. 
'''file = open("test_file.py","r")
print(file.read(50))'''


# To read line by line. 
'''file = open("test_file.py","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())'''


'''file = open('test_file.py','r')
for i in file:
	print(i)'''


###########  5th June 2022  ############

#  Open the file 'h.py' and append (add) content to the file:

'''z = open("test_file.py","a")
z.write("\n\n I am a great person.")
z = open("test_file.py","r")
print(z.read())
z.close()'''




############ Write method example ############ 

'''z = open("test_file.py","w")
z.write("You are awesome.")
z = open("test_file.py","r")
print(z.read())
z.close()'''



'''z = open("test_file2.py","w")
z.write("Main tera hero.")
z = open("test_file2.py","r")
print(z.read())
z.close()'''



############ Create method example ############

'''To create a new file in python, use the open() method, with one of the following program:  
 
  'x' - Create - will create a file, returns an error if the file exist.''' 

'''z = open("test_file3.py","x")
z = open("test_file3.py","w")
z.write("apple is good for health.")
z = open("test_file3.py","r")
print(z.read())'''


############ Python delete file ############

'''To delete a file, you must import the OS module, and run its os.remove() function:

Example
Remove the file "test_file.py"'''
 

'''import os
os.remove('test_file2.py')'''



############ To delete any folder ############

'''To delete an entire folder, use the 'os.rmdir()' method. 

Remove the folder "myfolder"'''

'''import os
os.rmdir("test_folder")'''


# Note: You can only remove the empty folders 




############    Some Important Commands    ############

#   cd stands for change directory

#   cd..     come back on c one by one. 

#   cd/..    we can come on direct c prompt.c

#   pushd drive_name:    we can change the drive. 

#   pushd D:

#   popd      we can come back on previous drive. 



###########   Assignment    ###########

'''Question: 1 
First print a msg in a file with the help of append "a", msg should be "This is my program".
with the help of try and exception method, find the number is even or odd.'''


'''Question: 2
With the help of "w" or write() create a file and print a msg this is my program, and 
print a table with the help of while loop, use try and exception blocktake user.'''




#  What is module?

'''Consider a module to be the same as a code library. 
A file containing a set of functions you want to include in your applications.

Create a module
To create a module just save the code you want in a file with the file extension.py:
example

save the code in a file named mymodule.py'''

'''def greeting(name):
	print("Hello, "+name)'''

'''Use a module 
Now we can use the module we just created by using the import statement'''









###########   Python Datetime   ###########

# A date in python in not a data type of its own, but we can import a module named datetime to work with dates as date objects. 



'''Example:
Import the datetime module and display the current date:'''

'''import datetime
x = datetime.datetime.now()
print(x)
'''



# Return the year and name of weekdays:
'''import datetime
x = datetime.datetime.now()
print(x.year)              		# 2022
print(x.strftime("%A"))    		# Saturday
print(x.strftime("%a"))    		# Sat
print(x.strftime("%B"))    		# June
print(x.strftime("%b"))    		# Jun
print(x.strftime("%C"))    		# 20 (Prefix of the year)
print(x.strftime("%c"))    		# Sat Jun 18 14:04:54 2022
print(x.strftime("%D"))    		# 06/18/22  
print(x.strftime("%d"))    		# 18'''





########################  Numpy    ########################

# What is Numpy?

'''Numpy stands for Numercal python. Numpy is a python library used for working with arrays. 
It is also has function for working in domain of linear algebra, fourier transform, and matrix.

Matrix:  A set of number arrenged in row and columns so as to form a rectangular array.
We can say a matrix is a collection of numbers arrenged into a fixed numbers of rows and columns. 


# Why we use Numpy?

In python we have lists that serve the purpose of arrays, but they are slow to process.
Numpy aims to provide an array object that is faster than list.

# Why numpy is faster than list?
Numpy arrays are stored at one continous place in memory unlike lists, so process can access and manipulate them very efficiently.

# Which language is numpy written in?


# How can we start  Numpy?

Note: Numpy is used for numerical computing and scientific computing. It provides arrays and many function with help of arrays and function
we can perform many numerical operations and scientific operations. 


# What is array in python?

A python array is a collection of common type of data structures having elements with same data type. 
It is used to store collection of data. In Python programming, an array are handeled by the "array" module. 
If you create arrays using the array module, elements of the array must be of the same numeric type. 

# How we can Create an Array?'''

'''import numpy

x = numpy.array([1,2,3,4,5])
print(x)
#print(type(x))
#print(len(x))'''

'''import numpy
x = numpy.array([1,2,3,4,5])
print(x)'''

'''import numpy
x = numpy.array([1,2,3,4,5])
print(x)'''

# import numpy as np

'''import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))'''

# import numpy as np
'''x = no.array((1,2,3,4,5,6,7,8))
print(x)
print(type(x))
print(x.size)'''

# Numpy arrays are homogenious. javascript:void(0)

'''x = np.array([1,2j,8,9,"am"])
print(x)'''  # Converting in string

'''x = np.array([1,2j,8,9])
print(x)'''

'''x = np.array([1,2,8,9])
print(x)'''

'''What is the difference betwwen numpy array and nd array.
"ndarray()" is a class, while numpy. array() is method / function to create nd array.'''

######## Single Dimension Array:

'''x = np.array([[1,2,3,4,5]])
print(x.ndim)  # It represents the length of array, means number of square brackets. 1D, 2D, 3D......n 
print(type(x))
print(x.dtype)
print(x.size)'''



######### Multidimension Array

#Two D
'''x = np.array([[1,2,3,4,5]])
print(type(x))
print(x.dtype)
print(x.ndim)'''

'''import numpy as np

x = np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x[0][0][2])'''


###########################     Assignment     #########################

'''x = np.array([[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]]]])'''

'''find the type, dimension, print this array, size of this array,and extract these value of this array.  
return 7,12,18,1,20 and 3
return 7 to 10
return 12 to 13
reverse this array [16,17,18,19,20]
return 6 to 10
return 2 to 3

Print each array seprately. ''' 

'''import numpy as np

x = np.array([[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]]]])
print(x)                   # Print array
print(type(x))			   # Type of the array
print(x.ndim)              # Dimension of the array
print(x.size)              # size of array
print(x[0][0][0][1][1:5])  # return 7 to 10
print(x[0][0][0][2][1:3])  # return 12 to 13
print(x[0][0][0][3][::-1]) # reverse this array [16,17,18,19,20]
print(x[0][0][0][1])       # return 6 to 10
print(x[0][0][0][0][1:3])  # return 2 to 3
print(x[0][0][0][1][1])    # return 7 
print(x[0][0][0][2][1])    # return 12
print(x[0][0][0][3][2])    # return 18
print(x[0][0][0][0][0])    # return 1
print(x[0][0][0][3][4])    # return 20
print(x[0][0][0][0][2])    # return 3'''

###### 25th Jun ######


## Create an array with the help of arange method. 

# import numpy as np

'''x = np.arange(6)
print(x)'''

'''x = np.arange(1,11)
print(x)'''

'''x = np.arange(1,11,2)
print(x)'''


## Create an array with the help of 'zeros' and 'ones' method.

'''x = np.zeros(6)
print(x)
#print(type(x))'''

'''x = np.ones(6)
print(x)
#print(type(x))'''


# To join two arrays

'''x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
z = np.concatenate((x,y))
print(z)'''


# Create two arrays with the help of zeros and ones method and concatenate it. 
'''import numpy as np

x = np.zeros(6)
y = np.ones(6)
z = np.concatenate((x,y))
print(z)'''

# Create two arrays with the help of arange method and concatenate it and then do sort of this array. 

'''import numpy as np

x = np.arange(6,11)
y = np.arange(6)
z = np.concatenate((x,y))
z.sort()
print(z)'''


'''Full method: The full() function, generates an array with the specified dimensions 
and data type that is filled with specified number.'''

'''import numpy as np
x = np.full(3,2)    # 3-Times of element 2-Elements
print(x)'''


# string
'''x = np.array([1,2,3,4,5,'a'])
print(x.dtype)'''

# float
'''x = np.array([1,2,3,4,5.0])
print(x.dtype)'''

# complex
'''x = np.array([1,2,3,4,5.0,4j])
print(x.dtype)'''

'''x = np.array([[1,2,3,4,5],[6,7,8,9,10]],ndmin = 6)
# print(x.size)
# y=x.ndim
print(y)'''





###### sum of total rows and columns

'''x = np.array([10,6,2])
y = np.array([20,4,3])
z = np.sum([x,y])
print(z)'''


'''x = np.array([10,6,2])
y = np.array([20,4,3])
z = np.sum([x,y],axis=0)  # axis = 0, add these elements with respect to columns. 
print(z)'''


'''x = np.array([10,6,2])
y = np.array([20,4,3])
z = np.sum([x,y],axis=1)  # axis = 0, add these elements with respect to rows. 
print(z)'''


# Basic Airthmatic Operation for calculation. 

# Addition
'''x = np.array([10,6,4])
x = x+10
print(x)'''

# Subtraction
'''x = np.array([10,6,4])
x = x-10
print(x)'''

# Multiplication
'''x = np.array([10,6,4])
x = x*2
print(x)'''


# Exponent
'''x = np.array([10,6,4])
x = x**2
print(x)'''


# Divide
'''x = np.array([10,6,4])
x = x/2
print(x)'''

##### Numpy Math Function  #####

'''Mean: The average value
 To calculate the mean, find the sum of all values, and divide the sum by the number of values.''' 

'''x = np.array([10,20,30,40,50,60])
z = np.mean(x)
print(z)'''


'''Median: The median value is the value in the middle, after you have sorted all the values.''' 

'''x = np.array([11,44,5,96,67,85])
x.sort()
z = np.median(x)
print(z)'''


### Initializing numpy array with zeros

'''x = np.zeros((1,3))    # Two paarameters here, one for rows and three for columns 
print(x)'''


'''x = np.zeros((5,5))  # 1st parameter for rows and 2nd parameter for columns
print(x)'''


'''x = np.zeros((5,5))    # 1st parameter for rows and 2nd parameter for columns
x = x+2
print(x)
x = x+3
print(x)'''


'''x = np.ones((5,5))   # 1st parameter for rows and 2nd parameter for columns
print(x)'''

'''x = np.ones((5,5))  # 1st parameter for rows and 2nd parameter for columns 
x = x+2
print(x)
x = x+3
print(x)'''



### Full:  

'''x = np.full((3,4),5)   # 1st parameter for rows and 2nd parameter for columns and 5 is for desired matrix value.
print(x)
x = x*3
print(x)'''


###Range function

'''x = np.arange(100,505,5)   # start, end, gap Last value will not be included. 
print(x)'''


'''x = np.arange(10,55,5)   # start, end, gap (between the numbers) Last value will not be included. 
print(x)
x = x+3
print(x)'''



'''Initializing numpy array with random numbers'''


'''x = np.random.randint(1,50,5)  #  First parameter for specified the number and second also specified the number and third parameter tell how number you want. 
print(x)'''



# Question: 1
'''Find the random numbers between 100 to 100 and multiply these values with 5. '''

'''x = np.random.randint(100,1000,10)
print(x)
x = x*5
print(x)'''

# Question: 2
'''Create a matrix with ones() and add 6 in this matrix take 5 col and 6 rows'''

'''x = np.ones((5,6))
print(x)
x = x+6
print(x)
x = x*2
print(x)'''


# Question: 3
'''Create a matrix of 9 and multiply by 2 take 6 rows and 4 columns. '''

'''x = np.full((6,4),9)
print(x)
x = x*6
print(x)'''



# Examples:
'''x = np.zeros((5,5,6)) #  1st parameter is for no. of matrix(dimension) you want 2nd parameter is for row and 3rd parameter is for column.
print(x)'''


'''# Example: 2
x = np.eye(4)
print(x)'''


# Example: 3
'''x = np.eye(5,5)
a = np.diag(x)    # It fatches the diagnel values
print(a)
print(a+9)'''


'''x = np.diagflat([[1,2,3,4],[5,6,7,8]])
print(x)
a = np.diag(x)'''




###### Joining arrays using stack functions ######
 
'''Stacking is same as concatenation, the only difference is that satcking is done only a new axis. 

We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, i.e stacking. 

We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicility 
passed it is taken as 0.'''

'''x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.stack((x,y),axis = 1)  
print(z)'''


'''x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.hstack((x,y))  # stack them horizontally with hstack. 
print(z)'''

'''x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.vstack((x,y))  # stack them vertically with vstack. 
print(z)'''

'''x = np.array([1,2,3,7])
y = np.array([4,5,6,8])
z = np.dstack((x,y))  #  
print(z)'''

'''x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.concatenate((x,y))   
print(z)'''

'''x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.concatenate((x,y),axis=0) # concatenate according to row wise.   
print(z)'''






'''x = np.array([[1,2,3],[4,5,6]])
y = np.array([[7,8,9][10,11,12]])
z = np.concatenate((x,y),axis=1) # concatenate according to column wise.   
print(z)'''


### Numpy Splitting arrays

'''Splitting is reverse operation of joining. 

Joining merges multiple arrays into one and splitting breaks one array into multiple.   

We use array_split() for Splitting arrays, we pass it the array we want to split and the number of splits. 

Example:'''

'''x = np.array([1,2,3,4,5,6,7,8])
y = np.array_split(x,4)
print(y)'''


'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
y = np.array_split(x,8)
print(y)'''

'''x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
y = np.hsplit(x,3)
print(y)'''

'''x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
y = np.vsplit(x,3)
print(y)'''

'''x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
y = np.hsplit(x,3)
print(y)'''

'''x = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]])
y = np.dsplit(x,3)
print(y)'''






#### Use Transpose()  #### 

'''It interchange the position of rows and columns:'''

'''x = np.array([[1,2,3,4],[5,6,7,8]]) 
print(x.transpose())
#print(x.T)'''


#### Broadcasting in Arrays ####

'''x = np.array([1,2,3,4])
y = np.array([2,2,2,2])
print(x*y)'''

'''x = np.array([1,2,3,4,5,6,7,8,9,10])
y = 3
print(x*y)'''


'''a = np.array([1,2,3,4,5,6,7])
b = np.array([8,9,10,11,12,13,14])
c = a*b
print(c)'''


'''a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
b = np.array([2,4,6,8,10,12,14])
c = a*b
print(c)'''

'''x = np.array([[2,3,4,5],[6,7,8,9]])
y = np.array([4,3,4,2])
z = x+y
print(z)'''




###  Numpy array copy vs view  ###


'''The difference between copy and view. 
 The main difference between a copy and a view of an array is that the copy is a new array, and the 
 view is just a view of the original array.
 
 
 The copy owns the data and any changes made to the copy will not affect original array, 
 any changes made to the original array will not affect the copy. 
 
 The view does not own the data and any changes made to the view will affect the original and any changes made 
 to the original array will affect the view. 
 
 copy:
 
 Make a copy change the original array and display both arrays:
 The copy should not to be affected by the changes made to the original array.''' 

'''x = np.array([1,2,3,4,5])
y = x.copy()
x[1] = 15
print(x)
print(y)'''


#View:

'''x = np.array([1,2,3,4,5])
y = x.view()
x[1] = 15
print(x)
print(y)'''


##### Numpy array iterating
##### Iterating Arrays

'''Iterating meean going through elements one by one. 
 As we deal with multi-dimentional arras in numpy, we can do this using basic for loop
 of python.
 
 If we iterate on a 1-D array it will go though each element one by one. 
 
 Iterate on the element of the following 1-D arraay.''' 

'''x = np.array([1,2,3,4,5])
for i in x:
	print(i)'''


'''Iterate on the element of the following 2-D arraay.''' 

'''x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in x:
	print(i)'''

'''x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in x:
	for y in i:
		print(y)'''


'''x = np.array([[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]])
for i in x:
	for y in i:
		for z in y:
			print(z)'''





########  Iterating Array using nditer()
#text





'''x = np.array([[[1,2],[3,4],[5,6],[7,8]]])
for i in np.nditer(x):
	print(i)'''


####  Searching an array:

'''You can search an array for a certain value, and return the indexex that get a match. 
to search an array use the where() method.'''

#example:

#Find the indexes where the value is 4:

'''x = np.array([1,2,3,4,5,4,4])
y = np.where(x == 4)  # lookup place values
print(y)'''

'''x = np.array([1,2,3,4,5,4,4])
y = np.where(x%2 == 0)  
print(y)'''





'''import pywhatkit
pywhatkit.sendwhatmsg('+919625641944','Happy Birthday',14,00)'''

###  9th Jul 2022

#How can we calculate arrays with comparision operators:

#If you want to select values from your array that fulfill certain conditions, it's straight forward with Numpy.

#For example, if you strart with this array:

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print(x[x<5])
print(x[x>12])
print(x[x>10])
print(x[x<=5])'''

# you can select elements that satisfy tow conditions using the & and | operators.

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#print(x[(x>2) & (x<11)])
print(x[(x>1)&(x<16)])'''

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
z = x[x%2==0]
print(z)'''

'''x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#z = x[(x<2) | (x>16)]
z = (x<3) | (x>16) for get out in boolean.
print(z)'''


#  How to create an empty matrix

# import numpy as np

'''x = np.empty([4,5],dtype=int)
print(x)'''


'''x = np.empty([3,2],dtype=int)   # row: 3  col: 2
print(x)'''


# argmax() method returns the index value of largest element. 

# Maximum
# it returns the index value of largest element.

'''x = np.array([10,20,25,15,30,28])
a = x.argmax()
print(a)'''


# Minimum
# it returns the index value of smallest element.
'''x = np.array([10,20,8,15,30,28])
a = x.argmin()
print(a)'''


# It returns the sorting index value. 
'''x = np.array([10,20,8,15,30,28])
a = x.argsort()
print(a)'''


### Intersaction and difference method()

#  intersaction() tells the common values in both the arrays. 

'''x = np.array([[10,22,12,8,15,20]])
y = np.array([[10,21,18,8,16,20]])
z = np.intersect1d(x,y)
print(z)'''



# setdiff1d() it gives the unique value in x. 
'''x = np.array([10,12,17,14,11,15,20,26])
y = np.array([11,12,19,14,18,15,23,26])
z = np.setdiff1d(x,y)   # Check unique values in x. 
print(z)'''


'''x = np.array([10,12,17,14,11,15,20,26])
y = np.array([11,12,19,14,18,15,23,26])
z = np.setdiff1d(y,x)  # Check unique values in x.
print(z)'''


# Flip Method

'''x = [1,34,7,9,56,4]
z = np.flip(x)
print(z)'''


#  Flatten Arrays:

'''x = np.array([[2,4],[5,3]])
y = x.flatten()
print(y)'''

'''x = np.array([[12,22,14],[15,30,13],[23,35,29]])
y = x.flatten()
print(y)'''

# What is cumsum in numpy
'''numpy.cumsum() function is used when we want to complete the cumulative
 sum of array elements over a given axis.''' 

'''x = np.array([[3,2,6],[4,8,7]])
y = np.cumsum(x)
print(y)'''

'''x = np.array([[3,2,6],[4,8,7]])
y = np.cumsum(x,axis=1)
print(y)'''

'''x = np.array([[3,2,6],[4,8,7]])
y = np.cumsum(x,axis=0)
print(y)'''


'''Numpy Array Reshaping
Reshaping menas changing the shape of an array. 
The shape of an array is the number of elements in each dimension.
By reshaping  

'''


'''x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(x.shape)
print(x)'''

'''x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(4,3)   # first parameter for row and second parameter for column. 
print(x1)
'''

'''x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(3,4)   # first parameter for row and second parameter for column. 
print(x1)
'''
'''x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(2,6)   # first parameter for row and second parameter for column. 
print(x1)'''

'''x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(6,2)   # first parameter for row and second parameter for column. 
print(x1)'''


# Convert into 1 D array into three D array. 
'''x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(2,3,2)
print(x1)'''

'''x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = x.reshape(3,2,2)
print(x1)'''




####  Pandas  #####



import numpy as np

import pandas as pd

'''x = pd.Series([23,45,67,89,55,34])
print(x)
print(type(x))
print(len(x))'''


'''x = pd.Series([23,45,67,89,55,'a','b','c',True,False])
print(x)'''

# Labels
'''if nothing else is specified, the values are labeled with their index number. First values has index 0
second values is index 1. 

This label can be used to access a specified value. 
Return the first value of the series. '''

'''x = pd.Series(['a','b','c','d','e'])
print(x[4])'''


'''Series is a one dimensional labeled array'''

'''Create a labels
With the index argument you can name your own labels. 
Create your own labels:'''

'''x = pd.Series([1,2,3,4,5,6], index = ['a','b','c','d','e','f'])
print(x)
print(x['d'])'''

'''
x = pd.Series([1,2,3,4,5], index = ['one','two','three','four','five'])
print(x)
print(x.dtype)
print(x.index)
'''

'''x = pd.Series(np.random.randint(100,1000,5), index=['a','b','c','d','e'])
print(x)
'''

'''x = pd.Series(np.random.randint(100), index=['a','b','c','d','e'])
print(x)
print(x.dtype)
print(x.index)'''


'''x = pd.Series({'a':10,'b':20,'c':30})
print(x)
'''

'''x = pd.Series({'Name':'Rohit','Class':'MBA','Roll No.':30})
print(x)'''


# Changing index position
'''x = pd.Series({'a':10,'b':20,'c':30}, index = {'a','d','c','b'})
print(x)'''

'''student = pd.Series({'Name':'Omkar','Class':'UKG','Roll No.':'22'}, index={'Name','Class','Age','Roll no.'})
print(student)'''


# Extracting Elements from back

'''x = pd.Series([23,43,45,56,35,76,72])
print(x[::])'''

'''x = pd.Series([23,43,45,56,35,76,72])
print(x[-3:])
'''

'''x = pd.Series([23,43,45,56,35,76,72])
print(x[::-2])'''

'''x = pd.Series([23,43,45,56,35,76,72])
print(x[-3:])'''



## Basic Math Operation with pd.Series()

'''x1 = pd.Series([24,45,65,23,72,75])
x2 = pd.Series([53,56,45,78,23,76])
z = x1+x2
print(z)
print(x1+x2)
print(x1-x2)
print(x1*x2)
print(x1/x2)
print(x1//x2)
'''




## Pandas DataFrame:

'''
What is a DataFrame?
A Pandas DataFrame is a 2-dimensional labeled data structure, like a 2-dimensional array,or a table with rows and column.


DataFrame
Dataframe is a 2 dimensional or multidimensional labeld data structure with column of potentially different types. YOu can 
think of it like a spreadsheet or SQL table, or a dict o series objects. It is generally the most commonly used pandas object.
Like series, dataframe accepts many different kins of input'''

'''x = pd.DataFrame({'Name': ['Deepak', 'Ranjeet', 'Omkar', 'Swarika'], 'Marks':[85,101,100,5]})
print(x)
print(type(x))
print(len(x))'''


'''x = pd.DataFrame({'Name': ['Deepak', 'Ranjeet', 'Omkar', 'Swarika'], 'Marks':[85,101,100,5]}, index =['a','b','c','d'])
print(x)'''

'''x = pd.DataFrame({'Name': ['Deepak', 'Ranjeet', 'Omkar', 'Swarika'], 'Marks':[85,101,100,5]}, index =[1,2,3,4])
print(x)
print(x.index)'''

'''x = pd.DataFrame({'Fruits':['Apple','Mango','Banana'],'cost':[50,100,150]},index=['a','b','c'])
print(x)'''

'''x = pd.DataFrame({'One':[1.2,2.4,5.6,8.6],'Two':[3.4,5.3,3.2,3.8]})
print(x)'''

'''x = pd.DataFrame({"Fruits":['Apple','Mango','Banana'],'Cost':[50,120,40],'Quality':['Good for health','Sweet','Yummy']})
print(x)'''

'''x = pd.DataFrame({"Fruits":['Apple','Mango','Banana'],'Cost':[50,120,40],'Quality':['Good for health','Sweet','Yummy']}, index = [1,2,3])
print(x)'''


'''x = pd.DataFrame({"Fruits":['Apple','Mango','Banana'],'Cost':[50,120,40],'Quality':['Good for health','Sweet','Yummy']}, index = [1,2,3],columns=['Quality','Fruits','Cost'])
print(x)'''


'''x = pd.DataFrame({'Name':['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit','Rohit','Karan'],
	'Salary':[30000,40000,50000,60000,70000,8000,10000,20000],
	'Designation':['Program Manager','Data Analyst','Data Scientist','Manager','Project Coordinator','SME','QA','Team Lead']},index = ['a','b','c','d','e','f','g','h'])
print(x)'''




# DataFrame Concate, Append, Merge

'''x = pd.DataFrame({'Name':['Omkar','Ranjeet','Deepak'],
	'Salary':[30000,40000,50000],
	'Designation':['Program Manager','Data Analyst','Data Scientist']},index = ['a','b','c'])

y = pd.DataFrame({'Name':['Ram','Mohit','Shobhit'],
	'Salary':[60000,70000,8000],
	'Designation':['Manager','Project Coordinator','SME']},index = ['d','e','f'])

z = pd.DataFrame({'Name':['Rohit','Karan','Saran'],
	'Salary':[10000,20000,50000,],
	'Designation':['QA','Team Lead','DTP']},index = ['g','h','i'])
r = (x,y,z)
w = pd.concat(r)
print(w)'''


'''x = pd.DataFrame({'Name':['Omkar','Ranjeet','Deepak'],
	'Salary':[30000,40000,50000],
	'Designation':['Program Manager','Data Analyst','Data Scientist']},index = ['a','b','c'])

y = pd.DataFrame({'Name':['Ram','Mohit','Shobhit'],
	'Salary':[60000,70000,8000],
	'Designation':['Manager','Project Coordinator','SME']},index = ['d','e','f'])

a = x.append(y)
print(a)'''



# Merge in DataFrame:


#### Inner Merge ####

'''x = pd.DataFrame({'Name_1':['Omkar','Ranjeet','Deepak','Mohit'],
	'Salary_1':[30000,40000,50000,25000]})

y = pd.DataFrame({'Name_2':['Ram','Mohit','Shobhit','Ranjeet'],
	'Salary_2':[60000,70000,8000,35000]})

z = pd.merge(left=x, right=y, how='inner',left_on='Name_1', right_on='Name_2' )
print(z)'''



'''x = pd.DataFrame({'Name_1':['Omkar','Ranjeet','Deepak','Mohit'],
	'Salary_1':[30000,40000,50000,25000]})

y = pd.DataFrame({'Name_2':['Ram','Mohit','Shobhit','Ranjeet'],
	'Salary_2':[60000,70000,8000,35000]})

z = pd.merge(left=x, right=y, how='inner',left_on='Name_1', right_on='Name_2',indicator=True)
print(z)'''



#### Outer Merge ####

'''x = pd.DataFrame({'Name_1':['Omkar','Ranjeet','Deepak','Mohit'],
	'Salary_1':[30000,40000,50000,25000]})

y = pd.DataFrame({'Name_2':['Ram','Mohit','Shobhit','Ranjeet'],
	'Salary_2':[60000,70000,8000,35000]})

z = pd.merge(left=x, right=y, how='outer',left_on='Name_1', right_on='Name_2')
print(z)'''


'''x = pd.DataFrame({'Name_1':['Omkar','Ranjeet','Deepak','Mohit'],
	'Salary_1':[30000,40000,50000,25000]})

y = pd.DataFrame({'Name_2':['Ram','Mohit','Shobhit','Ranjeet'],
	'Salary_2':[60000,70000,8000,35000]})

z = pd.merge(left=x, right=y, how='outer',left_on='Name_1', right_on='Name_2',indicator=True)
print(z)'''


#### Left Merge ####

'''x = pd.DataFrame({'Name_1':['Omkar','Ranjeet','Deepak','Mohit'],
	'Salary_1':[30000,40000,50000,25000]})

y = pd.DataFrame({'Name_2':['Ram','Mohit','Shobhit','Ranjeet'],
	'Salary_2':[60000,70000,8000,35000]})

z = pd.merge(left=x, right=y, how='left',left_on='Name_1', right_on='Name_2')
print(z)'''


'''x = pd.DataFrame({'Name_1':['Omkar','Ranjeet','Deepak','Mohit'],
	'Salary_1':[30000,40000,50000,25000]})

y = pd.DataFrame({'Name_2':['Ram','Mohit','Shobhit','Ranjeet'],
	'Salary_2':[60000,70000,8000,35000]})

z = pd.merge(left=x, right=y, how='left',left_on='Name_1', right_on='Name_2',indicator=True)
print(z)'''



#### Right Merge ####

'''x = pd.DataFrame({'Name_1':['Omkar','Ranjeet','Deepak','Mohit'],
	'Salary_1':[30000,40000,50000,25000]})

y = pd.DataFrame({'Name_2':['Ram','Mohit','Shobhit','Ranjeet'],
	'Salary_2':[60000,70000,8000,35000]})

z = pd.merge(left=x, right=y, how='right',left_on='Name_1', right_on='Name_2')
print(z)'''


'''x = pd.DataFrame({'Name_1':['Omkar','Ranjeet','Deepak','Mohit'],
	'Salary_1':[30000,40000,50000,25000]})

y = pd.DataFrame({'Name_2':['Ram','Mohit','Shobhit','Ranjeet'],
	'Salary_2':[60000,70000,8000,35000]})

z = pd.merge(left=x, right=y, how='right',left_on='Name_1', right_on='Name_2',indicator=True)
print(z)'''





### String methods in Pandas ### 

# Converts strings in the series/index to lower case.as

# Use of lower

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit','Rohit','Karan'])
#print(x)
print(x.str.lower())'''

# Use of Title

# It will provide the first letter in capital letter in all element. 

'''x = pd.Series(['omkar','ranjeet','deepak','ram','mohit','shobhit','rohit','karan'])
print(x.str.title())'''




# Use of Upper

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit','Rohit','Karan'])
#print(x)
print(x.str.upper())'''



# Computes string length()

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit','Rohit','Karan'])
print(x.str.len())
print(len(x))
'''

# Use of split pattern method(). 

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit','Rohit','Karan'])
print(x.str.split())'''



# Use of cat (sep=pattern)
'''cat(sep='__')
 Concatenate the series/index elements with given seperator.''' 

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit','Rohit','Karan'])
print(x.str.cat(sep='**'))'''


# Contains Method()

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit'])
print(x.str.contains('it'))'''


# Use of replace method

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Moheet','Shobheet'])
print(x.str.replace('eet','it'))'''



'''# Use of repeat(value)
x = pd.Series(['Omkar ','Ranjeet ','Deepak ','Ram ','Mohit ','Shobhit '])
print(x.str.repeat(2))'''



'''# Use of count() pattern method

# It returns count of appearance of pattern in each element. 

x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit'])
print(x.str.count('e'))
print(x.str.count('a'))'''



# Use of starts with pattern:
# It returns true if the element in the series/index starts with the pattern. 

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit'])
print(x.str.startswith('O'))   # True
print(x.str.startswith('B'))  # False'''


# Use of ends with pattern:
# It returns true if the element in the series/index ends with the pattern. 

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit'])
print(x.str.endswith('t'))   # True
print(x.str.endswith('B'))  # False'''


# Use of find with pattern:
# It Returns the first position of the first occurrence of the pattern. 
# "-1" Indicates that there no such pattern available in the element. 

'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit'])
print(x.str.find('R'))   #  0
print(x.str.find('T'))   #  -1  '''  



# Use of findall method
# It returns a list of all occurrence of the pattern. 
'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit'])
print(x.str.findall('R'))      # [R] if exists
print(x.str.findall('T'))      # [] if does not exists'''



# Use of swap case
# Swap the case lower case to upper case and upper case to lower case. 
'''x = pd.Series(['Omkar','Ranjeet','Deepak','Ram','Mohit','Shobhit'])
print(x.str.swapcase())'''

# Use of isupper()

'''Check weather all characters in each string in the series/index in upper case or not. 
Retrurns boolean'''

'''x = pd.Series(['Omkar','Ranjeet','DEEPAK','RaM','MOHIT','Shobhit'])
print(x.str.isupper())'''



# Use of isupper()
'''Check weather all characters in each string in the series/index in lower case or not. 
Retrurns boolean'''

'''x = pd.Series(['omkar','Ranjeet','DEEPAK','RaM','MOHIT','Shobhit'])
print(x.str.islower())'''




# Use of drop_duplicates() to remove the duplicate data.

'''x = pd.DataFrame({'Empolyee':['Omkar','Ranjeet','Deepak','Ram','Omkar','Shobhit'],'salary':[20000,40000,50000,60000,20000,77000]})
x = x.drop_duplicates()
print(x)'''

# By doing this data keep save in x veriable and remove by drop_duplicates() from z veriable.

'''x = pd.DataFrame({'Empolyee':['Omkar','Ranjeet','Deepak','Ram','Omkar','Shobhit'],'salary':[20000,40000,50000,60000,20000,77000]})
z = pd.DataFrame(x)
z = z.drop_duplicates()
print(z)'''



# Use to read a file. 

'''x = pd.read_csv('D:/Dataset/Iris.csv')
print(x)'''

'''x = pd.read_csv('D:/Dataset/Iris.csv')
print(x.head())'''

'''x = pd.read_csv('D:/Dataset/Iris.csv')
print(x.head(15))'''

'''x = pd.read_csv('D:/Dataset/Iris.csv')
print(x.tail())'''

'''x = pd.read_csv('D:/Dataset/Iris.csv')
print(x.tail(20))'''

'''x = pd.read_csv('D:/Dataset/Iris.csv')
print(x.shape)'''

'''x = pd.read_csv('D:/Dataset/Iris.csv')
print(x.describe())'''







## Data Cleaning:

# It will remove the rows in which any cell will be blank. 
'''x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
x.dropna(inplace=True)
print(x)'''


# It will update (anything) the rows in which any cell will be blank. 

'''x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
x.fillna('Blank',inplace=True)
print(x)'''

# In this we can update a blank cell by any string/number(anything)
'''x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
x['Calories'].fillna('Ranjeet',inplace = True)
print(x)'''

# It is use to correct the format of date in a column. 

'''x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
x.dropna(inplace = True)
x['Date'] = pd.to_datetime(x['Date'])
print(x)'''


# It is use to update a value in a specific row no. and column. 
'''x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
x.loc[7,'Duration'] = 45        # '7' is Row no. and 'Duration' is a name column. 
print(x)'''



# It is use to show the data between a specific range. 
'''x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
z = x.dropna()
y = z.iloc[0:10,0:4]
print(y)'''


# It is use to show the value of specific row no. and col no. 
'''x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
z = x.dropna()
y = z.iloc[4,2]
print(y)'''


# It is use to show the complete data of a specific row no. 
'''x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
z = x.dropna()
y = z.iloc[:,[2,0]]
print(y)'''


###############################################################################
'''# query: need to ask again 
x = pd.read_csv('D:/Personal/Dataset/dataset1.csv')
z = x.dropna()
y = z.iloc[2,'Pulse']
print(y)
'''
###############################################################################


### Aggregate Function in Pandas:


'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
#print(x.head())'''


'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
y = x.min()
print(y)'''


'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
y = x.max()
print(y)'''


'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
y = x.mean()
print(y)'''

'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
y = x.median()
print(y)'''

'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
y = x.std()
print(y)'''

'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
y = x.sum()
print(y)'''

'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
y = x.count()
print(y)'''

'''x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
y = x.describe()
print(y)'''



'''x = pd.DataFrame({'Company':['Google','Google','Yahoo','Yahoo','Amazone','Amazone'],
	'Person':['Aman','Mohan','Karan','Pihu','Rohit','Sachin'],
	'Sales':[400,450,100,500,320,250]})
#print(x)

#z = (x.groupby('Company'))
#print(z)

#print(z.min())
#print(z.max())
#print(z.mean())
#print(z.median())
#print(z.count())
#print(z.sum())
#print(z.describe().transpose())
#print(z.describe().transpose()['Amazone'])'''



'''x = pd.read_excel('D:/Personal/Dataset/dataset2.xlsx')
print(x)'''












####  13th Aug 2022  #####

###  Matplotlib  ###

#print(matplotlib._version)

'''What is matplotlib?
Matplotlib is a cross-platform, data visualization and graphical plotting library for python
and its numerical extension Numpy.
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
'''

## Working with Pyplot

'''The matplotlib.pyplot is the collection command style functions that make matplotlib feel like 
woking with MATLAB.


The Pyplot functions are used to make some changes to figure such as create a figure, creates a plotting 
area in a figure, plots some lines in a plotting area decorate the plot including lebels, etc. pyplot is a 
submodule od matplotlib. '''

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd



# To crate line plot. 

'''x = np.arange(1,15)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.show()'''


# To add title and labels in a line plot. 

'''x = np.arange(1,15)
y = 2*x
print(x)
print(y)
plt.plot(x,y)
plt.title("Simple Line Plot")
plt.xlabel("Data on x-axis")
plt.ylabel("Data on y-axis")
plt.show()
'''


# To add color, linestyle, linewidth

'''x = np.arange(1,15)
y = 2*x
print(x)
print(y)
#plt.plot(x,y)
plt.plot(x,y,color="purple", linestyle = ":", linewidth = 3)
plt.title("Simple Line Plot")
plt.xlabel("Data on x-axis")
plt.ylabel("Data on y-axis")
plt.show()'''



## If we want two lines in the same plot.

'''x = np.arange(1,15)
y1 = 2*x
y2 = 3*x
print(y1)
print(y2)
plt.plot(x,y1,color="purple", linestyle = ":", linewidth = 5)
plt.plot(x,y2,color="red", linestyle = "-.", linewidth = 5)
plt.title("Two lines on one Plot")
plt.xlabel("Range")
plt.ylabel("Two Lines")
plt.grid(True)
plt.show()'''



### To Create subplot. 

'''x = np.arange(1,15)
y1 = 2*x
y2 = 3*x
print(y1)
print(y2)
plt.subplot(1,2,1)  # first parameter for row and second for columns and third parameter for show this is a first subplot.
plt.plot(x,y1,color="purple", linestyle = ":", linewidth = 3) 
plt.subplot(1,2,2) # first parameter for row and second for columns and third parameter for show this is a first subplot.
plt.plot(x,y2,color="red", linestyle = ":", linewidth = 3)
plt.show()'''


### To stack both subplots coloumnwise.
'''x = np.arange(1,15)
y1 = 2*x
y2 = 3*x
print(y1)
print(y2)
plt.subplot(2,1,1)  # first parameter for row and second for columns and third parameter for show this is a first subplot.
plt.plot(x,y1,color="purple", linestyle = ":", linewidth = 3)
plt.grid()
plt.subplot(2,1,2) # first parameter for row and second for columns and third parameter for show this is a first subplot.
plt.plot(x,y2,color="red", linestyle = ":", linewidth = 3)
plt.grid()
plt.show()'''


####  14th Aug 2022

'''To create Bar Plots.
We apply bar plot on the categorical values and we apply histogram for the numerical values.
What is the difference between bar plot and histogram, we bar plot for categorical values, 
and histogram use for only numerical values.'''

# Example: 1

'''student = {'Omkar':90,'Aman':75,'Komal':65,'Ranjeet':95,'Deepak':35}
a = list(student.keys())
b = list(student.values())
print(a)
print(b)
plt.bar(a,b)
plt.show()'''


# Example: 2

# Varticle bar graph

'''vegetables_basket = {'Potato': 150,'Tomato':120,'Brinjal':180,'Carrot':200}
vegetables_names = list(vegetables_basket.keys())
vegetables_cost = list(vegetables_basket.values())
plt.bar(vegetables_names,vegetables_cost)
plt.title('Bar Plot')
plt.xlabel('vegetables_names')
plt.ylabel('vegetables_cost')
plt.grid(True)
plt.show()'''

# Example: 2

# Horizontal bar graph.

'''vegetables_basket = {'Potato': 150,'Tomato':120,'Brinjal':180,'Carrot':200}
vegetables_names = list(vegetables_basket.keys())
vegetables_cost = list(vegetables_basket.values())
plt.barh(vegetables_names,vegetables_cost,color = 'red')  
plt.title('Bar Plot')
plt.xlabel('vegetables_names')
plt.ylabel('vegetables_cost')
plt.grid(True)
plt.set_facecolor('blue')
plt.show()'''


### Scatter plot

'''x = [10,20,30,40,50,60,70,80,90]
a = [10,23,70,20,9,30,46,33,28]
b = [80,20,52,67,92,13,42,56,36]
plt.subplot(1,2,1)
plt.scatter(x,a,marker="*",color='g',s=150)
plt.title('Company Green')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(x,b,marker=".",color='red',s=300)
plt.title('Company Red')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()
'''

'''x = [10,20,30,40,50,60,70,80,90]
a = [10,23,70,20,9,30,46,33,28]
b = [80,20,52,67,92,13,42,56,36]
plt.subplot(2,1,1)
plt.scatter(x,a,marker="*",color='g',s=150)
plt.title('Company Green')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplot(2,1,2)
plt.scatter(x,b,marker=".",color='red',s=300)
plt.title('Company Red')
plt.xlabel('Years from entity origin')
plt.ylabel('Revenue growth in percentage(%)')
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()'''

####################   Incmplete    #########



## 20th Aug 2022 ##

# Histogram:

'''A histogram is a graphical representation that organizes a group of data points into user-specified ranges.

A histogram is a graph showing frequency distributions.

It is a graph showing the number of obervations within each given interval. 
Example: Say you ask for that height of 250 people, you might end up with a histogram like this. '''



'''data = [1,1,2,2,2,2,3,3,3,4,4]
plt.hist(data)
plt.show()'''


'''a = [1,1,2,2,2,3,3,3,3,4,4,5,5,5]
plt.hist(a,color = 'red',bins = 15)
plt.show()'''


'''a = [3,4,5,7,9,4,3,2,2,4,5,6,6,5,4,3,2,2]
plt.hist(a,bins = 15)
plt.show()'''



'''a = [3,4,5,7,9,4,3,2,2,4,5,6,6,5,4,3,2,2]
plt.hist(a,bins = 15)
plt.xlabel('Years')
plt.ylabel('Revenue growth')
plt.show()'''


## Pie chart ##

'''Use of pie chart: A pie chart is a type of graph that represent the data in cicular graph.
the slices of pie
show the relative size of the data

Why we use pie chart?
Pie charts are used to represent the proportional data or relative data in a single chart. 
The concept of pie slices is use to show the percentage of a particular data from whole pie.

autopct = '%0.1f%%' is use to show the percentage of the data in the pie chart.'''

'''fruit = ['Mango','Apple','Guava','Banana','Orange']
cost = [50,35,200,45,150]
plt.pie(cost,labels=fruit)
plt.show()'''


'''fruit = ['Mango','Apple','Guava','Banana','Orange']
cost = [50,35,200,45,150]
plt.pie(cost,labels=fruit,autopct = '%0.1f%%',colors = ['red','blue','green','teal','hotpink',],startangle=90, radius=1.2)
plt.show()'''





## DoughNut-Chart: It is look like a pie chart but it has one whole in the center of circle.

'''fruit = ['Mango','Apple','Guava','Banana','Orange']
cost = [50,35,125,45,140]
plt.pie(cost,labels=fruit,autopct = '%0.1f%%',colors = ['red','blue','green','yellow','teal',],startangle=90, radius=1)
plt.pie([5],colors=['white'],radius=0.4)
plt.show()'''





# Question pending

'''
x = pd.read_csv('D:/Personal/Dataset/Iris.csv')
plt.hist(x)
plt.show()
'''



import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

'''x = pd.read_csv("D:/Personal/Dataset/pokemon.csv")
#print(x)
sns.set(style = "whitegrid")
sns.barplot(x = "Legendary",y = "Speed",hue = "Generation",data = x)
plt.show()'''


'''x = pd.read_csv("D:/Personal/Dataset/pokemon.csv")
#print(x)
sns.set(style = "whitegrid")
sns.barplot(x = "Legendary",y = "Speed",hue = "Generation",data = x,palette = "Reds_d")
plt.show()
'''

'''x = pd.read_csv("D:/Personal/Dataset/pokemon.csv")
#print(x)
sns.set(style = "whitegrid")
sns.barplot(x = "Legendary",y = "Speed",hue = "Generation",data = x,palette = "rocket")
plt.show()'''


'''x = pd.read_csv("D:/Personal/Dataset/pokemon.csv")
#print(x)
sns.set(style = "whitegrid")
sns.barplot(x = "Legendary",y = "Speed",hue = "Generation",data = x,palette = "vlag")
plt.show()'''



# To change a specific color of our bar plot.
'''x = pd.read_csv("D:/Personal/Dataset/pokemon.csv")
y = x.head()
sns.set(style = "whitegrid")
#sns.barplot(x = "Legendary",y = "Speed",data = x,color = "g")
#sns.barplot(x = "Legendary",y = "Speed",data = x,color = "red")
#sns.barplot(x = "Legendary",y = "Speed",data = x,color = "blue")
#sns.barplot(x = "Legendary",y = "Speed",data = x,color = "orange")
plt.show()
'''



'''Scatter plot calculate between two numerical values. 
Note: This graph shows there is a linear relationship. As 'Sepal_Length' is increasing simentaneously.'''


################ Here 'hue' we used to get a diff diff shapes for scatter plot. 

'''x = pd.read_csv('D:/Personal/Dataset/iris.csv')
y = x.head()
#print(y)
sns.scatterplot(x = 'Sepal_Length',y = 'Petal_Length',data = x, hue = 'Species',style = 'Species')
plt.show()'''


'''x = pd.read_csv('D:/Personal/Dataset/iris.csv')
y = x.head()
#print(y)
sns.scatterplot(x = 'Sepal_Length',y = 'Petal_Length',data = x, hue = 'Petal_Length',style = 'Species')
plt.show()'''


'''This is a box plot an I got his data from churn file, to make box plot we will need one categorical columns and second columns
should be numerical, we we make this box plot in two columns, churn columns and tennure columns which shows that customer will churn or not, means customer will use
this my telecom service or not.

In this box plot numerical lable will come on y axis and categorical value will come on x axis.we will use this box plot for multivarient visulaization
There is metioned yes means customer will left you and no means customer will not left you. There is mentioned a black line in between box plot that will
show your may 40 months there is more chances that customer will not left you. we will use median values for analysis.'''


'''x = pd.read_csv('D:/Personal/Dataset/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x = 'Churn', y = 'tenure', data = x)
plt.show()'''



'''x = pd.read_csv('D:/Personal/Dataset/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x = 'InternetService', y = 'tenure', data = x)
plt.show()'''


'''x = pd.read_csv('D:/Personal/Dataset/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x = 'InternetService', y = 'tenure', data = x,color = 'green')
plt.show()'''


'''x = pd.read_csv('D:/Personal/Dataset/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x = 'InternetService', y = 'tenure', data = x, palette = 'Set1', linewidth = 4)
plt.show()'''


'''x = pd.read_csv('D:/Personal/Dataset/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x = 'Contract', y = 'tenure', data = x, palette = 'Set1', linewidth = 4)
plt.show()'''


'''x = pd.read_csv('D:/Personal/Dataset/Churn.csv')
y = x.head()
print(y)
sns.boxplot(x = 'Contract', y = 'tenure', data = x, order = ['Two year','Month-to-month','One year'])
plt.show()'''


'''x = pd.read_csv('D:/Personal/Dataset/iris.csv')
print(x.head())
plt.hist(x['Sepal_Length'],bins = 50, color = 'orange')
plt.show()'''


'''one  = [1,2,3,4,5,6,7,8,9]
two =  [1,2,3,4,5,4,3,2,1]
three = [6,7,8,9,8,7,6,5,4]
x = list([one,two,three])
plt.violinplot(x,showmedians = True)
plt.show()'''


'''import libraries as per ur requirement.
Take any one data set 
Find top 20 rows from data set
Extract bottom 10 row from data set
Extract any two column from data set
Extract 20 rows from the mid of data set
and show any two vizualisation with

'''







#Test

#Drop any four rows from the data set.
#x = pd.read_csv('D:/Personal/Dataset/matches.csv')
#x.dropna(inplace=True)
#print(x)

#Return 3 rows from the bottom.
#print(x.tail(3))

#Return 6 rows from the head.
#print(x.head(6))


#Return any 15 rows from the mid 
'''z = x.dropna()
y = z.iloc[10:25]
print(y)'''


#find the mean,count,min,max from this dataset.
#y = x.win_by_wickets.mean()
#print("The mean of the column 'win_by_wickets' is: ",y)

#y = x.win_by_runs.count()
#print("The mode of the column 'win_by_runs' is: ",y)

#y = x.win_by_runs.min()
#print("The mode of the column 'win_by_runs' is: ",y)

#y = x.win_by_runs.max()
#print("The mode of the column 'win_by_runs' is: ",y)



#count the values of any two columns.



#Take some data as you want and make a bar graph on this data.
'''x = pd.read_csv("D:/Personal/Dataset/pokemon.csv")
y = x.head()
sns.set(style = "whitegrid")
'''#sns.barplot(x = "Legendary",y = "Speed",data = x,color = "g")
#sns.barplot(x = "Legendary",y = "Speed",data = x,color = "red")
#sns.barplot(x = "Legendary",y = "Speed",data = x,color = "blue")
#sns.barplot(x = "Legendary",y = "Speed",data = x,color = "orange")
#plt.show()


#Find the mean any specific column.

#Drop any two colmns.

#find two columns and six rows from the mid.

#Show the number of rows and columns in the data set

#Getting the frequency of most of the match awards

#Getting the top 10 players with the most man of the match awards.


 
#Finding out the number of toss wins w.r.t each team
#toss = x.value_counts('toss_winner')
#print("The number of toss wins in the each team \n",toss)




#Extracting the records where a team.

#Make a bar plot for the top 5 players with most man of the match awards.

#Making a pie chart for distribution of most wins after batting second.

#Looking at the number of matches played each season.






##########################################################################################################################################################################################

##################  STATISTICS  ###################


import statistics as st
#x = np.array([10,20,30,56,40,50,60])

#Mean
#z = np.mean(x)
#print(z)


#Mode
#print(st.mode(x))


#Median
#z = np.median(x)
#print(z)



#x = pd.read_csv('D:/Personal/Dataset/Employee_monthly_salary.csv')

#print(x)

#print(x.head())



'''Random Sampling: 
Random sampling is one of the easiest forms of collecting data from the total population. Under random sampling, each member of 
the population carries an equal opportunity of being chosen as a part of the sampling process.'''

#print(x.sample(200))




'''Systematic Sampling: 
Systematic sampling is a probability sampling method where elements from a target population 
are chosen by selecting a random 
starting point and selecting sample members after a fixed ‘sampling interval. 
We do systematic sampling, choosing every 10th element.'''

#print(x.iloc[0:1802:10])



'''Stratified Sampling:
Stratum is a subset of the population having at least one common characteristic. Further sampling is done to select 
sufficient number of samples from each stratum. Stratified sampling is a common sampling technique used when trying to draw 
conclusions from different sub-groups or strata. Here, we do stratified sampling. First we choose only male data points, 
then we choose random data points. Similar can be done for the female data points, finally an aggregate of the data can be 
taken.'''

#x_male = x[x['Gender']=='M']
#print(x_male)
#print(x_male.head())
#print(x_male.sample(100))


#from scipy import stats

'''data = [66, 67, 67, 68, 68, 68, 68, 69, 69, 69, 69, 70, 70, 71, 71, 72, 73, 75, 65, 87]  


Q1 = np.median(data[:9])
Q3 = np.median(data[9:])
IQR = Q3 - Q1
print(IQR)'''


'''from scipy import stats
IQR = stats.iqr(data,interpolation = 'midpoint')
print(IQR)'''




### Standard Deviation:


'''x = [66, 67, 67, 68, 68, 68, 68, 69, 69, 69, 69, 70, 70, 71, 71, 72, 73, 75, 65, 87]
y = np.std(x)
print(y)'''


### Veriance:
'''x = [66, 67, 67, 68, 68, 68, 68, 69, 69, 69, 69, 70, 70, 71, 71, 72, 73, 75, 65, 87]
y = np.var(x)
print(y)'''

'''import warnings
warnings.filterwarnings('ignore')

x = [66, 67, 67, 68, 68, 68, 68, 69, 69, 69, 69, 70, 70, 71, 71, 72, 73, 75, 65]

a = np.percentile(x, 25, interpolation = 'midpoint')
print(a)'''

'''b = np.percentile(x, 75, interpolation = 'midpoint')
print(b)'''





############    Normal Distribution   ##############

'''The normal distribution is one  of the most important distributions. 
It is also called the gaussian distribution.percentile
Use the random.normal distribution

loc- (Mean) Where the peak of the bell exists. 

scale- (Std Deviation) How flat the graph distribution should be.

size- The shape of the returned array.percentile
'''

'''from numpy import random

x = random.normal(loc=1,scale=2,size=(2,3))
print(x)'''


'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000),hist=False)
plt.show()
'''






###What is Binomial Distribution?
'''The binomial distribution is a probability distribution that summrizes the likelihood that a value will take
one of two independent values under a given set of parameters or assumptions.

Binomial distribution is a discreate distribution.

It describe the outcome of binary scenarios, e.g toss of a coinm it will either be head or tails/

It has three parameters.

n - number of trails.

p - probability of occurance of each trial 

Size - The shape of the returned array.
'''


'''from numpy import random
x = random.binomial(n=10,p=0.5,size=10)
print(x)'''

'''visualization of binomial disctribution
example'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist =True, kde=False) #Kde is curve
plt.show()'''





####What is poission Distribution?

'''Poission Distribution is a Discrete Distribution.

In statistics, a poission Distribution is a probability Distribution that is used to show how many 
times an event is likely to occur over a specified period.`

example:
A poission Distribution can be used to estimate how likely it is that something'''

'''from numpy import random 
x = random.poisson(lam = 2,size=10)
print(x)'''


'''visualization of poisson distribution.
Example:'''


#What is Emprical Rule?








import scipy.stats as stats


'''#>>>> What is Z score?
x = np.array([6,7,7,12,13,13,15,16,19,22])
y = stats.zscore(x)
print(y)'''


#https://www.kaggle.com/code/victoriamiller19/outlier-detection

#x = pd.read_csv("D:/Personal/Dataset/weight-height.csv")


#print(x.head())

#print(x.Height.describe())

#print(x.Height.mean())

#print(x.Height.std())


#upper_limit = x.Height.mean() + 3*x.Height.std()
#print(upper_limit)


#lower_limit = x.Height.mean() - 3*x.Height.std()
#print(lower_limit)



#x['z-score'] = ( x.Height - x.Height.mean() ) / x.Height.std()
#print(x.head())


#print(x[x['z-score']>3])

#print(x[x['z-score']<-3])



############## Cityblock Distance (Manhattan Distance)

'''
x1 = int(input("Enter X Coordinates for point A: "))
y1 = x1 = int(input("Enter Y Coordinates for point A: "))

x2 = int(intput("Enter X Coordinates for point B: "))
y2 = int(intput("Enter X Coordinates for point B: "))

x = abs(x2-x1)

y = abs(y2-y1)

mant = x+y
print("Manhattan Distance: ", mant)
'''



import mysql.connector
x = mysql.connector.connect(user = 'root', password = 'Rschauhan@1995', 
	host = '127.0.0.1', 
	database = 'ranjeetsingh')
y = x.cursor(buffered = True)

query = ("SELECT name, salary, dept_no from a1")

y.execute(query, params = None,  multi = True)

for(name, salary, dept_no) in y:
	print(name, salary, dept_no)
x.close()











0