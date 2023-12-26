#! python

file = open('pessoas.csv')

for line in file:
  print("Nome: {} Idade: {}".format(*line.split(",")))

file.close()