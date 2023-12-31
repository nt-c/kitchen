from collections import deque
from bisect import bisect_left as bs
from itertools import permutations
import sys, math
import heapq as hq

# sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = float('inf')

n = 1
transports = {54:19, 90:48, 99:77, 9:34, 40:64, 67:86}
msg = ''
while True:
    roll = int(input())
    if n+roll<=100:
        n+=roll
    if n in transports:
        n = transports[n]
    if roll==0:
        msg+='You Quit!\n'
        break
    else:
        msg+='You are now on square '+str(n)+'\n'
    if n==100:
        msg+='You Win!\n'
        break
print(msg)