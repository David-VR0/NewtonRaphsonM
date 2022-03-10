def derivada1(matriz,n):
    listad1=[]
    for i in range(0,n):
        x=matriz[i]*(n-i)
        listad1.append(x)
    #print(listad1)
    b=derivada2(listad1,n-1)

    return listad1,b

def derivada2(matriz, n):
    listad2 = []
    for i in range(0,n):
        x=matriz[i]*(n-i)
        listad2.append(x)
    #print(listad2)
    return listad2

def operacion(d1,d2,m,xi,n):
    x=0
    m1=[]
    m1.append(m)
    m1.append(d1)
    m1.append(d2)
    suma=[]
    t=0
    while(n!=0 ):
        while(t!=3):
            for i in range(0, n + 1):
                if n - i != 0:
                    x = x + m1[t][i] * (pow(xi, n - i))
                else:
                    x = x + m1[t][i]

            suma.append(x)
            x = 0
            n = n - 1
            t = t + 1
            if t == 3:
                n = 0
    r=xi-(suma[0]*suma[1])/(pow(suma[1],2)-suma[0]*suma[2])

    return r
def error(r,t):
    e=abs((r-t)/r)*100
    return e

def resolver(matriz,n,xi):
    listad1,listad2 = derivada1(matriz,n)
    e=100
    j=0
    lista=[[j,xi,e]]
    while(e>0.9):
        m=[]
        r = operacion(listad1, listad2, matriz, xi, n)
        # print(r)
        e = error(r, xi)
        xi = round(r, 6)
        print("Iteraccion :",j)
        print("Error :")
        print(round(e,3),"%")
        print("xi : ")
        print(xi)
        j=j+1
        m=[j,xi,str(round(e,4))+"%"]
        lista.append(m)

    print(lista)
    return lista