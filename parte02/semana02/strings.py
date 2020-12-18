# time = 'joão'
# time.upper() # JOÃO
# time.lower() # joão
# frase = "there should have been a time and a place, but this wasn't it"
# frase.capitalize() # There should have been a time and a place, but this wasn't it
# email = " email@email.com "
# email.strip() # "email@email.com"
# frase.count('a') # 6
# frase.replace("should", "") # there  have been a time and a place, but this wasn't it
# print(time.capitalize().center(40)) #
# print(frase.find('b'))


'''Escrever uma função que recebe uma lista de Strings 
contendo nomes de pessoas como parâmetro e devolve o nome mais curto.
A função deve ignorar espaços antes e depois do nome e deve devolver o nome 
"capitalizado", i.e, apenas com a 1a letra maiúscula'''
lista_de_nomes = ["josé", " ana", "arquibaldo", "alouhis"]
def shorter(array_of_names):
  short = array_of_names[0]
  for i in range(len(array_of_names)-1):
    if len(array_of_names[i].strip()) < len(short):
      short = array_of_names[i].strip()
  return short.capitalize()

print(shorter(lista_de_nomes))


