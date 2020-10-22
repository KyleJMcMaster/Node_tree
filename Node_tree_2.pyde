class Node:

    def __init__(self, value, level=None, dir=None, parent_node=None):
        self.Left = None
        self.Right = None
        self.value = value
        
        if parent_node is None:
            self.parent_node = 0
            self.is_root = True
        else:
            self.parent_node = parent_node
            self.is_root = False
        if dir is None:
            self.dir = True
        else:
            self.dir = dir
        if level is None:
            self.level = 1
        else:
            self.level = level
        if parent_node is None:
             self.xPos = width/2
        else:   
            if self.dir:
                self.xPos = parent_node.xPos - width/2 ** level
            else:
                self.xPos = parent_node.xPos + width/2 ** level      
            

    def insert(self, data):

        if data <= self.value:
            if self.Left is None:
                self.Left = Node(data, self.level +1, dir=True, parent_node=self)
            else:
                self.Left.insert(data)
        else:
            if self.Right is None:
                self.Right = Node(data, self.level +1, dir=False, parent_node = self)
            else:
                self.Right.insert(data)

    def print_tree(self):

        if self.Left:
            self.Left.print_tree()
            print(self.value)
        if self.Right:
            self.Right.print_tree()
            
    def draw_tree(self):
        stroke(255)
        if self.parent_node:
            line(self.xPos, 100 * self.level, self.parent_node.xPos, 100 * (self.level -1))
        
        if self.level < 4:
            ellipse(self.xPos, (100* self.level), 45, 45)   
             
        else:
            ellipse(self.xPos, (100 * self.level), 70/(2**self.level-2), 70/(2**self.level-2))
            
        fill(0, 102, 153)
        textAlign(CENTER)
        text(self.value, self.xPos, (100* self.level))
        fill(255)
        
        
        
        if self.Left:
            self.Left.draw_tree()

        if self.Right:
            self.Right.draw_tree()
            
            
    def reorg(self, num_array, root):
        root = Node(self.value)
        for i in range(len(num_array)):
            root.insert(num_array[i])
            
            
    def delete_tree(self):
        if self.Left:
            self.Left.delete_tree()
        if self.Right:
            self.Right.delete_tree()
        del self
        
        


width = 1200
root = Node(50000)
num_list = [root.value]

def setup():
    size(1200,800)
    
def mouseClicked():
    x = int(random(100000))
    root.insert(x)
    num_list.append(x)

def keyReleased():
    return True

def draw():
    
    background(200)
    root.draw_tree()
    #print(num_list)
