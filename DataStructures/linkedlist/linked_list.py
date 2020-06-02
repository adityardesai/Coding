class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def _add_to_beginning(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def _append(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current != None:
                current = current.next

            current.next = temp

    def _search(self, key):
        if self.head is None:
            return

        current = self.head
        while current != None and current.data != key:
            current = current.next

        if current is None: return False
        if current.data == key: return True

    def __repr__(self):
        current = self.head
        print_list = []
        while current != None:
            print_list.append(current.data)
            current = current.next

        print(print_list)

    def _remove(self, key):
        "remove only the first occurence"

        if self.head is None: return

        previous = None
        current = self.head

        while current != None and current.data != key:
            previous = current
            current = current.next

        if previous is None:
            self.head = current.next
        elif current:
            previous.next = current.next
            current.next = None


def main():
    ll = LinkedList()
    ll._add_to_beginning(5)
    ll._add_to_beginning(50)
    ll._add_to_beginning(100)
    ll.__repr__()

    #print (ll._search(50))
    print(ll._search(-50))

    ll._remove(100)
    ll.__repr__()


if __name__ == '__main__':
    main()
