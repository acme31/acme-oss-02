import random
listran=[]
r = str(random.randint(0, 9)) 
listran.append(r)
while len(listran)!=3:
    while r in listran :
        r = str(random.randint(0, 9)) 
    listran.append(r)
stringran=''.join(listran)
num="0" 
s=0 
b=0 
turn=0 
i=0 
while num!=stringran: 
    num=input("숫자:") 
    if num=="포기":
        print("답: ",stringran)
        print("종료")
        break
    list_n=list(num) 
    for i in range(0,3): 
        if list_n[i]==listran[i]: 
            s+=1 
        elif list_n[i] in listran:
            b+=1
    turn+=1 
    print(s,"스트라이크", b,"볼")
    s=0
    b=0
print("정답",turn)
