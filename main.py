nomes = ["Banana", "Amor", "Cacto", "Maça", "Feliz", "Azul"]

def ordenar_nomes(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(tamanho - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def buscar_nome(lista, busca):
    for nome in lista:
        if nome.lower() == busca.lower():
            return f"Nome '{busca.capitalize()}' encontrado"
    return f"Nome '{busca.capitalize()}' não encontrado"


def buscar_index(lista, busca):
    for i, nome in enumerate(lista):
        if nome.lower() == busca.lower():
            return f"Nome '{busca.capitalize()}' encontrado no índice {i}"
    return f"Nome '{busca.capitalize()}' não encontrado na lista"


nomes_ordenados = ordenar_nomes(nomes)

print("Lista ordenada:", nomes_ordenados)
print(buscar_nome(nomes_ordenados, "Banana"))
print(buscar_index(nomes_ordenados, "EfIco"))
