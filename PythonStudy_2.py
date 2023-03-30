#!/usr/bin/env python
# coding: utf-8

# ### 복사호출, 참조호출, 할당호출
# #### 복사호출과 참조호출
# - 복사호출 (Call-by-Value) : 변수의 값을 리턴
# - 참조호출 (Call-by-Reference) : 변수의 레퍼런스(식별자, 포인터, 주소 등)를 리턴
# 
# #### 할당호출 : 파이썬은 함수의 파라미터가 불변타입이면 복사호출 / 가변타입이면 참조호출
# - 함수의 파라미터가 불변 타입이면 값 복사, 가변 타입이면 레퍼런스 복사
# 

# In[3]:


def twofold1(a):
    a=2*a
def twofold2(a):
    a=2*a
    return a
x=5
twofold1(x)
print(x)

x=5
x=twofold2(x)
print(x)

def sample(a:int,b):
    a=2*a
    b.append('test')
    
x=5
y=[1,2]
sample(x,y)
print(x)
print(y)


# In[4]:


# 클래스
# 파이썬은 객체지향언어, 클래스는 객체지향언어의 '객체'를 만드는 수단
#  -> 생성자(constructor) : 해당 클래스의 객체가 하나 만들어질 때 자동으로 수행되어 객체를 초기화하는 특별한 메서드
#  -> 메서드(method) : 클래스 안에서 정의된 함수
class Sample:
    def __init__(self):
        self.counter=0
    def numEven(self, n):               # self가 매개변수로 지정되어야 함
        for k in range(n):
            if k % 2 == 0:
                self.counter += 1
        return self.counter             # self.counter 값이 리턴되어야 함
s = Sample()
print('# of enen integers =', s.numEven(15))


# In[6]:


# self.counter는 각 객체마다 존재
# counter2(또는 Sample.counter2) 는 해당 클래스 모든 개게를 통틀어 하나만 존재
class Sample:
    counter2=0
    def __init__(self):
        self.counter=0
    def numEven(self, n):              
        for k in range(n):
            if k % 2 == 0:
                self.counter += 1
                Sample.counter2 += 1
        return self.counter    
s1=Sample()
s2=Sample()
s1.numEven(15)
s2.numEven(15)
print(s1.counter, s1.counter2, Sample.counter2)


# In[7]:


# private method : 클래스 내부에서만 사용되며, 클래스 밖에서는 사용할 수 없는 메서드. (ex) __counter


# In[8]:


# 순회 가능 클래스 (Itarable Class)
#  -> 순회 가능 클래스 : 순회자(iterator)를 제공하는 클래스
#  -> 사용자가 직접 순회자를 만들어 클래스에 포함한 것
# "for x in 객체A" : 'x in 객체A' 가 True 가 되는 모든 x 에 대하여로 해석
#  -> in은 차례대로 훑을 수 있는 (순회 가능한) 대상으로부터 하나씩 훑어가는 역할을 한다
# 모든 순회 가능 클래스는 내부에 순회자를 가지고 있다
#  -> 순회자는 클래스와 외부의 연결을 부드럽게 해주는 고급 기능인 '디자인 패턴'의 하나
#  -> 순회자는 두 메서드 __iter__() 와 __next__() 로 구성

print('s' in 'east') # keyword 'in' : 'east'에 's' 가 있으면 True 값을 리턴
print(77 in [10,20,35,50])

for element in 'east': # 문자열 'east' 를 차례로 훑으면서 element에 할당
    print(element, end='-')
print()

for x in [0,1,2,3]: # 리스트 [0,1,2,3] 의 모든 원소를 차례로 변수 x에 할당
    print(x,end=' ')


# In[12]:


class L:
    def __init__(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
    def insert(self, i, newItem):
        ...
    def append(self, newItem):
        ...
    def __iter__(self):
        return Literator(self) # 순회자를 가동시키기 위해 수행되는 메서드 
class Literator: # 순회 가능한 객체로 만들기 위한 클래스 Literator
    def __init__(self, alist):
        self.iterPosition = alist.getNode(0)
    def __next__(self):
        if self.iterPosition == None:
            raise StopIteration
        item = self.iterPosition.item
        self.iterPosition = self.iterPosition.next
        return item


# In[11]:


# 순회자 사용 전
def count(self,x) -> int:
    cnt = 0
    curr = self.__head.next
    while curr != None:
        if curr.item == x:
            cnt += 1
        curr = curr.next
    return cnt
# 순회자 사용 후
def count(self, x) -> int:
    cnt = 0
    for a in self:
        if a == x:
            cnt += 1
    return cnt


# In[14]:


# 정의코드와 수행코드
class Heap:
    def __init__(...):
        ...
    def isEmpty(...):
        ...
    def insert(...):
        ... # 클래스의 정의만 있고 이를 사용하는 문장이 없음 -> 다른 파일(*.py)에서 사용하는 목적으로만 쓰임
class Test:
    def __init__(...):
        ...
    def isEmpty(...):
        ...
    print('클래스 내부 테스트') # 클래스 Test를 해석하는 과정에서 그냥 수행
    
    def insert(...):
        print('매서드 내부 테스트') # 클래스 Test를 해석하는 과정에서는 수행되지 않으며 메서드를 사용하면서 수행
        ...
        
print('클래스 외부 테스트') # sample.py 를 해석하는 과정에서 그냥 수행


# In[15]:


# 모듈로의 접근
from heap import *
from DS.list.test import *


# In[ ]:




