'''DESAFIO 1'''
# def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
#     # Implemente aqui a lógica da função
#     if tempo_chegada1 > tempo_chegada2 and tempo_chegada1 > tempo_chegada3:
#         if tempo_chegada2 > tempo_chegada3:
#             variavel_de_retorno = f'1 - {tempo_chegada3} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada1} minutos\n'
#         else:
#             variavel_de_retorno = f'1 - {tempo_chegada2} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada1} minutos\n'
                
#     elif tempo_chegada2 > tempo_chegada1 and tempo_chegada2 > tempo_chegada3:
#         if tempo_chegada1 > tempo_chegada3:
#             variavel_de_retorno = f'1 - {tempo_chegada3} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada2} minutos\n'
#         else:
#             variavel_de_retorno = f'1 - {tempo_chegada1} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada2} minutos\n'
#     elif tempo_chegada3 > tempo_chegada1 and tempo_chegada3 > tempo_chegada2:
#         if tempo_chegada1 > tempo_chegada2:
#             variavel_de_retorno = f'1 - {tempo_chegada2} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada3} minutos\n'
#         else:
#             variavel_de_retorno = f'1 - {tempo_chegada1} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada3} minutos\n'

# # ERRO:'1 - 3 minutos\n2 - 2 minutos\n3 - 1 minutos\n' != '1 - 1 minutos\n2 - 2 minutos\n3 - 3 minutos\n'
# # ERRO: '1 - 1 minuto(s) \n2 - 2 minuto(s)\n 3 - 3 minuto(s) \n' != '1 - 1 minutos\n2 - 2 minutos\n3 - 3 minutos\n'
        
#     return variavel_de_retorno

# temp_cheg1 = 10
# temp_cheg2 = 7
# temp_cheg3 = 8

# print(podio_olimpico(temp_cheg1, temp_cheg2, temp_cheg3))


'''DESAFIO 2'''
def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3,nome_corredor1,nome_corredor2,nome_corredor3):
    # Implemente aqui a lógica da função
    if tempo_chegada1 > tempo_chegada2 and tempo_chegada1 > tempo_chegada3:
        if tempo_chegada2 > tempo_chegada3:
            variavel_de_retorno = f'1 - {nome_corredor3} - {tempo_chegada3} minutos\n2 - {nome_corredor2} - {tempo_chegada2} minutos\n3 - {nome_corredor1} - {tempo_chegada1} minutos\n'
        else:
            variavel_de_retorno = f'1 - {nome_corredor2} - {tempo_chegada2} minutos\n2 - {nome_corredor3} - {tempo_chegada3} minutos\n3 - {nome_corredor1} - {tempo_chegada1} minutos\n'
                
    elif tempo_chegada2 > tempo_chegada1 and tempo_chegada2 > tempo_chegada3:
        if tempo_chegada1 > tempo_chegada3:
            variavel_de_retorno = f'1 - {nome_corredor3} - {tempo_chegada3} minutos\n2 - {nome_corredor1} - {tempo_chegada1} minutos\n3 - {nome_corredor2} - {tempo_chegada2} minutos\n'
        else:
            variavel_de_retorno = f'1 - {nome_corredor1} - {tempo_chegada1} minutos\n2 - {nome_corredor3} - {tempo_chegada3} minutos\n3 - {nome_corredor2} - {tempo_chegada2} minutos\n'
    elif tempo_chegada3 > tempo_chegada1 and tempo_chegada3 > tempo_chegada2:
        if tempo_chegada1 > tempo_chegada2:
            variavel_de_retorno = f'1 - {nome_corredor2} - {tempo_chegada2} minutos\n2 - {nome_corredor1} - {tempo_chegada1} minutos\n3 - {nome_corredor3} - {tempo_chegada3} minutos\n'
        else:
            variavel_de_retorno = f'1 - {nome_corredor1} - {tempo_chegada1} minutos\n2 - {nome_corredor2} - {tempo_chegada2} minutos\n3 - {nome_corredor3} - {tempo_chegada3} minutos\n'
# ERRO '1 - Fulano1- 1 minutos\n2 - Fulano2 - 2 minutos\n3 - Fulano3 - 3 minutos\n' != '1 - Fulano1 - 1 minutos\n2 - Fulano2 - 2 minutos\n3 - Fulano3 - 3 minutos\n'
    return variavel_de_retorno

temp_cheg1 = 10
temp_cheg2 = 7
temp_cheg3 = 8
nome_corr1 = ''
nome_corr2 = ''
nome_corr3 = ''

print(podio_olimpico(temp_cheg1, temp_cheg2, temp_cheg3,nome_corr1,nome_corr2,nome_corr3))