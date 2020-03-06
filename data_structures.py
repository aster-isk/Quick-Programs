
#Puts together a data structure where only the most recent entry is accessable
#first in first out
class Stack:
     
     
    def __init__(self):
         self.__contents = []

    def top(self):
        data = self.__contents[-1]
        return data     
                           
    def pop(self):
        data = self.top()
        self.__contents = self.contents[:-1]
        return data
        
    def push(self, data):
        self.__contentss += data
        

#Puts together a data structure where only the last entry is accessable
#first in last out
class Queue:
    
    def __init__(self):
        self.__contents = []

    def bottom(self):
        data = self.__contents[0]
        return data 
                
    def enqueue(self, data):
        self.__contents += data
        
    def dequeue(self):
        data = self.bottom()
        self.__contents = self.contents[1:]
        return data
    

#Tree Nodes for a SBT
class TreeNode():
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def print_node(self):
        print(self.data)
        
    def add_sorted_node(self, d, node):
        if d <= node.data:
            if node.left == None:
                node.left = TreeNode(d)
            else:
                node.left.add_sorted_node(d, node.left)
        elif d > node.data:
            if node.right == None:
                node.right = TreeNode(d)
            else:
                node.right.add_sorted_node(d, node.right)
                
#Creates a Sorted Binary Tree from a given array or list
class SortedBinaryTree:
    
    def __init__(self, data):
        self.__root = TreeNode(data[0])
        data = data[1:]
        for d in data:
            print("init" + str(d))
            self.__root.add_sorted_node(d, self.__root)
            
    def add_node(self, d):
        self.__root.add_sorted_node(d, self.__root)
        
    def __print_inorder(self, node):
        if node == None:
                return
        node.print_node()
        self.__print_inorder(node.left)
        self.__print_inorder(node.right)
        
    def print_inorder(self):
        self.__print_inorder(self.__root)
        
