def executar(funcao):
  if callable(funcao):
    funcao()


def bom_dia():
  print('Bom dia')

def boa_tarde():
  print('Boa tarde')

executar(boa_tarde)