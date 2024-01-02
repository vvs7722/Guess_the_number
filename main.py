import random
import os,time
ls=[]
def fun3():
    global a
    a=random.randint(0,100)
    global i
    global c
    i=0
    c='nn'
aa='''GUESS THE NUMBER
THE RANGE OF THE NUMBER IS IN BETWEEN 0 AND 100
YOU HAVE ONLY 5 CHANCES TO GUESS THE NUMBER
IF YOUR CHOICE IS GREATER THAN THE NUMBER THEN THE COMPUTER SHOWS GREATER
IF YOUR CHOICE IS LESSER THAN THE NUMBER THEN THE COMPUTER SHOWS LESSER
THE GAME STARTS NOW'''
print(aa)
def fun4():
    if c=='nn':
        print('YOU LOST')
        fun2()
#For revaling the answer for 0.25seconds
def reveal():
    global ls
    global i
    ls=ls[:len(ls)-1]
    print(aa)
    for k in ls:
        print(f"NUMBER:{k}")
        check(k)
    i-=1

def check(b):
    global i
    if b==1234:
        print(a)
        time.sleep(0.25)
        os.system('cls')
        reveal()
    elif b<a:
        print('YOUR CHOICE IS LESSER')
    elif b>a:
        print('YOUR CHOICE IS GREATER')
    elif b==a:
        print('YOU WON')
        i+=99
        global c
        c=''
        fun2()
    else:
        print('INVALID CHOICE')

def fun():
    global i
    i+=1
    b=int(input('NUMBER:'))
    ls.append(b)
    check(b)
    
def fun1():
    while i<5:
        fun()
    if i==5:
        fun4()
def fun2():
    global ls
    print(a,'IS THE CORRECT ANSWER')
    print('CLICK 1 TO EXIT')
    print('CLICK ANY KEY TO PLAY AGAIN')
    l=input()
    if l!='1':
        i=0
        os.system('cls')
        print(aa)
        ls=[]
        fun3()
        fun1()
    else:
        print('OK')
        exit()
fun3()
fun1()
