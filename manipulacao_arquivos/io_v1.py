#! python

file = open('pessoas.csv')
data = file.read()
file.close()

for line in data.splitlines():
  print("Nome: {}, Idade: {}".format(*line.split(',')))