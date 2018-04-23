lista = []

length = int(input('How many elements will your list have? '))
print('\n')

while length > 0:
    element = int(input('Add a number to your list: '))
    length -= 1
    lista.append(element)

print('\nYour list is:',lista)

nova_lista = []

while len(lista) > 0:
    
    for counter in range(1,len(lista)):
    
        n = len(lista)
        a = lista[n-counter]   
        b = lista[n-counter-1] 

        if a<b:
            lista.remove(b)             
            lista.insert(n-counter,b)   
        else:
            pass

    x = lista.pop(0)      
    nova_lista.append(x)  

print('\nYour bubble sorted list is:',nova_lista)