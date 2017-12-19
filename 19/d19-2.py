#!/usr/bin/env python3

from sys import argv

filename=argv[1]
dir='s'
letters = []
steps=0

with open(filename) as f:
    input = f.readlines()
x=input[0].index('|')
y=0

def turnlr():
    global dir
    if x>0 and input[y][x-1] not in ['|', ' ']:
        dir='w'
    elif x<len(input[y])-1 and input[y][x+1] not in ['|', ' ']:
        dir='e'

def turnsn():
    global dir
    if y>0 and input[y-1][x] not in ['-', ' ']:
        dir='n'
    elif y<len(input)-1 and input[y+1][x] not in ['-', ' ']:
        dir='s'
        
while True:
    if x<0 or y<0 or x>=len(input[y]) or y>=len(input) or input[y][x]==' ':
        break
    if input[y][x]=='+':
        if dir=='n' and (y==0 or (y>0 and input[y-1][x] in ['-',' '])):
            turnlr()
        elif dir=='s' and (y>=len(input)-1 or (y<len(input)-1 and input[y+1][x] in ['-',' '])):
            turnlr()
        elif dir=='e' and (x>=len(input[y])-1 or (x<len(input[y])-1 and input[y][x+1] in ['|',' '])):
            turnsn()
        elif dir=='w' and (x==0 or (x>0 and input[y][x-1] in ['|',' '])):
            turnsn()
        else:
            break
    elif input[y][x] not in ['+','-','|']:
        letters.append(input[y][x])
    if dir=='n':
        y-=1
        steps+=1
    if dir=='e':
        x+=1
        steps+=1
    if dir=='s':
        y+=1
        steps+=1
    if dir=='w':
        x-=1
        steps+=1
print("Answer:",steps)
