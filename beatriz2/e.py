# class Carro:
#     def __init__(self,marca,ano,modelo,tem_4_portas):
#      self.marca = marca
#      self.ano= ano
#      self.modelo = modelo
#      self.tem_4_portas = tem_4_portas

# carro1 = Carro("Ford", 2021, "Ka", True)
# carro2 = Carro ("Fiat", 2007, "Uno", False)
# carro3 = Carro (modelo= "Hb20", tem_4_portas=True, marca= "Hyundai", ano= 2023)

# if carro3.tem_4_portas == True:
#    print ("Carro com 4 portas")

# marca = str (input ("Digite a marca do carro: "))
# ano = str (input ("Digite a ano do carro: "))
# modelo = str (input ("Digite a modelo do carro: "))
# portas = str (input ("O carro tem 4 portas?: "))

# carro4 = Carro(marca=marca, modelo=modelo, ano=ano, tem_4_portas=portas)

# class Televisao:
#     def __init__(self,marca:str, polegadas:int, smart:bool, preco:float, apps:list):
#         self.marca= marca
#         self.polegadas = polegadas
#         self.smart = smart
#         self.preco = preco
#         self.apps = apps


# tv1 =Televisao (marca= "LG", polegadas=50, smart=True, preco= 2.149, apps=["Netflix , Youtube, Disney, HBO, Google, Discovery"])
# class Jogo:
#     def __init__(self, nome:str, ano_lancamento:int, genero:str, preco:float, estoque:bool):
#         self.nome=nome
#         self.ano_lancamento=ano_lancamento
#         self.genero = genero
#         self.preco = preco
#         self.estoque = estoque

# jogo1 = Jogo (nome= "TheSims4", ano_lancamento=2013, genero="livre", preco=100, estoque=True)


# if jogo1.estoque == True:
#      print(f"o jogo {jogo1.nome} tem no estoque")
# else:
#      print (f"o jogo {jogo1.nome} não tem no estoque")    

# if jogo1.preco >= 300:
#      print (f"O jogo {jogo1.nome} ta caro, quero não")
# else:
#      print(f"o jogo {jogo1.nome} ta no preço, vou querer")    
        

# nome= str (input("Digite o nome do Jogo: "))
# ano_lancamento= int (input("Qual o ano de lançamento Jogo: "))
# genero= str (input("Qual o genero: "))
# preco = float (input("Qual o preço do jogo: "))
# estoque = bool (input ("O jogo tem em estoque? "))

# jogo2 =Jogo (nome=nome, ano_lancamento=ano_lancamento, genero=genero, preco=preco, estoque=estoque)

# if jogo2.estoque == True:
#      print(f"o jogo {jogo2.nome} tem no estoque")
# else:
#      print (f"o jogo {jogo2.nome} não tem no estoque")    

# if jogo2.preco >= 300:
#      print (f"O jogo {jogo2.nome} ta caro, quero não")
# else:
#      print(f"o jogo {jogo2.nome} ta no preço, vou querer")  
# class Carro:
#   def __init__(self, marca,modelo,ano ):
#     self.marca = marca
#     self.modelo = modelo
#     self.ano = ano
#     self.velocidade_atual = 0

#   def ligar(self):
#     return f"O {self.modelo} está ligado"

#   def acelerar(self, velocidade):
#     self.velocidade_atual = self.velocidade_atual + velocidade
#     return self.velocidade_atual
  
#   def freiar(self):
#     if self.velocidade_atual <= 20:
#       self.velocidade_atual = 0
#     else:
#       self.velocidade_atual = self.velocidade_atual - 20
#     return self.velocidade_atual
  
#   def desligar(self):
#     return f"O {self.modelo} está desligado"
  


# carro1 = Carro(marca="Hyundai", modelo="HB20", ano=2019)

# while True:
#   menu = int(input("""
#             1 - Ligar
#             2 - Acelerar
#             3 - Freiar
#             4 - Desligar
#             0 - Sair
#   """))
#   match menu:
#     case 1:
#       print(carro1.ligar())
#     case 2:
#       velocidade = int(input("Digite o quanto você quer acelerar: "))
#       carro1.acelerar(velocidade)
#     case 3:
#       carro1.freiar()
#     case 4:
#       carro1.desligar()
#     case 0:
#       break
#     case _:
#       print("Opção inválida")

#   print(f"Velocidade atual: {carro1.velocidade_atual}")

class Fatura:
    def __init__(self,nome, preco,quantidade, valor_total):
        self.nome=nome
        self.preco = preco
        self.quantidade = quantidade
        self.valor_total = valor_total

def gerar_fatura (self):
    self.valor_total = self.preco * self.quantidade
    return f"o valor da fatura fatura {self.valor_total}"      
        
fatura1 = Fatura (nome= "Monitor", preco= 400 , quantidade=2, valor_total=800)       
print (f"o valor da fatura  {fatura1.gerar_fatura}")
