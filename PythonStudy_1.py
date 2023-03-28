#!/usr/bin/env python
# coding: utf-8

# ### 연걸 리스트 클래스 구조 (linkedListBasic.py)

# In[1]:


print('Hello, World!')


# In[1]:


# print() 프린트 -> 작성한 프로그램이 제대로 돌아가는지 확인하는 방법
# sep='' 프린트 하는 원소간 구분 (기본값 : 공백)
# end='' 프린트 후 종료조건 (기본값 : 줄바꿈)
print('Hello!',end='\n')

x= 77
print('x is', x, "th",end='\n')
print("My","name","is","Lee",sep = '*')


# In[2]:


# 수의 처리
# 변수 타입 ( 동적 타이핑 )
# 대부분 다른 언어 -> 변수 타입 정해져 있음
# 파이썬은 변수에 수가 저장되는 순간 타입이 결정
# 타입 캐스팅 : 파이썬에서 더 중요
# 연산자 : 사칙연산 + - * /
# 기타연산 : //, %, **
x=5 # 정수
y= 10.5 # 실수
z=x+y # 실수
print('z is', z)

a = (int)(x+y) # type casting 을 통해 정수로 변환
print('a is', a)

x=(20+30) % 10 # 10으로 나눈 나머지
print(x)

print(20/3) # 실수 나눗셈 (나눗셈)
print(20//3) # 정수 나눗셈 (몫)


# In[3]:


# 문자열
# '', "", ''' ''' 로 문자열 감싸줌
# 이미 사용한 문자열 구분 기호와 다른 형태를 사용하면 됨 ( '가 사용됐으면 "사용하기 )
# ',",\ -> \',\",\\

list = ['lion', 'in', 'oil']
print(list)

print("5's element")
print('5"s element')
print(''' 5's element ''')
print("4\'s element \\ 6\"s element")


# In[6]:


# 제어
# 루프를 돌거나 분기를 통해 흐름 제어
# 반복 제어문 : for, while
# 순회 대상 함수 range(n): n보다 작은 수까지 루프 수행
# 조건 분기 : if, if-else, if-elif-else, switch(X)

sum=0
A=[0,1,2,3,4,5]
N=6
for i in range(3,N): # 시작 : 3, 끝 : 6-1=5, 간격 : 1
    sum += A[i]
print(sum)

sum = 0; i=3
while i<= N-1:
    sum += A[i]
    i += 1
print(sum)

N=100;
K=200;
print("Enter i")
i = int(input())
if i < N:
    print(i, "is less than ", N)
else:
    print(i, "is not let than", N)
    
if i < N:
    print("i <", N)
elif i < K :
    print(N, "<= i <", K)
else:
    print(k, "<= i")


# In[7]:


# 제어
# for 루프에서 순회 대상 함수 range(n) : n 보다 작은 수까지 루프 수행
for i in range(10) :
    print(i,end=' ') # 시작 1, 끝 10-1 = 9, 간격 1
print()
for i in range(4,10,2): # 시작 4, 끝 9, 간격 2
    print(i,end=' ')
print()
for i in range(10,4,-2): # 시작 10, 끝 4+1=5, 간격 -2
    print(i, end=' ')


# In[ ]:


# 제어
# 리스트, 튜플, 딕셔너리, 집합 => 순회대상

print('List 1') # 리스트 1
for i in [0,1,2,3]:
    print(i,end=' ')
print(), print('\nList 2') # 리스트 2
s = [4,5,6]
for i in s :
    print(i, end=' ')
print(), print('\nDictionary') # 딕셔너리
d = {1:10, 2:20, 3:30, 10:40}
for i in d:
    print(i, ';', d[i], end=' ') 
print(), print('\nSet') # 집합
for i in {1,2,3,10}:
    print(i, end=' ')
    
print(), print('\nString') # 문자열
for i in 'testseq':
    print(i,end='-')

