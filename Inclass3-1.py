class Node:
    def __init__(self, data):
        self.data = data  # storing the data
        self.next = None  # Pointer to the next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        new_node = Node(data)  # Create the node
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # traverse to the end of the list
            last_node = last_node.next
        last_node.next = new_node  # link last node to the new node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # link the new node to the current head
        self.head = new_node  # update the head to the new node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')


if __name__ == '__main__':
    linkedlist = SinglyLinkedList()
    linkedlist.append(10)
    linkedlist.append(20)
    linkedlist.append(30)
    linkedlist.prepend(5)
    linkedlist.print_list()
