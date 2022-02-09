#1
for x in range(0,151,1):
    print(x)

#2
for x in range(5,1005,5):
    print(x)

#3
def thedojo():
    for x in range(1,101):
        if x % 10 == 0:
            print('Coding Dojo')
        elif x % 5 == 0:
            print('Coding')
        else:
            print(x)
thedojo()

#4
total=0 
for x in range (0,500000):
    if x % 2 != 0:
        total += x
print(total)

#5
for x in range (2018,0,-4):
    if x % 2 ==0:
        print(x)

#6

def flex_counter(lowNum,highNum,mult):
    for x in range (lowNum,highNum,mult):
        if x % mult ==0:
            print(x)
flex_counter(2,12,2)

