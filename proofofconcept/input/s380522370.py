# -*- coding:utf-8 -*-

def main():
    LIST=input().split()
    LIST.sort(reverse=True)
    map(int(),LIST)
    print("{0} {1} {2} {3} {4}".format(LIST[0],LIST[1],LIST[2],LIST[3],LIST[4]))
        
if __name__ == '__main__':
    main()