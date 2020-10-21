class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

ancestor_input = input("Who are the ancestors? Separate them by space \n") 
ancestors = [[Node(ancestor) for ancestor in ancestor_input.split(' ')]]

while True:
    ancestors.append([])
    for ancestor in ancestors[-2]:
        children_input = input("Who are the children of " + ancestor.data + '\n')
        for child in children_input.split(' '):
            ancestor.add_child(child) 
            new_node = Node(child)
            ancestors[-1].append(new_node)

    cont = input("Do you want to add a new generation? Y / N \n")
    if cont == "Y":    
        continue
    if cont == "N":
        for i in ancestors[0]:
            print (i.data, i.children)
        break
    else:
        "invalid input. Please answer yes by entering Y and no by entering N"