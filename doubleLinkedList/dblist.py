from Node import Node
"""
A implemntation for a double linked list
"""


class Dbls(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def __str__(self):
        return ""

    def addr(self, curr, new_node):
        """
        insert a new node after the current node 
        Node,Node -> Dblist
        """
        res = curr.next
        res.next = new_node
        new_node.prev = curr

        # link the res to the new node

        new_node.next = curr
        curr.prev = new_node

        self.size += 1

        return self.head

    def addl(self, curr, newnode):
        """
        insert a new node before the node 
        """
        prev = curr.prev
        prev.next = newnode
        newnode.prev = prev

        # link back to prev prt
        newnode.next = curr
        curr.prev = newnode

        self.size += 1

        return self.head

    def add_tail(self, val):
        """
        add the ndoe to the end of the while dbls
        val -> Dbls
        """
        return self.addl(self.tail, Node(val))

    def add_head(self, val):
        """
        add the ndoe to the begin of the while dbls
        """
        return self.addr(self.head, Node(val))

    def toDbList(self, ls):
        """
        convert a array to dblist
        """
        for num in ls:
            self.add_tail(num)
        return self

    def __str__(self):
        pointer = self.head.next
        res = ""
        while pointer != self.tail:
            res += str(pointer.val) + " <-> "
            pointer = pointer.next
        res += "None"
        return res


dbls = Dbls().toDbList([1, 3, 5, 7, 9])
print(dbls)
