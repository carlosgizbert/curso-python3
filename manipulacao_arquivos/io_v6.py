#! python
with open('pessoas.csv', 'r') as fileRead:
    with open('exit.txt', 'w') as fileExit:
        for line in fileRead:
            people = line.strip().split(',')
            fileExit.write("Nome: {} Idade: {}\n".format(*people))

if fileRead.closed:
  print('Arquivo já foi fechado!')

if fileExit.closed:
  print('Arquivo de saída já foi fechado!')