# Desenvolvedores: Renata Domingos Manso e Andre Gadelha junior

# Síntese
#  Objetivo: Um programa para auxiliar no controle de informação dos pacientes e UTI's da COVID-19no DF.
#  Entrada : Ler a quantidade de Hospitais, quantidade de UTI's,  nome da localidade/hospital, a
#            quantidade de pacientes da unidade, a classificação dos pacientes de acordo com o 
#            quadro de risco(Condição: Vermelho - paciente com quadro crítico, com sintomas graves,
#            necessidade de UTI; Laranja - paciente com quadro de sintomas menos comum que podem 
#            evoluir; Amarela - paciente com quadro de sintomas mais comum da COViD-19), a idade do 
#            paciente.
#  Saída   : Localidade do Hospital, quantidade de pacientes classificados de acordo com sua idade, 
#            quantidade de pacientes classficados pelo quadro de saúde de cade unidade, mostrando no 
#            final a quantidade de pacientes classificados como vermelho, depois aqueles da mesma 
#            classificação, mas que são idosos e crianças, o numero total de pacientes contabilizados,  
#            por fim mostrar a quantidade de UTI's para os pacientes de alto risco ou que a situação  
#            esta grave no Estado.


def main():
    imprime_mensagem_abertura()
    qtdeHospital=leValidaQtdeHospital()
    qtdeUTI=leValidaQtdeUTI()
    
    contQtdeTotalIdCr = 0
    contQtdeTotalVer = 0
    contQtdeTotal = 0
    contQtdeTotal_SobrandoUTI = qtdeUTI
    for i in range (1, qtdeHospital+1, 1):
        localidade=leValidaNomeLocalidade()
        qtdePacientes=leValidaQtdePacientes()
        
        contCrianca = 0
        contAdolecente = 0
        contAdulto = 0
        contIdoso = 0
        contVermelho = 0
        contLaranja = 0
        contAmarelo = 0
        for i in range (1, qtdePacientes+1, 1):
            classificacao=leValidaClassificacao()
            idade=leValidaIdade()

            if(idade<13):
                contCrianca = contCrianca+1
            elif(idade>=13 and idade<=17):
                contAdolecente = contAdolecente+1
            elif(idade>=18 and idade<=64):
                contAdulto = contAdulto+1
            else:
                contIdoso = contIdoso+1

            contQtdeTotal = contQtdeTotal+1
            
            if(classificacao==1):
                contVermelho = contVermelho+1
                contQtdeTotalVer = contQtdeTotalVer+1
                contQtdeTotal_SobrandoUTI = contQtdeTotal_SobrandoUTI-1
                if(idade<13 or idade>64):
                    contQtdeTotalIdCr = contQtdeTotalIdCr+1
            elif(classificacao==2):
                contLaranja = contLaranja+1
            elif(classificacao==3):
                contAmarelo = contAmarelo+1

        exibeQuantidadeAtendimento(contCrianca, contAdolecente, contAdulto, contIdoso, localidade)
        exibeQuantidadeClassificacaoRisco(contVermelho, contLaranja, contAmarelo)

    apresentaQuantidadeTotalAtendimento(contQtdeTotalVer, contQtdeTotalIdCr, contQtdeTotal, contQtdeTotal_SobrandoUTI)



def imprime_mensagem_abertura():
    print("**********************************************************************")
    print("*****Bem Vindo ao Sistema de Redes de Hospitais da COVID-19 do DF*****")
    print("**********************************************************************\n\n")

def leValidaQtdeHospital():
    print("\n             Digite Informações das redes de Hospitais")
    print("======================================================================")
    while True:
        qtdeHospital=int(input("Digite a quantidade de Hospitais da rede do DF: "))
        if (qtdeHospital >0):
            print("======================================================================\n")
            break
    return qtdeHospital

def leValidaQtdeUTI():
    print("======================================================================")
    while True:
        qtdeUTI=int(input("Digite a quantidade total de UTI's em todo DF: "))
        if (qtdeUTI >=0):
            print("======================================================================\n")
            break
    return qtdeUTI

def leValidaNomeLocalidade():
    print("======================================================================")
    while True:
        localidade=input("Digite o nome da localidade ou hospital de campanha: ") 
        if (localidade.isidentifier()):
            break      
    return localidade

def leValidaQtdePacientes():
    while True:
        qtdePacientes=int(input("Digite a quantidade de pacientes com COVID-19: "))
        if (qtdePacientes>0):
            print("======================================================================\n")
            break
    return qtdePacientes

def leValidaClassificacao():
    print("======================================================================")
    while True:
        print("Escolha a classificação do quadro de risco da COVID-19:")
        print("1 - vermelho")
        print("2 - laranja")
        print("3 - amarelo")
        classificacao=int(input("Opção: "))
        if (classificacao==1 or classificacao==2 or classificacao==3):
            break
    return classificacao
    
def leValidaIdade():
    while True:
        idade=int(input("Digite a idade do paciente: "))
        if(idade>=0):
            print("======================================================================\n")
            break
    return idade


def exibeQuantidadeAtendimento(contCrianca, contAdolecente, contAdulto, contIdoso, localidade):
    print("\n                    Informações Hospital")
    print("======================================================================")
    print("Localidade do Hospital é: {}".format(localidade))
    print("Quantidade de crianças = {}".format(contCrianca))
    print("Quantidade de adolescentes = {}".format(contAdolecente))
    print("Quantidade de adultos = {}".format(contAdulto))
    print("Quantidade de idosos = {}".format(contIdoso))
    print("======================================================================\n")

def exibeQuantidadeClassificacaoRisco(contVermelho, contLaranja, contAmarelo):
    print("======================================================================")
    print("Quantidade com classificação vermelho =  {}".format(contVermelho))
    print("Quantidade com classificação laranja =  {}".format(contLaranja))
    print("Quantidade com classificação amarelo =  {}".format(contAmarelo))
    print("======================================================================\n")
    
def apresentaQuantidadeTotalAtendimento(contQtdeTotalVer, contQtdeTotalIdCr, contQtdeTotal, contQtdeTotal_SobrandoUTI):
    print("\n\n\n                                       Quantidade Total Atendimento e UTI's na Rede Hospitalar do DF")
    print("============================================================================================================================================================================")
    print("A quantidade total de pacientes de todos os Hospitais presentes na pesquisa com COVID-19 do DF foi de: {}".format(contQtdeTotal))
    print("A quantidade total de pacientes crianças e idosos que tiveram classificação de risco vermelho de todos os Hospitais presentes na pesquisa sobre COVID-19 foi de: {}".format(contQtdeTotalIdCr))
    print("A quantidade total de pacientes que tiveram classificação de quadro de risco vermelho de todos os Hospitais presentes na pesquisa da COVID-19 foi de: {}".format(contQtdeTotalVer))
    if(contQtdeTotal_SobrandoUTI > 0):
        print("A quantidade total de UTI's de todos as redes de Hospitais que estão disponiveis para pacientes com maior complicações pela COVID-19, presentes na pesquisa foi de: {}".format(contQtdeTotal_SobrandoUTI))
        print("========================================================================================================================================================================\n\n")
    else:
        print("Infelizmente a rede não tem mais UTI's disponiveis, Decreta medidas de restrição para controlar os casos da COVID-19")
        print("========================================================================================================================================================================\n\n")

        

if __name__ == "__main__":
    main()
