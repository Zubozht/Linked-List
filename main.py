class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
        def __init__(self):
            self.head = None

        def __str__(self):
            return self.printlist()

        def __iter__(self):
            for i in self.listasiter():
                yield i

        def printlist(self):
            if self.head is None:
                return 'The linked list is empty.'
            ll_output = ''
            current_node = self.head
            while current_node:
                ll_output += current_node.data + ' --> '
                current_node = current_node.next
            return ll_output

        def listasiter(self):
            elements = []
            if self.head is not None:
                current_node = self.head
                while current_node:
                    elements.append(current_node.data)
                    current_node = current_node.next
            return elements


        def listgetelement(self, index):
            if self.head is None:
                return 'The linked list is empty.'
            if index < 0 or index >= self.listlen():
                return 'Index out of range.'
            lcount = 0
            current_node = self.head
            while lcount != index:
                lcount += 1
                current_node = current_node.next
            return current_node.data

        def listappend(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current_node = self.head
                while current_node.next:
                    current_node = current_node.next
                current_node.next = new_node
                return

        def listprepend(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node

        def listinsertarr(self, data):
            for el in data:
                self.listappend(el)

        def listindexinsert(self, data, index):
            listlen = self.listlen()
            if index < 0 or index > listlen:
                print('Index out of range.')
            else:
                new_node = Node(data)
                if index == 0:
                    self.listprepend(data)
                elif index == listlen:
                    self.listappend(data)
                else:
                    lcount = 0
                    current_node = self.head
                    while lcount != index-1:
                        lcount += 1
                        current_node = current_node.next
                    new_node.next = current_node.next
                    current_node.next = new_node


        def listlen(self):
            if self.head is None:
                return 0
            else:
                current_node = self.head
                lcount = 0
                while current_node:
                    lcount += 1
                    current_node = current_node.next
                return lcount

        def listdelete(self, data):
            if self.head is None:
                print('The linked list is empty.')
            else:
                current_node = self.head
                if current_node.data == data:
                    self.head = current_node.next
                else:
                    while current_node.next and current_node.next.data != data:
                        current_node = current_node.next
                    if current_node.next and current_node.next.data == data:
                        current_node.next = current_node.next.next
                    else:
                        print('Given element not found in the linked list.')

        def listremovefirst(self):
            if self.head is None:
                print('The linked list is empty.')
            else:
                self.head = self.head.next

        def listindexremove(self, index):
            listlen = self.listlen()
            if self.head is None:
                print('The linked list is empty.')
                return
            if index < 0 or index >= listlen:
                print('No element found at the given index.')
                return
            if index == 0:
                self.listremovefirst()
                return
            lcount = 0
            current_node = self.head
            while lcount != index-1:
                lcount += 1
                current_node = current_node.next
            current_node.next = current_node.next.next


        def listreverse(self):
            if self.head is None:
                print('The linked list is empty.')
            if self.head.next is None:
                return self.printlist()
            else:
                prev = None
                current = self.head
                next = current.next
                while current:
                    if next is None:
                        current.next = prev
                        self.head = current
                        return self.printlist()
                    current.next = prev
                    prev = current
                    current = next
                    next = next.next