#T = input(''' ''')
T = [input() for _ in range()]

def check_size(texto):
    if len(texto) <=1 and len(texto)<= 140:
      print(f"TWEET")
    else:
      print(f"MUTE")
      
check_size(T)