class carro:
  def __init__(self, marca, modelo, cor):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.velocidade = 0

  def acelerar(self):
    self.velocidade += 10
    

  def frear(self):
    self.velocidade -= 10
    if self.velocidade < 0:
      self.velocidade = 0 
    print(f"Velocidade atual: {self.velocidade} km/h")

  def exibir_info(self):
    print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}")


lista_carros = []

while True:
  print("\n---Menu---\n")
  print("1 - Adicionar novo Carro")
  print("2 - exibir informações do carro")
  print("3 - acelerar o carro")
  print("4 - frear o carro")
  print("5 - sair")

  escolha = input("escolha uma Opção: ")

  if escolha =="1":
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    cor = input("Digite a cor do carro: ")

    novo_carro = carro(marca, modelo, cor) 
    lista_carros.append(novo_carro)

  elif escolha =="2":
    if lista_carros:
      for carro in lista_carros: 
        carro.exibir_info() 
    else:
      print("Nenhum carro cadastrado")

  elif escolha =="3":
    modelo = input("Digite o Modelo do carro que deseja acelerar: ")
    for carro in lista_carros: 
      if carro.modelo == modelo:
        carro.acelerar()
        break 
      print("modelo de carro não encontrado")

  elif escolha =="4":
    modelo = input("Digite o Modelo do carro que deseja frear: ")
    for carro in lista_carros: 
      if carro.modelo == modelo:
        carro.frear()
        break 
    else:
      print("modelo de carro não encontrado")

  elif escolha =="5":
    print("Saindo do programa em:... \n 1 \n 2 \n 3 \nsaindo...")
    break 
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
