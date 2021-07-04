class Node:
    def __init__(self, order_id=None, price=None, next_node=None):

        self.order_id = order_id
        self.price = price
        self.next_node = next_node
        self.active = True


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

        if self.head is None:

            return None

        ret = self.head
        self.head = head.next_node

        del self.order_ids[ret.order_id]

        return ret

    def add(self, price):
        """Adds the node to the queue with time priority.
        Order price must be positive.


        Returns None on failure, or pointer to node on success"""

        if price is None:

            return None

        if price < 0:

            return None

        node = self.head
        new_node = Node(self.generate_order_id(), price)

        # Add map from order id to node in queue
        if new_node.order_id in self.order_ids:

            raise ValueError("New order id already in queue")

        self.order_ids[new_node.order_id] = new_node

        if node is None:

            self.head = new_node

        else:

            while node.next_node != None:

                if node.next_node.price <= price:

                    node = node.next

                else:

                    # Insert node
                    temp = node.next_node
                    node.next_node = new_node
                    new_node.next_node = temp

                    return new_node

            node.next_node = new_node

        return new_node

    def remove(self, order_id):
        """Removes the node from the queue"""

        if order_id is None:

            return None

        if order_id not in self.order_ids:

            return None

        pass

    def get_head(self):

        return self.head
