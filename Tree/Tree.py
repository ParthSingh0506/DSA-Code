
class TreeNode:
    def __init__(self, d):
        self.data = d
        self.leftchild = None
        self.rightchild = None
        
root = TreeNode("Menu")
drink = TreeNode("Drink")
food = TreeNode("Food")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
panipuri = TreeNode("Panipuri")
dosa = TreeNode("Dosa")

root.leftchild = drink
root.rightchild = food

drink.leftchild = tea
drink.rightchild = coffee

food.leftchild = panipuri
food.rightchild = dosa

''' Hybrid Recursion code:
def preOrderTraversal(node):
    if node:
        print(node.data)
        pre(node.leftchild)
        pre(node.rightchild)
'''

stack = []

// # Tail Recursion code:
def preOrderTraversal(node):
    
    print(node.data)
    if node.rightchild != None:
        stack.append(node.rightchild)
    if node.leftchild != None:
        stack.append(node.leftchild)
    if stack:
        preOrderTraversal(stack.pop())
        
        
preOrderTraversal(root)

/*
                    Menu
                    /  \
                   /    \
                  /      \
                 /        \
              Drinks        Food
               /  \       /      \ 
              /    \   Panipuri Dosa
            Tea   Coffee
*/