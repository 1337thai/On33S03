## Atividade 4: Utilize a formatação de strings para criar uma mensagem personalizada.

import random

palavras = ['pirulito', 'pimenta', 'caracol','etiqueta', 'terremoto']

palavras = random.choice(palavras)

resultado = f'{palavras}'

print('A palavra aleatória é:', resultado)