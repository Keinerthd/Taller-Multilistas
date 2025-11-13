from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def add_child(self, parent: Node, child: Node):
        if parent.sub_list is None:
            sublist = LinkedList()
            sublist.head = child
            sublist.tail = child
            parent.sub_list = sublist
        else:
            current = parent.sub_list.tail
            current.next = child
            child.prev = current
            parent.sub_list.tail = child
        return parent.sub_list

    def search_by_attr(self, attr, value):
        current = self.head
        while current:
            if getattr(current, attr) == value:
                return current
            current = current.next
        return None

    def update_value(self, search_value, **attrs):
        node = self.search_by_attr("id", search_value)
        if node:
            for k, v in attrs.items():
                setattr(node, k, v)
            return True
        return False

    def delete_value(self, search_value):
        current = self.head
        while current:
            if current.id == search_value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def print_multilinked_list(self, level=0):
        if self.head is None:
            print("Empty list")
            return
        
        current = self.head
        while current:
            print("  " * level + str(current))
            if current.sub_list:
                current.sub_list.print_multilinked_list(level + 1)
            current = current.next


"""
# Ejemplo de uso:

from Node import Node

paises = LinkedList()
colombia = Node(1, "Colombia")
peru = Node(2, "Peru")
paises.append(colombia)
paises.append(peru)

# Crear sublistas
cund = Node(1, "Cundinamarca")
bogota = Node(1, "Bogota")

dep_list = paises.add_child(colombia, cund)
dep_list.add_child(cund, bogota)

paises.print_multilinked_list()
"""
