def leValidaClassificacao():
    while True:
        qtdeUpas=int(input("Digite a quantidade de UPAS: "))
        if (qtdeUpas >0):
            break
    return qtdeUpas
    
def leValidaLocalidade():
    while True:
        localidade=input("Digite o nome da localidade: ")
        if (localidade.isidentifier()):
            break
    return localidade
    

def main():
    qtdeUpas=leValidaClassificacao()
    for i in range (1, qtdeUpas+1, 1):
        localidade=leValidaLocalidade()
        print("qtdeupas: ", qtdeUpas)
        print("local: ", localidade)



if __name__ == "__main__":
    main()


