class Node:
    def __init__(self, value: object) -> None:
        """
        Constructor.
        """
        self.value: object = value
        self.next: object = None


class LinkedList:
    def __init__(self: object) -> None:
        """
        Constructor.
        """
        self.head = None

    def prepend(self: object, value: object) -> None:
        """
        Prepend a node to the linked list.

        Parameters
        ----------
        value: object, required
            The value that is used to create the node that is being prepended.
        """
        if self.head is None:
            self.head = Node(value)
        else:
            current_head: Node = self.head
            self.head = Node(value)
            self.head.next = current_head

    def size(self: object) -> int:
        """
        Return the size or length of the linked list.

        Returns
        ----------
        int
            The size of the linked list.
        """
        size: int = 0
        current_node: Node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def to_list(self: object) -> list:
        """
        Create a list representation of the linked list.

        Returns
        ----------
        list
            A list representation of the linked list.
        """
        result_list: list = list()
        if self.head is not None:
            node: Node = self.head
            while node:
                result_list.append(node.value)
                node = node.next

        return result_list
