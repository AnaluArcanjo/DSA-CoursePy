# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 

print("\n******************* Calculadora em Python *******************")

def soma(x, y):
    return int(x + y)
    
def sub (x, y):
    return x - y

def mult (x, y):
    return x * y

def div (x, y):
    if y == 0:
        return "erro: divisão por 0 não existe!"
    return x / y


def voltar_menu ():
    input( '\n Digite qualquer tecla para voltar ao menu \n ')
    main()


def exibir_opcoes():
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')    
    # print('5. Sair do programa')
    
    try: 
        operacao = int(input('\n Selecione o tipo de operação para realizar na Calculadora:'))

        if operacao == 1:        
            s1 = int(input('\n Digite o primeiro valor da operação Soma: '))
            s2 = int(input(' Digite o segundo valor da operação Soma: '))

            print('\n %s + %r ='  %(s1, s2), soma(s1, s2))

        elif operacao == 2:
            m1 = int(input('\n Digite o primeiro valor da operação Subtração: '))
            m2 = int(input(' Digite o segundo valor da operação Subtração: '))

            print('\n %s - %r ='  %(m1, m2), sub(m1, m2))

        elif operacao == 3:
            v1 = int(input('\n Digite o primeiro valor da operação Multiplicação: '))
            v2 = int(input(' Digite o segundo valor da operação Multiplicação: '))

            print('\n %s * %r ='  %(v1, v2), mult(v1, v2))

        elif operacao == 4:
            d1 = int(input('\n Digite o primeiro valor da operação Divisão: '))
            d2 = int(input(' Digite o segundo valor da operação Dvisão: '))

            print('\n %s / %r ='  %(d1, d2), div(d1, d2))

        else:
            print('Opção Inválida. Tente novamente!!')
            
    except ValueError:
        print("\n -------- deu erro -------- ")
        voltar_menu()



def main():
    exibir_opcoes()

if __name__ == '__main__':
    main()
