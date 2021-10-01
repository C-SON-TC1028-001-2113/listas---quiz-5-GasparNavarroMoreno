
def Diagonal_principal(Matriz):
    Diagonal = []
    for i in range(len(Matriz)):
        Diagonal.append(Matriz[i][i])
    return Diagonal

def crear_matriz(X,Y):
    Matriz = []
    if X == Y:
        for i in range(X):
            Matriz.append([])
            for j in range (Y):
                Matriz[i].append(int(input()))
    return Matriz

def main():
    X = int(input())
    Y = int(input())
    if X != Y:
        print("La matriz no es cuadrada")
    else:
        MATRIZ = crear_matriz(X,Y)
        print(Diagonal_principal(MATRIZ))

  
if __name__=='__main__':
    main()
