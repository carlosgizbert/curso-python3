#! python
with open('desafio-ibge.csv', 'r') as fileRead:
    with open('exit.txt', 'w') as fileExit:
        for line in fileRead:
            line = line.strip().split(',')
            # fileExit.write("Quarto: {} Nono: {}\n".format(line[3], line[7]))
            print("Quarto: {} Nono: {} ".format(line[3], line[8]))

if fileRead.closed:
  print('Arquivo já foi fechado!')

if fileExit.closed:
  print('Arquivo de saída já foi fechado!')