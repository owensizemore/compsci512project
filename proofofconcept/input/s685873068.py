# -*- coding:utf-8 -*-

def main():
    l=input().split(" ")
    l.sort(reverse=True)
    print(int(l[0]),int(l[1]),int(l[2]),int(l[3]),int(l[4]))
        
if __name__ == '__main__':
    main()