'''
 # 2️⃣ Calculadora de partidas Rankeadas

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções

## Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

'''

def saldoVitorias(V, D):
    return V - D

V = int (input("Quantas vitorias  ? \n"))
D = int (input("Quantas derrotas ? \n"))



cal = saldoVitorias(V,D)


while V != -999:
    if  cal <= 10:
        nivel = 'Ferro' 
        print("Suas vitorias são {} e seu rank está no nível de {}".format(cal,nivel))
        break
    elif cal <= 20:
        nivel = 'Bronze' 
        print("O Herói de nome {} está no nível de {}".format(cal,nivel))
        break
    elif cal <= 50:
        nivel = 'Prata' 
        print("O Herói de nome {} está no nível de {}".format(cal,nivel))
        break
    elif cal <= 80:
        nivel = 'Ouro' 
        print("O Herói de nome {} está no nível de {}".format(cal,nivel))
        break
    elif cal <= 90:
        nivel = 'Diamante' 
        print("O Herói de nome {} está no nível de {}".format(cal,nivel))
        break
    elif cal <= 100:
        nivel = 'Lendário' 
        print("O Herói de nome {} está no nível de {}".format(cal,nivel))
        break
    else:
        nivel = 'Imortal' 
        print("O Herói de nome {} está no nível de {}".format(cal,nivel))
        break