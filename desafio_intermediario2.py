''' 
Desafio
Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar refrigerantes e levar os cascos vazios no dia seguinte, ela troca cada conjunto de K garrafas vazias  por uma garrafa cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

Faça um programa para calcular isso.

Entrada
A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos de teste. Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),  respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia.

Saída
Para cada caso de teste imprima o número de garrafas que o cliente terá no segundo dia, se aproveitar ao máximo a oferta.

 
Entrada	Saída
3
7 4
4 7
4000 7

4
4
574
'''
import sys



T = int(input()) 
for i in range (T): 
  a  = input()
  refrigerantes_comprados = int(a.split()[0])
  garrafas_vazias = int(a.split()[1])

  k = garrafas_vazias
  
  n = refrigerantes_comprados 

  total_garrafas_2o_dia = ((n % k) + (n // k))
  print(total_garrafas_2o_dia)
  