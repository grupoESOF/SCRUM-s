import shelve
shelf = shelve.open('Words')
lista = []
adj = input('Enter an adjective:')
lista.append(adj)
noun1 = input('Enter a noun:')
lista.append(noun1)
verb = input('Enter a verb:')
lista.append(verb)
noun2 = input('Enter with other noun:')
lista.append(noun2)
shelf['words'] = lista
print('The', shelf['words'][0] ,'panda walked to the', shelf['words'][1],
      'and then ', shelf['words'][2],'. A nearby ', shelf['words'][3],' was unaffected by these events.')
