class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_linked_list(numbers: list)-> Node:
    head = prev = None
    for number in numbers:
        node = Node(number)

        if head is None:
            head = prev = node
        else:
            prev.next = node
            prev = node

    return head


def print_linked_list(head: Node):
    print("\nHere are the nodes in the linked list:\n")
    while head is not None:
        print(head.val)
        head = head.next


def reverse_linked_list(head: Node)-> Node:
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


input_1 = [1, 2, 3, 4, 5]
head = create_linked_list(input_1)
print_linked_list(head)
reversed_head = reverse_linked_list(head)
print_linked_list(reversed_head)