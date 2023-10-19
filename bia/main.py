from texto.caracter import * 


n1= float (input ("Digite um número: "))
n2= float (input ("Digite outro número: "))

while True:
    menu = int (input("""
                1 - Somar
                2 - Diminuir
                3 - Multiplicar
                4 - Dividir
                0 - Sair
    """))
    if menu == 1:
        print (somar(n1,n2))
    elif menu == 2:
        print (diminuir(n1,n2) ) 
    elif menu ==3:
        print (multiplicar)   
    elif menu == 4:
        print (dividir)   
    elif menu == 0:
      break
    else:
        print ("Opção inválida")           