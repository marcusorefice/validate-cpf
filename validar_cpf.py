while True:
    cpf = input('Informe o CPF com 11 números e sem pontuação: ')
    if not cpf.isnumeric() or len(cpf) != 11:
        print("O CPF só pode conter números.")
        print("Digite exatamente 11 números.")
        print()
    else:
        break

novo_cpf = cpf[:-2]
mult = 10
soma = 0
temp = []

while True:
    if len(novo_cpf) == 10:
        mult = 11
    for p in novo_cpf:
        temp.append(int(p) * mult)
        mult -= 1
    soma = sum(temp)
    temp.clear()
    digito1 = 11 - (soma % 11)

    if digito1 > 9:
        digito1 = 0
    novo_cpf += str(digito1)
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if len(novo_cpf) == 11:
        if cpf == novo_cpf and not sequencia:
            print('O CPF é válido')
        else:
            print('O CPF é inválido')
        break
