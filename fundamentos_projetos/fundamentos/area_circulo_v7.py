#! python
from math import pi
import sys

def circulo(raio: str):
  return pi * float(raio) ** 2


if __name__ == '__main__':
  if len(sys.argv) < 2:
    name = sys.argv[0]
    print(f"É necessario informar a area do circulo, ex: {name} 12")
  
  else:
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do circulo', area)