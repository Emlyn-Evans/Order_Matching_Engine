class Order:
    def __init__(
        self, order_id=None, order_type=None, price=None, time=None, size=None
    ):

        self.order_id = order_id
        self.order_type = order_type
        self.price = price
        self.time = time
        self.size = size
        self.active = True

    def min(self, order_2):

        if isinstance(self, order_2) is True:

            if self.order_type == order_2.order_type:

                if self.order_type == "buy":

                    if self.price > order_2.price:

                        return 0

                    elif self.price == order_2.price:

                        if self.time <= order_2.time:

                            return 0

                        else:

                            return 1

                    else:

                        return 1

                elif self.order_type == "sell":

                    if self.price < order_2.price:

                        return 0

                    elif self.price == order_2.price:

                        if self.time <= order_2.time:

                            return 0

                        else:

                            return 1

                    else:

                        return 1

                else:

                    raise ValueError("Unknown order type upon comparison")

            else:

                return None


class Node:
    def __init__(self, order, parent, left=None, right=None):

        self.order = order
        self.parent = parent
        self.left = left
        self.right = right


class Heap:
    def __init__(self):

        self.root = None
        self.tail = None

    def get_min(self):

        if root is None:

            return None

        return self.root.order

    def pop(self):

        if self.root is None:

            return None

        if self.root.left is None:

            ret = self.root.order
            self.root = None
            return ret

        order = self.root.order

        # Swap with tail
        self.root.order = self.tail.order
        self.tail.order = None

        # Downheap
        self.downheap(self.root)

        # Find new tail node
        self.find_new_tail()

        return True

    def insert(self, order):

        if order is None:

            return None

        pass

    def remove(self):

        pass

    def upheap(self):

        pass

    def downheap(self, node):

        if node is None:

            return None

        valid = False

        while valid is False:

            left = node.order.min(node.left.order)
            right = node.order.min(node.right.order)
            direction = None

            if left is None:

                if right is None:

                    valid = True

                else:

                    raise Exception(
                        "Complete property not satisfied: last child not leftmost"
                    )

            else:

                if right is None:

                    direction = 0

                else:

                    if left == 1:

                        if right == 1:

                            ret = node.left.order.min(node.right.order)

                            if ret is None:

                                raise ValueError(
                                    "Left or Right child not of type order"
                                )

                            else:

                                if ret == 0:

                                    direction = 0

                                else:

                                    direction = 1

                        else:

                            direction = 0

                    else:

                        if right == 1:

                            direction = 1

                        else:

                            valid = True

            if direction is not None:

                temp = node.order

                if direction == 0:

                    node.order = node.left.order
                    node.left.order = temp
                    node = node.left

                else:

                    node.order = node.right.order
                    node.right.order = temp
                    node = node.right

        return True

    def find_new_tail(self):

        traversing_up = True

        old_tail = self.tail
        node = self.tail

        while traversing_up:

            if node == self.root:

                traversing_up = False

            else:

                if node.parent.right == node:

                    node = node.parent.left
                    traversing_up = False

                node = node.parent

        while node.right is not None:

            node = node.right

        self.tail = node

        if old_tail.parent.right == old_tail:

            old_tail.parent.right = None

        else:

            old_tail.parent.left = None

        return True


class Queue:
    def __init__(self):

        self.head = None
        self.hash = 0
        self.order_ids = {}

    def generate_order_id(self):

        order_id = self.hash
        self.hash += 1

        return order_id

    def pop(self):
        """Removes and returns the node at the head of the queue."""

        pass

    def add(self, price):
        """Adds the node to the queue with time priority.
        Order price must be positive.


        Returns None on failure, or pointer to node on success"""

        pass
