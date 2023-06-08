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
a=input()
b=input()
c=input()
print(str(conjunto_animais[a][b][c]))
