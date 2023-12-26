#! python
try:
  file = open('pessoas.csv')

  for line in file:
    print("Nome: {} Idade: {}".format(*line.strip().split(",")))
finally:
  file.close()

if file.closed:
  print('Arquivo já foi fechado!')