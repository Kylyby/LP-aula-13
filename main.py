from conversor import converter

while True:
    valor = input('digite o valor em centímetros (ou "sair" para sair): ')
    if valor == 'sair':
        break
    else:
        converter(float(valor))
        print('222')
