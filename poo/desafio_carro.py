class Carro:
    def __init__(self, velocidade_maxima=180):
        self.velocidade_atual = 0
        self.velocidade_minima = 0
        self.velocidade_maxima = velocidade_maxima

    def __print__(self):
        print(f"velocidade atual: {self.velocidade_atual}")

    def acelerar(self, delta=5):
        self.velocidade_atual = min(
            self.velocidade_atual + delta, self.velocidade_maxima
        )
        return self.velocidade_atual

    def frear(self, delta=5):
        self.velocidade_atual = max(
            self.velocidade_atual - delta, self.velocidade_minima
        )
        return self.velocidade_atual


c1 = Carro(180)

for _ in range(25):
    print(c1.acelerar(8))

for _ in range(10):
    print(c1.frear(delta=20))
