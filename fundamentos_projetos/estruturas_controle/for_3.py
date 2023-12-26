produto = {
  'nome': 'Caneca Chic',
  'preco': 14.99,
  'importada': True,
  'estoque': 793
}

for key in produto:
  print(key)

# for key in produto.keys():
#   print(key)

for value in produto.values():
  print(value)

for key, value in produto.items():
  print(key, ' = ', value)