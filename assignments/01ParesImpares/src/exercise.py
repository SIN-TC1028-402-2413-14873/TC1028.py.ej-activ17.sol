def main():
    #escribe tu código abajo de esta línea
    l=[]

    dato='+'
    
    while dato != '*':
        dato = input("Dame el Numero (*=Fin):")

        if dato != '*':
            l.append(int(dato))

    cp=0
    ci=0

    for i in range(len(l)):
        if l[i] % 2 == 0:
            cp = cp + 1
        else:
            ci = ci + 1

    print(f"PARES={cp}")
    print(f"IMPARES={ci}")


if __name__=='__main__':
    main()
