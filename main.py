class Node:
    def __init__(self, data):
        self.data = data,
        self.next = None

class LinkedList:
        def __init__(self):
            self.head = None

        def printlist(self):
            if self.head is None:
                print('The linked list is empty')
            else:
                current_node = self.head
                while current_node:
                    print(current_node.data)
                    current_node = current_node.next

        def listappend(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current_node = self.head
                while current_node:
                    if current_node.next:
                        current_node = current_node.next
                    else:
                        current_node.next = new_node
                        return

if __name__ == '__main__':
    myll = LinkedList()
    myll.printlist()
    myll.listappend('apple')
    myll.listappend('pineapple')
    myll.listappend('orange')
    myll.printlist()