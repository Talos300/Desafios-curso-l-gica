class Heroi:
    def __init__(self, nome, idade, classe):
        self.nome = nome
        self.idade = idade
        self.classe = classe

    def atacar(self):
        if self.classe == 'mago':
            self.ataque = 'magia'
        elif self.classe == 'guerreiro':
            self.ataque = 'espada'
        elif self.classe == 'monge':
            self.ataque = 'artes marciais'
        elif self.classe == 'ninja':
            self.ataque = 'shuriken'
        else:
            self.ataque = 'suas habilidades'
        
        print(" O seu " + self.classe + " atacou usando " + self.ataque);

personagem_mago = Heroi('Patous','80','mago')
personagem_guerreiro = Heroi('Duncan','25','guerreiro')
personagem_monge = Heroi('Aang','40','monge')

personagem_mago.atacar();
personagem_monge.atacar();
personagem_guerreiro.atacar();