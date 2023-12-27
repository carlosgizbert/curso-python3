def fibonacci(sequencia=[0, 1]):
  # Usar mutáveis como valor default é armadilha
  # Não deve usar objetos mutáveis como parametro padrão de funções
  sequencia.append(sequencia[-1] + sequencia[-2])

  inicio = fibonacci()
  print(inicio, id(inicio))
  print(fibonacci(inicio))
  restart = fibonacci()
  print(restart, id(restart))