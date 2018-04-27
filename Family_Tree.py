from IPython.display import clear_output

class Person:
    def __init__(self, name, birth, death=None):
        self.name = name
        self.birth = birth
        self.death = death

relatives = ['you','grandfather','father','brother','sister','son','daughter']
persons = {}

def enter_person():
    for relative in relatives:
        if relative == 'you':
            name = input('What is your name?')
            birth = input('Your date of birth: ')
            persons['you'] = Person(name, birth)
        else:
            name = input("Enter {}'s name: ".format(relative))
            birth = input("Enter {}'s date of birth: ".format(relative))
            death = input("Enter {}'s date of death if applicable: ".format(relative))
            persons[relative] = Person(name, birth, death)

from anytree import Node, RenderTree

def family_tree():
    
    grandfather = Node(persons['grandfather'].name, birth = persons['grandfather'].birth, death = persons['grandfather'].death )
    father = Node(persons['father'].name, parent=grandfather, birth = persons['father'].birth, death = persons['father'].death)
    you = Node(persons['you'].name, parent=father, birth = persons['you'].birth, death = '' )
    brother = Node(persons['brother'].name, parent=father, birth = persons['brother'].birth, death = persons['brother'].death)
    sister = Node(persons['sister'].name, parent=father, birth = persons['sister'].birth, death = persons['sister'].death)
    son = Node(persons['son'].name, parent=you, birth = persons['son'].birth, death = persons['son'].death)
    daughter = Node(persons['daughter'].name, parent=you, birth = persons['daughter'].birth, death = persons['daughter'].death)
    for pre, fill, node in RenderTree(grandfather):
        if node.name != '':
            print("{}{}, ({})-({})".format(pre, node.name, node.birth, node.death))

enter_person()
clear_output()

print('Here is your family tree:\n')
family_tree()














