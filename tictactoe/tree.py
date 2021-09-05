class Node:
    def __init__(self, item: None, childs: list = []):
        self.item = item
        self.childs = []
        self.addChilds(childs)

    def addChilds(self, childs: list):
        for child in childs:
            self.add(child)

    def add(self, child):
        if isinstance(child, Node):
            self.childs.append(child)
        else:
            self.childs.append(Node(child))

    def remove(self, child):
        self.childs.remove(child)

    def pop(self, index: int):
        self.childs.pop(index)

    def walk(self, function: None, depth: int = -1):
        if function:
            function(self, depth=depth)
        if depth != 0:
            for child in self.childs:
                child.walk(function, depth=depth - 1)
