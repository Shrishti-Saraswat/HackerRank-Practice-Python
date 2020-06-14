if __name__ == '__main__':
    n = int(input())
    li=list(map(int,input().strip().split()))
    li1=set(li)
    li1.remove(max(li1))

    print(max(li1))       
