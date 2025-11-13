class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None
        self.prev = None
        self.sub_list = None   # apunta a otra LinkedList
    
        self.lat = None
        self.lon = None

        def __str__(self):
            return f"{self.id} - {self.name}"