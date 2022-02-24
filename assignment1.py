two=1
one=1
zero=1

n_two=0
n_one=0
n_zero=0


data=[(0,0),(1,1),(1,2),(2,1)]
# gt : 에러함수를 각 가중치로 미분한 값 (근데 모든 합인 에러함수를 미분한게 아니라, 각 data에 따라 미분해서 합한 것임) 
# => 미분한 일반식을 구해서 데이터를 넣어서 그걸 다 합친 것임
# => 근데 미분한 일반식이 w에 따라서 달라짐 
#t에 따라서 w가 계속 바뀌는데, gt도 t에 따른 w에 따라서 계속 x값을 대입해서 바뀌는 식임, w에 따라서 x값은 고정 
# 고정된 x값은 data를 통해서 제공하고, zero, one, two는 계속 바뀜


def Fzero(data, zero, one, two):
    #gt0
    #8w0
    sum=0
    for i in range(4):
        sum+=-2*(data[i][1]-(two*(data[i][0]**2)) - one*(data[i][0]) - zero) #-2*(y-f(x;w))
        
    return sum


def Fone(data, zero, one, two):
    #gt1
    sum=0
    for i in range(4):
        sum+=-2*(data[i][1]-(two*(data[i][0]**2)) - one*(data[i][0]) - zero)*data[i][0] #-2*(y-f(x;w))*x
    
    return sum

def Ftwo(data, zero, one, two):
    #gt2
    sum=0
    for i in range(4):
        sum+=-2*(data[i][1]-(two*(data[i][0]**2)) - one*(data[i][0]) - zero)*(data[i][0]**2) #-2*(y-f(x;w))*x^2
    
    return sum

print("Fzero",Fzero(data,zero,one,two))
print("Fone",Fone(data,zero,one,two))
print("Ftwo",Ftwo(data,zero,one,two))

for i in range(0,100000):
    # print("before : ",zero, one, two)
    
    n_two=two-(0.0001)*Ftwo(data,zero,one,two)
    n_one=one-(0.0001)*Fone(data,zero,one,two)
    n_zero=zero-(0.0001)*Fzero(data,zero,one,two)
    two=n_two
    one=n_one
    zero=n_zero

print("after : ",n_two,"x^2 + ", n_one,"x + ", n_zero)
