
n = int(input())
r = int(input())

def factorial(number):
   if number < 1:   
       return 1
   else:
       return number * factorial( number - 1 )
nCr = factorial(n)/(factorial(r)*(factorial(n-r)))
print(nCr)

##this is my combinations calculator. getting factorial recursively. really ghetto imo but does the job i guess

