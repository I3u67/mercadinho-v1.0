print("Seja bem vindo a padaria!")
class pao:
    nome = str()
    quantidade = int()
    preco = float(5.0)

class agua:
    nome = str()
    quantidade = int()
    preco = float(2.0)

class banana:
    nome = str()
    quantidade = int()
    preco = float(3.0)

print("Oque você quer?")
print("Pão: R$5,00 | Água: R$2,00 | Banana: R$3,00")
pedido = str(input("Faça seu pedido: ").lower().strip())
if pedido == "pao":
    pedido = pao
    pedido.quantidade = int(input("Quantos você quer? "))
    valorfinal = pedido.quantidade * pedido.preco
    print(f"A compra será: R${valorfinal}")
    print("Quanto de dinheiro você possue? Para efetuar o pagamento! ")
    carteira = float(input("insira seu saldo: "))
    if carteira >= valorfinal:
        print("Compra efetuada!")
    else:
        print("Saldo Insuficiente!")
if pedido == "agua":
    pedido = agua
    pedido.quantidade = int(input("Quantos você quer? "))
    valorfinal = pedido.quantidade * pedido.preco
    print(f"A compra será: R${valorfinal}")
    print("Quanto de dinheiro você possue? Para efetuar o pagamento! ")
    carteira = float(input("insira seu saldo: "))
    if carteira >= valorfinal:
        print("Compra efetuada!")
    else:
        print("Saldo Insuficiente!")
if pedido == "banana":
    pedido = banana
    pedido.quantidade = int(input("Quantos você quer? "))
    valorfinal = pedido.quantidade * pedido.preco
    print(f"A compra será: R${valorfinal}")
    print("Quanto de dinheiro você possue? Para efetuar o pagamento! ")
    carteira = float(input("insira seu saldo: "))
    if carteira >= valorfinal:
        print("Compra efetuada!")
    else:
        print("Saldo Insuficiente!")


