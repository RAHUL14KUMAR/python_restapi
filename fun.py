def sum(a,b):
    return a+b

def avg(a,b):
    return (a+b)/2

def armstrong(n):
    # n=int(input("Enter the number\n"))
    sum=0
    order=len(str(n))
    copy_n=n
    while n>0:
        digit=n%10
        sum=sum+digit**order
        n=n//10
    if(copy_n==sum):
        print("Armstrong")
        return True
    else:
        print("Not Armstrong")
        return False
    
def greet(name):
    return "Hello",name