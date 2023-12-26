#! python

file = open('pessoas.csv')

for line in file:
  print("Nome: {} Idade: {}".format(*line.strip().split(",")))

file.close()