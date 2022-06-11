# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:13:45 2022

@author: 081796
"""
##Introduction to the if Statement
x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')
    
##Python: It’s All About the Indentation

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')

# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  #x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x


##The else and elif Clauses
x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
    
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
    
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")
    
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")
    
name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")
    
    
if 'a' in 'bor':
    print('foo')
elif 1/0:
    print("This won't happen")
##elif var:
    print("This won't either")
    
##One-Line if Statements
x = 2

if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

##Python "while" Loops
n = 5
while n > 0:
    n -= 1
    print(n)
    

i = 1
while i < 6:
  print(i)
  i += 1
  
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

age = 10 
gender = 'M'

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')