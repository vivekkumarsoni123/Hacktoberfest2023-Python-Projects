def prime(n):
    for i in range(2,n//2 +1):
        if n%i==0:
            return(False)
    else:
        return(True)
a=int(input())
if prime(a):
    while a!=0:
        r=a%10;
        if prime(r):
            a=a//10
        else:
            print('not mega prime')
            break
    if a==0:
        print('mega prime')
else:
    print('not prime')
