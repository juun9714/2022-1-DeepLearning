two=1 #w2
one=1 #w1
zero=1 #w0

n_two=0 
n_one=0
n_zero=0


data=[(0,0),(1,1),(1,2),(2,1)]

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

for i in range(0,100000):
    n_two=two-(0.0001)*Ftwo(data,zero,one,two)
    n_one=one-(0.0001)*Fone(data,zero,one,two)
    n_zero=zero-(0.0001)*Fzero(data,zero,one,two)
    two=n_two
    one=n_one
    zero=n_zero

print("Result : ",n_two,"x^2 +", n_one,"x +", n_zero)
