class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
        def __init__(self):
            self.head = None

        def printlist(self):
            if self.head is None:
                return 'The linked list is empty.'
            ll_output = ''
            current_node = self.head
            while current_node:
                ll_output += current_node.data + ' --> '
                current_node = current_node.next
            return ll_output

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
                while current_node:
                    if current_node.next:
                        current_node = current_node.next
                    else:
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
            if index < 0 or index > self.listlen():
                print('Index out of range.')
            else:
                new_node = Node(data)
                if self.head is None:
                    self.head = new_node
                elif index == 0:
                    self.listprepend(data)
                elif index == self.listlen():
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
                    while current_node.next.next and current_node.next.data != data:
                        current_node = current_node.next
                    if current_node.next.data == data:
                        current_node.next = current_node.next.next
                    else:
                        print('Given element not found in the linked list.')

        def listindexremove(self, index):
            if self.head is None:
                print('The linked list is empty.')
                return
            if index < 0 or index >= self.listlen():
                print('No element found at the given index.')
                return
            lcount = 0
            current_node = self.head
            while lcount != index:
                lcount += 1
                current_node = current_node.next
            self.listdelete(current_node.data)


        def listreverse(self):
            if self.head is None:
                print('The linked list is empty.')
            if self.listlen() == 1:
                return self.printlist()
            else:
                new_head = self.listgetelement(self.listlen()-1)
                if self.head.data == new_head :
                    return self.printlist()

                self.listreverse()



if __name__ == '__main__':
    myll = LinkedList()
    #print(myll.printlist())
    myll.listappend('apple')
    myll.listappend('pineapple')
    myll.listappend('orange')
    myll.listprepend('dragonfruit')
    myll.listdelete('apple')
    myll.listinsertarr(['1','2','3','4','5','6'])
    myll.listindexremove(8)
    myll.listindexinsert('new fruit', 0)
    print(myll.listlen())
    print(myll.printlist())
    print('reversed: ', myll.listreverse())