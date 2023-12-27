def todos_params(*args, **kwargs):
  print(f'args: {args}')
  print(f'kwargs: {kwargs}')

todos_params('a', 'b', 'c')
print('--------------------')
todos_params(1, 2, 3, legal=True, valor=12.99)