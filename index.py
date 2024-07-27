class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque padrão"  # Caso o tipo não seja reconhecido

        print(f"O {self.tipo} {self.nome} atacou usando {ataque}")

# Criando alguns heróis
heroi1 = Heroi("Gandalf", 2000, "mago")
heroi2 = Heroi("Conan", 30, "guerreiro")
heroi3 = Heroi("Ryu", 35, "monge")
heroi4 = Heroi("Hanzo", 32, "ninja")
heroi5 = Heroi("Personagem desconhecido", 25, "desconhecido")

# Fazendo os heróis atacarem
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
heroi5.atacar()
