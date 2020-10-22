class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    # A function to do inorder tree traversal 
    def printInorder(self): 
        print (self.data)
        if self.children != []:
            for i in self.children:
                i.printInorder()

# ancestor_input = input("Who is the ancestor \n") 
# ancestors = [[Node(ancestor_input)]]

# while True:
#     ancestors.append([])
#     for ancestor in ancestors[-2]:
#         children_input = input("Who are the children of " + ancestor.data + '\n')
#         for child in children_input.split(' '):
#             new_node = Node(child)
#             ancestor.add_child(new_node) 
#             ancestors[-1].append(new_node)

#     while True:
#         cont = input("Do you want to add a new generation? Y / N \n")

#         if cont == "Y" or "N":    
#             break
#         else:
#             print("invalid input. Please answer yes by entering Y and no by entering N")

#     if cont == "N":
#         break

# root = ancestors[0][0]

# root.printInorder()