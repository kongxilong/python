#!/usr/bin/python3

#if  test
count = 1
if count > 1:
  print ("test 1")
elif count == 1 :
  print ("test 2")



#while loop test
while count < 3:
    print("now count = %d" % count)
    count += 1


#for loop test
print("I like to use internet for:")
for item in ['e-mail', 'net-surfing', 'homework']:
    print(item,)

print()

#range test

for eachNum in [0,1,2]:
    print(eachNum)

print('*'*4)
for eachNum in range(3):
    print(eachNum)

print('test for string','*'*4)

foo = 'abs'
for s in foo:
    print(s)

print('test of range and len')

for i in range(len(foo)):
    print (foo[i],'%d'%i)


squared = [x**2 for x in range(4)]
for i in squared:
     print(i)


def addMe2Me(x):
    'apply + operation to argument'
    return (x+x)


print(addMe2Me([2,'4']))







