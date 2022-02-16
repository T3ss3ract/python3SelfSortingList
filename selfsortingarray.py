class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SortedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            previous = None
            while current is not None:
                if current.data > data:
                    break
                previous = current
                current = current.next
            if previous is None:
                new_node.next = self.head
                self.head = new_node
            else:
                previous.next = new_node
                new_node.next = current

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    my_list = SortedList()
    my_list.add(1)
    my_list.add(6)
    my_list.add(3)
    my_list.add(9)
    my_list.add(5)
    my_list.add(2)
    my_list.add(7)
    my_list.add(8)
    my_list.add(4)
    my_list.add(10)
    my_list.print_list()

