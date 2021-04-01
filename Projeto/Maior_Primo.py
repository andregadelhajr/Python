def maior_primo (x):
    maior_P = 0
    num = 1
    
    for i in range (2, x+1):

        mult=0
        num += 1
        for i in range(2, num):
            if (num % i == 0):
                mult += 1

                
        if(mult==0):
            if (maior_P == 0):
                maior_P = num
            elif (num > maior_P):
                maior_P = num

    print(maior_P)           


if __name__ == "__main__":
    maior_primo(46)