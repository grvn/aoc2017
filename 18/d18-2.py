#!/usr/bin/env python3

from sys import argv
from threading import Thread
from queue import Queue
from collections import defaultdict

filename=argv[1]
reg0=defaultdict(lambda:0)
reg1=defaultdict(lambda:0)
reg1['p']=1 # reg0 är autofixad
pos0=0
pos1=0
to0=Queue()
to1=Queue()

with open(filename) as f:
    input = f.readlines()
    input = [line.split() for line in input]

def exec(reg, val):
    try:
        int(val)
        return int(val)
    except ValueError:
        return reg[val]
    
def worker(id,reg,pos,to,fro):
    co=0
    while True:
        ins = input[pos]
        if ins[1] not in reg:
            reg[ins[1]]=0
        if ins[0]=='set':
            reg[ins[1]]=exec(reg,ins[2])
        elif ins[0]=='add':
            reg[ins[1]]+=exec(reg,ins[2])
        elif ins[0]=='mul':
            reg[ins[1]]*=exec(reg,ins[2])
        elif ins[0]=='mod':
            reg[ins[1]]%=exec(reg,ins[2])
        elif ins[0]=='snd':
            to.put(exec(reg,ins[1]))
            co+=1
        elif ins[0]=='rcv':
            try:
                reg[ins[1]]=fro.get(True,1)
            except:
                print("Thread",id,":",co)
                return
        elif ins[0]=='jgz':
            if exec(reg,ins[1]) > 0:
                pos+=exec(reg,ins[2])
                continue
        pos+=1


t0=Thread(target=worker, args=(0,reg0,pos0,to0,to1))
t1=Thread(target=worker, args=(1,reg1,pos1,to1,to0))
t0.start()
t1.start()
t0.join()
t1.join()
