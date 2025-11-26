class Fabricante:
    def __init__(self, nome):
        self.nome = nome


class Carro:
    def __init__(self, cor, ano, modelo, fabricante, placa):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
        self.fabricante = fabricante  # objeto Fabricante
        self.placa = placa


def cadastrar(lista, carro=None):
    if carro is None:
        cor = input("Cor: ")
        ano = int(input("Ano: "))
        modelo = input("Modelo: ")
        nome_fabricante = input("Fabricante: ")
        placa = input("Placa: ")

        fabricante = Fabricante(nome_fabricante)
        carro = Carro(cor, ano, modelo, fabricante, placa)

    lista.append(carro)
    return lista


def imprimir(lista):
    for c in lista:
        print(f"Modelo: {c.modelo}")
        print(f"Cor: {c.cor}")
        print(f"Ano: {c.ano}")
        print(f"Placa: {c.placa}")
        print(f"Fabricante: {c.fabricante.nome}")
        print("-" * 20)


def autoCadastrar(lista):
    f1 = Fabricante("Ford")
    f2 = Fabricante("Volkswagen")
    f3 = Fabricante("Fiat")

    cadastrar(lista, Carro("Prata", 2010, "Fiesta", f1, "ABC-1234"))
    cadastrar(lista, Carro("Preto", 2018, "Gol", f2, "XYZ-9988"))
    cadastrar(lista, Carro("Branco", 2015, "Uno", f3, "JHG-2211"))
    cadastrar(lista, Carro("Vermelho", 2020, "Ka", f1, "KKK-2020"))
    cadastrar(lista, Carro("Azul", 2012, "Polo", f2, "POL-3012"))


if __name__ == "__main__":

    lista = []
    finalizar = True

    while finalizar:
        option = input(
            "Digite a opção desejada: \n"
            "1 - Imprimir veiculos cadastrados: \n"
            "2 - Cadastrar veiculos: \n"
            "3 - Finalizar programa: \n"
        )

        match option:
            case "1":
                imprimir(lista)
            case "2":
                lista = cadastrar(lista)
            case "3":
                print("Finalizando o programa...")
                finalizar = False
            case "22":
                lista = autoCadastrar(lista)
            case _:
                print(f"Opção inválida: {option}")
