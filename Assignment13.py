
# create a class to handle the Nodes
class Node:
    def __init__(self, data):
        self.data = data # This is the data of the node
        self.next = None # Pointer to the next node, normally set to None

class LinkedList:
    def __init__(self):
        self.head = None # Starting with an empty linked list

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if not self.head:
            print("List is empty. Nothing to remove")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print("Node with data provided wasn't found! Data is: ", data)

    def pfun(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


llist = LinkedList()

llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)

print("Original List: ")
llist.pfun()

llist.remove(30)
llist.remove(60)

print("New List: ")
llist.pfun()
