#! python
with open('pessoas.csv') as file:
  for line in file:
    print("Nome: {} Idade: {}".format(*line.strip().split(",")))

if file.closed:
  print('Arquivo já foi fechado!')