class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")
    def delete_nth_node(self, n):
        if self.head is None:
            print("Cannot delete from an empty list.")
            return

        if n <= 0:
            print("Invalid index. Index must be greater than 0.")
            return

        if n == 1:
            self.head = self.head.next
            return

        temp = self.head
        count = 1
        while temp is not None and count < n - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            print("Index out of range.")
            return

        temp.next = temp.next.next
my_list = LinkedList()

my_list.add_node(10)
my_list.add_node(20)
my_list.add_node(30)
my_list.add_node(40)

print("Original list:")
my_list.print_list()

my_list.delete_nth_node(3)
print("After deleting 3rd node:")
my_list.print_list()
