class Node(object):
    """
This function builds node objects for the tree builder class.
Args
    input (string): name of the node
Returns
    output: node object
    """
    def __init__(self, data):
        self.data = data
        self.children = []
    """ Using this function we can add children to the existing nodes.
Args
    input (string): name of the children
Returns
    output (obj): children object
    """
    def add_child(self, obj):
        self.children.append(obj)


    new_list = []

    """ This function is used in the tree builder to print all nodes in the tree
Args
    input (Node object): root node
Returns
    output (obj): children object
    """        
    def tree_list(self): 
        self.new_list.append(self.data)
        if self.children != []:
            for i in self.children:
                i.tree_list()
        return self.new_list

class Treebuilder:
    def __init__ (self):
        self.ancestor_input = input("Who is the ancestor \n")

    """ Using this function we can build a tree.
Args
    input : None
Returns
    output (List): A list of all nodes
    """
    def build(self):
        self.ancestors = [[Node(self.ancestor_input)]]

        while True:
            self.ancestors.append([])
            for ancestor in self.ancestors[-2]:
                children_input = input("Who are the children of " + ancestor.data + '\n')
                for child in children_input.split(' '):
                    new_node = Node(child)
                    ancestor.add_child(new_node) 
                    self.ancestors[-1].append(new_node)

            while True:
                cont = input("Do you want to add a new generation? Y / N \n")

                if cont == "Y" or "N":    
                    break
                else:
                    print("invalid input. Please answer yes by entering Y and no by entering N")

            if cont == "N":
                break

        root = self.ancestors[0][0]

        return root.tree_list()

a = Treebuilder().build()
print (a)