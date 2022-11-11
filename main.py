# Print the First 3 multiples of the number with single spaces between them as an output.
'''
A = int(input())
B = A*1, A*2, A*3
print(*B, sep=' ')
'''
import pandas as pd

# Find the cube of the number.
'''
A = int(input())
B = A**3
print(B)
'''
# Print the factorial of the integer.
'''
A = int(input())
B = 1
for i in range(1, A + 1):
     B = B*i
print(B)'''

# The days in the month corresponding to the input number
'''
month =int(input())
if(month==2) :
    print("Number of days is 28");
elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    print("31");
elif(month==4 or month==6 or month==9 or month==11 ) :
    print("30");
else:
    print("Error");
'''
# Nine tables
'''
N = int(input())
if N <= 0:
    print('NULL')
else:
    for i in range(1, N + 1):
        B = 9 * i 
        print(B, end=" ")
'''
# Reverse the string
'''
A = input()
print(A[:: -1])
'''

# SUm of digits
'''
num = input()
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)'''

# Print the HCF of the integer
'''
A, B = map(int, input().split())
hcf = 1
for i in range(1, min(A+1, B+1)):
    if A % i == 0 and B % i == 0:
        hcf = i
print(hcf)
'''
# Print the even and odd integers of the integer in a separate line
# To convert the given integer to a collection
'''
B = input()
A = tuple(map(int, str(B)))
even = [i for i in A if i % 2 == 0]
odd = [i for i in A if i % 2 != 0]
print(*sorted(even))# to arrange the similar numbers together (eg 2 2 3)
print(*sorted(odd))'''

# prime or complex number
'''
A = int(input())
if A > 1:
    for i in range(2, int(A)+1):
        if (A % i) == 0:
            print("yes")
            break
    else:
        print("No")'''

# With in the range
'''
lower, upper = map(int, input().split())
A = []
for num in range(lower, upper+1):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            A.append(num)
print(len(A))
'''

# The rules of rock paper scissors:
# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.
'''
A, B = map(str, input().split())
if A == "S" and B == "P":
    print("S")
elif A == "S" and B == "R":
    print("R")
elif A == "P" and B == "R":
    print("P")
elif B == "S" and A == "P":
    print("S")
elif B == "S" and A == "R":
    print("R")
elif B == "P" and A == "R":
    print("P")
else:
    print("D")
'''

# Given a string S consisting of 2 words reverse the order of two words .
'''
S = input().split()
S.reverse()
print(' '.join(S))'''

# .Find the smallest number and largest number
'''
k = int(input())
a = list(map(int, input().split()))
for i in range(1, k):
    A = a.index(min(a))
    B = a.index(max(a))
print(A+1, B+1)'''

# print the number of repetition of K
'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))
if n == len(arr):
    for i in range(1, k):
        if arr[i] == k:
            A = arr.count(k)
            print(A-1)
        else:
            print("-1")
            break
'''
# find the Bitwise AND of the array elements.
'''
n = int(input())
arr = list(map(int, input().split()))
ans = arr[0]  # Initialise ans variable is arr[0]
for i in range(1, n):
    ans = ans & arr[i]  # Traverse the array compute AND
print(ans)'''

# Given an array of N elements switch(swap) the element with the adjacent element and print the output.
'''
n = int(input())
l = list(map(int, input().split()))
i = 0
while i < n - 1:
    if n == len(l):
        l[i], l[i + 1] = l[i + 1], l[i]

    i += 2
print(*l)'''

# Given a string 'S' swap
'''
n = input()
s = list(n)
for i in range(0, len(s)-1, 2):
    s[i], s[i+1] = s[i+1], s[i]

result = ''.join(s)
print(result)'''

# list comprehension
'''a = [1, 2, 3, 4, 5, 6, 7, 8]
b = ["low" if i < 3 else "High" if i > 6 else "medium" for i in a]
print(b)'''

# lambda
'''
W = [90, 87, 76, 67, 98]
H = [1.34, 1.5, 1.7, 1.8, 1.9]
b = list(map(lambda W,H: W/H**2, weight,height))
print(b)
'''

# Addition without carry
'''A, B = map(int, input().split())
ans = (A % 10) + (B % 10)
print(ans)'''

# Print the smallest perfect power of 2 greater than n.
'''n = int(input())
for i in range(0, n):
    if (n % i) == 0:
        print(n)
else:
        print("-1")'''

'''N, k = map(int, input().split())
arr = list(map(int, input().split()))
A = sorted(arr)
print(A)
for i in range(0, N):
    if N == len(arr):
        B = arr[k - 1]
        print(arr)
    else:
        print("-1")'''

# Series addition
'''def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
'''
# The encryption can be represented using modular arithmetic by first transforming the letters into numbers,
# according to the scheme, A = 0, B = 1,…, Z = 25.
# Encryption of a letter by a shift n can be described mathematically as.
# (Encryption Phase with shift n) = E_n(x)=(x+n)mod\ 26
# (Decryption Phase with shift n) = D_n(x)=(x-n)mod\ 26
# Algorithm:
# Extract the ASCII value of the character
# Subtract  65(for Upper-case letter) or 97 (for lower-case letter)
# Add shift value
# Perform modulo operation
# Add 65 or 97
'''S, A = map(str, input().split())
M = int(A)
output = ""

for i in range(len(S)):
    char = S[i]
    if char.isupper():
        output += chr((ord(char) + M - 65) % 26 + 65)  # ASCII value of upper-case letters starts from 65
        # Encrypt lowercase characters
    else:
        output += chr((ord(char) + M - 97) % 26 + 97)  # ASCII value of lower-case letters starts from 97

print(output)'''

# Print the smallest perfect power of 2 greater than n.
'''
n = int(input())


def highestPowerof2(n):
    count = 0
    for i in range(n, 0, -1):
        if i & (i - 1) == 0:  # to find the exact power of 2 in a number
            count = i
            break
    return count


print(highestPowerof2(n*2))     # to print next power of 2
'''

# To find co prime:
'''
n, m = map(int, input().split())

for i in range(1, min(n+1, m+1)):
    if n != 0:
        n, m = n, n % m
        print("Co prime")
        break
    else:
        print("0")
        break
'''
'''
import pandas as pd

df = pd.read_csv("C:\\Users\\Dell\\OneDrive\\Desktop\\insurance.csv")
A = pd.crosstab(df["sex"], df["children"])
print(A)
'''

