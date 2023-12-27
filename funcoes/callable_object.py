class Potencia:
  def __init__(self, expoente):
    self.expoente = expoente


  def __call__(self, base):
    return base ** self.expoente
    
quadrado = Potencia(2)
cubo = Potencia(3)

if callable(quadrado) and callable(cubo):
  print(f'3 => {quadrado(3)}')
  print(Potencia(3)(2))