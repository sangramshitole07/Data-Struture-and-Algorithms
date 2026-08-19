def Count_digits(n):
    cnt=0
    while n>0:
        cnt=cnt+1
        n=n//10
    return cnt

if __name__=="__main__":
    n=329823
    print("N : ",n)
    digits=Count_digits(n)
    print("Number of Digits are : " , digits)