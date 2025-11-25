'''
Created on Mar 22, 2013

@author: wukc
'''

from sys import stdin

a=map(int,stdin.readline().split())
a.sort()
print(" ".join(a[::-1]))