#klutix
#this class was created as a educational challenge
class Node():
    node1 = None
    node2 = None
    deepest_node = None
    def __init__(self,value=None):
            self.value = value
                     
    def add(self,value):        
        if value >= self.value:
                if self.node2 is None :
                    self.node2 = Node(value)
                    Node.deepest_node = self.node2
                elif self.node2.value == None:
                    self.node2 = Node(value)
                    Node.deepest_node = self.node2
                else:
                    self.node2.add(value)                          
        elif self.node1 is None:
             self.node1 = Node(value)
        else:
             self.node1.add(value)
                               
    def delete(self,value):
        if value == self.value:        
            self.value = Node.deepest_node.value if value != Node.deepest_node.value else None
            Node.deepest_node = None          
        elif value >= self.value:
            self.node2.delete(value)
        else:
            self.node1.delete(value)