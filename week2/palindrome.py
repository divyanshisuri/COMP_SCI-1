n=int(input('Enter a number :'))
num=n
rev=0

while n>0:
    r=n%10
    rev=rev*10+r
    n//=10
print('Reverse of',num,'=',rev)
if rev==num:
    print(num,'is a palindrome number')
else :
    print(num,'is not a palindrome number')
#output
Enter a number :132
Reverse of 132 = 231
132 is not a palindrome numbe
________________________________________________________________________________
Enter a number :451
Reverse of 451 = 154
451 is not a palindrome number

Enter a number :12321
Reverse of 12321 = 12321
12321 is a palindrome number