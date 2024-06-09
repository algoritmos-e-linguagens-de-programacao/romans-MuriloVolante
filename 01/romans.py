def int_to_roman(num):

    num2 = num // 1000
    num3 = (num % 1000) // 100
    num4 = (num % 100) // 10
    num5 = num % 10

    milhar = ["","M","MM","MMM"]
    centena = ["","C","CC","CCC","CD","D","DC","DCC", "DCCC", "CM"]
    dezena = ["","X","XX","XXX","XL","L","LX","LXX","LXXX", "XC"]
    unidade = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

    traducao = milhar[num2] + centena[num3] + dezena[num4] + unidade[num5]

    return traducao


def roman_to_int(s):
    def romano_para_numero(romano):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    valor_anterior = 0

    for caractere in reversed(romano):
        valor_atual = valores[caractere]

        if valor_atual < valor_anterior:
            total -= valor_atual
        else:
            total += valor_atual

        valor_anterior = valor_atual

    return total

romano = "M"
inteiro = romano_para_numero(romano)
print(inteiro)

    pass
