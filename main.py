def etapa1(ID):
    ID = str(ID)

    listaID= []
    for letra in ID:
        listaID.append(int(letra))
    listaID.sort(reverse=True)
    if len(listaID) == 4:
        maior1 = listaID[0]
        maior2 = listaID[1]
        maior3 = listaID[2]
        maior4 = listaID[3]
    elif len(listaID) == 3:
        maior1 = listaID[0]
        maior2 = listaID[1]
        maior3 = listaID[2]
        maior4 = 0
    elif len(listaID) == 2:
        maior1 = listaID[0]
        maior2 = listaID[1]
        maior3 = 0
        maior4 = 0
    elif len(listaID) == 1:
        maior1 = listaID[0]
        maior2 = 0
        maior3 = 0
        maior4 = 0
    str1 = str(maior1)
    str2 = str(maior2)
    str3 = str(maior3)
    str4 = str(maior4)

    combinacao1 = int(str4+str1)
    combinacao2 = int(str3+str2)
    combinacao3 = int(str4+str3+str2)
    combinacao4 = int(str1)

    lista1 = [combinacao1, combinacao2]
    lista2 = [combinacao3, combinacao4]
    if sum(lista1) > sum(lista2):
        return (sum(lista2))
    else:
        return (sum(lista1))


def etapa2(self):
    lista2 = []
    valores = []
    output = []
    self.sort()
    for x in self:
        if x not in valores:
            valores.append(x)
    print(valores)
    if len(valores) == len(self):
        print("Funcionou")
    else:
        x = 1
        while x != (len(self) + 1):
            if x not in self:
                output.append(x)
            x += 1
        x = 1
        while x != self[(len(self) - 1)]:
            if x not in self:
                if x not in output:
                    output.append(x)
            x += 1
        return (output)


def etapa3(senha):
    senha = list(senha)
    a = 1
    b = []
    c = {}
    valido = True
    for x in senha:
        if x not in b:
            b.append(x)
            c[x] = 0
    for x in senha:
        if x in b:
            c[x] += 1
    for x in c:
        while a < len(b):
            if c[x] != c[b[a]]:
                valido = False
                break
            a += 1
    return valido


if __name__ == "__main__":
    if etapa1('1234') > 100:
        print('ID inválido')
        exit(1)
    if len(etapa2([1, 1])) > 0:
        print('Voto inválido')
        exit(1)
    if not etapa3('abba'):
        print('Senha inválida')
        exit(1)
