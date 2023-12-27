#! python

def tag_bloco(conteudo, classe='success'):
  return f'<div class="{classe}">{conteudo}</div>'

def tag_lista(*itens):
  lista = ''.join((f'<li>{item}</li>' for item in itens))
  return f'<ul>{lista}</ul>'

if __name__ == '__main__':
  assert tag_bloco('Incluído com sucesso!') == '<div class="success">Incluído com sucesso!</div>'
  assert tag_bloco('Impossível excluir!') == '<div class="success">Impossível excluir!</div>'
  print(tag_bloco('bloco'))
  print(tag_lista('Item 1', 'Item 2'))