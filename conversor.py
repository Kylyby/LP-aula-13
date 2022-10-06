def converter(centimetros):
    output = open('saída.txt', 'a+', encoding="utf-8")
    output.write(
        f'o valor {centimetros} em centímetros corresponde a %.2f valor em polegadas\n' % (centimetros/2.54))
