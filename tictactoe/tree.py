from typing import (
    Dict,
    Any,
    Callable
)

class Node:
    def __init__(self, item: Any = None, childs: Dict = {}):
        self.item = item
        self.childs = {}
        self.addChilds(childs)

    # Add child nodes
    #
    # :param childs: child node dictionary
    def addChilds(self, childs: Dict):
        for key in childs:
            self.add(key, childs[key])

    # Add child node with key
    # Already registered keys will be replaced
    #
    # :param key: node key
    # :param child: child node
    def add(self, key: Any, child: Any):
        node = child
        if not isinstance(node, Node):
            node = Node(child)
        self.childs[key] = node

    # Remove child node
    #
    # :param key: child node key
    def remove(self, key: Any):
        if key in self.childs:
            del self.childs[key]

    # Walk through child nodes and their children
    #
    # :param function: function to execute for every node, including current node
    # :param depth: number of layers to process (-1 for infinite)
    def walk(self, function: Callable, depth: int = -1):
        function(self, depth=depth)
        if depth != 0:
            for key in self.childs:
                self.childs[key].walk(funciton, depth=depth - 1)
