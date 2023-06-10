''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 

conjunto_animais = {
  'vertebrado': {
    'ave': {
      'carnivoro': 'aguia',
      'onivoro': 'pomba'
    },
    'mamifero': {
      'onivoro': 'homen',
      'herbivoro': 'vaca'
    }
 },
 'invertebrado': {
     'inseto': {
         'hematofago': 'pulga',
         'herbivoro': 'lagarta'
     },
     'anelideo': {
         'hematofago': 'sanguessuga',
         'onivoro': 'minhoca'
     }
    
 }

}

'''

import sys

a = input()
b = input()
c = input()


if a == 'vertebrado':
    if b == 'ave' and 'carnivoro':
            print('aguia')
    elif b == 'ave' and c == 'onivoro':
            print('pomba')
    elif b == 'mamifero' and c == 'onivoro':
            print('homen')
    elif b == 'mamifero' and c == 'herbivoro':
            print('vaca')
elif a == 'invertebrado':
    if b == 'inseto' and c == 'hematofago':
            print('pulga')
    elif b == 'inseto' and c == 'herbivoro':
            print('lagarta')
    elif b == 'anelideo' and c == 'hematofago':
            print('sanguessuga')
    elif b == 'anelideo' and c == 'onivoro':
            print('minhoca')