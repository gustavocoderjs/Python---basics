

class Pessoa:
    def andar(self):
        print("Pessoa está andando com duas pernas.")

class Cachorro:
    def andar(self):
        print("Cachorro está andando com quatro patas.")

class Robo:
    def andar(self):
        print("Robô está andando com rodas.")

def movimento(objeto):
    objeto.andar()

p = Pessoa()
c = Cachorro()
r = Robo()

movimento(p)  # Pessoa está andando com duas pernas.
movimento(c)  # Cachorro está andando com quatro patas.
movimento(r)  # Robô está andando com rodas.

