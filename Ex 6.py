tempo = int(input('Informe os segundos: '))


def calculo_tempo():
    minuto = tempo/60
    hora = minuto/60
    dia = hora/24
    minuto_formatado = "{:.0f}".format(minuto)
    hora_formatada = "{:.1f}".format(hora)
    dia_formatado = "{:.0f}".format(dia)
    print(f'{tempo} segundos correspondem a {minuto_formatado} min, {hora_formatada} h e {dia_formatado} dias')

calculo_tempo()    