
'''
# 1️⃣ Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) 
de um herói, depois utilize uma estrutura de decisão para apresentar alguma 
das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"
 '''

nome = str (input("Qual o nome do seu heroi ? \n"))
xp = int (input("Qual a experiencia total do heroi ? \n"))

while xp != -1:
    if xp >= 10001:
        nivel = 'Radiante' 
        print("O Herói de nome {} está no nível de {}".format(nome,nivel))
        break
    if xp < 1001:
        nivel = 'Ferro' 
        print("O Herói de nome {} está no nível de {}".format(nome,nivel))
        break
    if xp < 2001:
        nivel = 'Bronze' 
        print("O Herói de nome {} está no nível de {}".format(nome,nivel))
        break
    if xp < 5001:
        nivel = 'Prata' 
        print("O Herói de nome {} está no nível de {}".format(nome,nivel))
        break
    if xp < 7001:
        nivel = 'Ouro' 
        print("O Herói de nome {} está no nível de {}".format(nome,nivel))
        break
    if xp < 8001:
        nivel = 'Platina' 
        print("O Herói de nome {} está no nível de {}".format(nome,nivel))
        break
    if xp <  9001:
        nivel = 'Ascendente' 
        print("O Herói de nome {} está no nível de {}".format(nome,nivel))
        break
    if xp <= 10000:
        nivel = 'Imortal' 
        print("O Herói de nome {} está no nível de {}".format(nome,nivel))
        break
    









