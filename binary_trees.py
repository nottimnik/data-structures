#binary tree example:
#               g
#              / \
#             /   \
#            /     \
#           /       \
#          c         i
#         / \       / \
#        /   \     /   \
#       /     \   h     j
#      b       e         \
#     /       / \         \
#    /       d   f         k
#   a    


class Node: #binary tree node implemanatation
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
    def insert(self, data): #insert function to insert data into the binary tree
        if self.data is None:
            self.data = data
            
        else:
            
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                    
            elif data > self.data:
                
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


#InOrder: left, root, right
#PreOrder: root, left, right
#PostOrder: root, right, left

def inOrder(r): #inOrder Traversal of Binary tree
    if r is None: #make the recursive function stop when we reach the end
        return 
    else:
        preinter(r.left)
        print(r.data)
        preinter(r.right)
        
def PreOrder(r): #PreOrder Traversal of Binary tree
    if r is None: #make the recursive function stop when we reach the end
        return
    else:
        print(r.data) #first print the root then go to left and after that to the right
        PreOrder(r.left)
        PreOrder(r.right)
        
def PostOrder(r): #PostOder Traversal of Binary Tree - same as the others just change the order
    if r is None:
        return
    else: 
        print(r.data)
        PostOrder(r.right)
        PostOrder(r.left)
        
#AdjacencyList Examples:
# g: [c, i]
# c: [b, e]
# b: [a]
# a: []
# etc...

d = {} #dic that we will use to store the lists

def AdjacencyListMaker(r): #use the inorder traversal 
    if r is None: 
        return 
    else:
        d[r.data] = []
        AdjacencyListMaker(r.left)
        
        
        if(r.left):
            d[r.data].append(r.left.data)
            
        if(r.right):
            d[r.data].append(r.right.data)
            
        AdjacencyListMaker(r.right)
        
    return d
    
                    
if __name__ == '__main__':
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    
    print('Adjacency Lists:')
    Adjacency = AdjacencyListMaker(root)
    for ele in Adjacency:
        print(f'{ele} : {d[ele]}')
