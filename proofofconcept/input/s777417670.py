#!/usr/bin/python


def datasets():
    s = raw_input().strip()
    yield [int(w) for w in s.split()]
    
def main():
    for ds in datasets():
        print ' '.join([str(n) for n in sorted(ds, reverse=True)])
        
if __name__ == '__main__':
    main()