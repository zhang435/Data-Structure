"""
implementation of min heap structure

insert(val) add the value to the tail, push  up

"""


class Heap(object):
    def __init__(self):
        """
        init the function
        """
        # skip the first element,  so the parent is n /2
        self.ls = [0]
        self.size = 0

    def parent(self, i):
        """
        find the parent of a node
        int -> int
        """
        return self.ls[i // 2]

    def left(self, i):
        """
        get the val of left child
        int -> int
        """
        return self.ls[i * 2]

    def right(self, i):
        """
        get the val of right child
        int -> int
        """
        return self.ls[i * 2 + 1]

    def push_up(self, i):
        """
        move heap to the parent position
        int -> void
        """
        if i == 1:
            return
        if self.ls[i] < self.parent(i):
            # if the children is less than the parent
            tmp = self.parent(i)
            self.ls[i // 2] = self.ls[i]
            self.ls[i] = tmp
            self.push_up(i // 2)

    def insert(self, val):
        """
        add one to the counter
        add the element into the end of the list
        push up the elements
        int -> void
        """
        # add the new item in the heap
        self.size += 1
        self.ls.append(val)
        self.push_up(self.size)

    def pop(self):
        """
        min heap pop, where pop outbthe first element
        return int
        """
        if self.size == 0:
            return None
        self.size -= 1
        self.ls[1], self.ls[-1] = self.ls[-1], self.ls[1]
        res = self.ls.pop()
        self.push_down(1)
        return res

    def push_down(self, i):
        """
        push the node in i's position of the tree to the child level and swap with child
        int  -> void
        """
        left = i * 2 if i * 2 > self.size else i * 2
        right = i * 2 if i * 2 + 1 > self.size else i * 2 + 1

        # if this node is the leaf of the node
        if left == right and left > self.size:
            return
        minchild = left if self.ls[left] < self.ls[right] else right
        if self.ls[minchild] < self.ls[i]:
            tmp = self.ls[minchild]
            self.ls[minchild] = self.ls[i]
            self.ls[i] = tmp
            self.push_down(minchild)

    @staticmethod
    def heapify(ls):
        newheap = Heap()
        for num in ls:
            newheap.insert(num)
        return newheap


ls = [3, 2, 1]
heap = Heap.heapify(ls)
heap.insert(4)
heap.insert(10)
heap.insert(12)
heap.insert(13)
print(heap.ls)
print(heap.pop())
# print(heap.ls)
print(heap.pop())
# print(heap.ls)
print(heap.pop())
# print(heap.ls)
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
