import turtle as t 

import math as m 

import random as rn 

def star(r,c,x,y): 

 t.penup(); t.setpos(x,y); t.color(c); t.begin_fill(); t.circle(r); t.end_fill()

t.bgcolor("black"); t.speed(0)

for i in range(50):

 star(1,'white',rn.randint(-500,500),rn.randint(-500,500))

star(30,'red',0,-30)

t.shape('circle')

t.color('blue')

r=250

i=0

t1=t.Turtle() # 달을 표현하기 위해 펜(거북이) 추가

t1.speed(0); t1.shape('circle'); t1.color('yellow'); t1.penup()

r1=50

i1=0

while True: # 지구와 달의 공전을 표현하기 위해 무한 반복 

 x=m.cos(i)*r; y=m.sin(i)*r # 지구의 위치

 t.setpos(x,y)

 i=i+0.01

 x1=x + m.cos(i1)*r1; y1=y + m.sin(i1)*r1 # 태양을 중심으로 한 달의 위치 =

 t1.setpos(x1,y1) # (지구의 위치 + 지구를 중심으로 한 달의 위치) 

 i1=i1+0.12 
