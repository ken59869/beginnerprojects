
n = float(input())
r = float(input())

def factorial(number):
   if number < 1:   
       return 1
   else:
       return number * factorial( number - 1 )
nCr = factorial(n)/(factorial(r)*(factorial(n-r)))
print(int(nCr))

##this is my combinations calculator. getting factorial recursively. really ghetto imo but does the job i guess

