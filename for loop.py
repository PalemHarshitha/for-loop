#for loop:
#A for loop in python is used to iterate over a sequnce such as
#list,tuple,string or range and execute a block of code for each data in the sequnce.
#syn:
'''
for iterator in iterable:
    stmt
'''

#1.program to iterate any iterable?
'''
s='python'
for i in s:
    print(i)
'2.'
l=['python','java','devops']
for i in l:
    print(i)
'''

#2.program to iterate dictionary?
'''
dict={'python':78,'tata':65,'honda':98}
for i in dict:
    print(i)
'''
'''
dict={'python':78,'tata':65,'honda':98}
for i in dict.keys():
    print(i)
'''
'''
dict={'python':78,'tata':65,'honda':98}
for i in dict.values():
    print(i)
'''
'''
dict={'python':78,'tata':65,'honda':98}
for i in dict.items():
    print(i)
'''
#unpack
'''
dict={'python':78,'tata':65,'honda':98}
for i in dict.items():
    print(i[0],i[1])
'''

#control statements
#We have 3 control statements:
'''
1.break
2.continue
3.pass
'''



#1.break--->It is used to exit a loop permanently.
#It can be used inside for loop and while loop.
#syntax:
#while
'''
while cond:
    if cond:
        break
    incr/decr
'''
#for
'''
for iterator in iterable:
    if cond:
        break
'''


#example
#prgram to break when the number is 5?
'''
i=1
while i<10:
    if i==5:
        break
    else:
        print(i)
    i+=1
'''


#2.continue--->It is used to skip the rest of the code inside a loop for the recent iteration only.
#The continue keyword can be used only inside for loop.
#syntax:
'''
for iterator in iterable:
    if cond:
        continue
'''

#program to skip all the even numbers?
'''
t=(34,35,5,3,68,4,90,77,23)
for num in t:
    if num%2==0:
        continue
    print(num)
'''


#3.pass---->It is a null operator and it is used as a placeholder for future use.
#when the pass keyword is executed nothing happens and it is useful in the situation where
#code is required but not necessary at this moment.

#syntax:
'''
for iterator in iterable:
    pass
'''
#example
'''
for i in [1,2,4,5]:
    pass
for i in 'hai':
    print(i)

'''















































