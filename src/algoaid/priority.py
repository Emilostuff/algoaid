class Item:
    def __init__(self, content, key, i):
        self.content = content
        self.key = key
        self.i = i


class MinHeap:
    def __init__(self):
        self.h = [Item(None, None, 0)]
        self.items = dict()

    def swap(self, a, b):
        self.h[a].i, self.h[b].i = self.h[b].i, self.h[a].i
        self.h[a], self.h[b] = self.h[b], self.h[a]

    def insert(self, x, key):
        if id(x) in self.items:
            raise Exception("Item is already in the MinHeap")
        new_item = Item(x, key, len(self.h))
        self.items[id(x)] = new_item
        self.h.append(new_item)
        self.bubble_up(len(self.h) - 1)

    def bubble_up(self, i):
        p = i >> 1
        if p > 0 and self.h[p].key > self.h[i].key:
            self.swap(p, i)
            self.bubble_up(p)

    def bubble_down(self, i):
        l = i << 1  # noqa
        r = l + 1
        lv = l < len(self.h)
        rv = r < len(self.h)
        if lv and self.h[i].key > self.h[l].key and (not rv or self.h[l].key <= self.h[r].key):  # noqa
            self.swap(l, i)
            self.bubble_down(l)
        elif rv and self.h[i].key > self.h[r].key:
            self.swap(r, i)
            self.bubble_down(r)

    def extract_min(self):
        if len(self.h) < 2:
            raise Exception("Can not extraxt minimum item from empty MinHeap")
        min_item = self.h[1]
        self.h[1] = self.h[-1]
        self.h[1].i = 1
        self.h.pop()
        self.bubble_down(1)
        return min_item.content

    def decrease_key(self, x, new_key):
        if id(x) not in self.items:
            raise Exception("Item is not in the MinHeap")
        item = self.items[id(x)]
        if item.key < new_key:
            raise Exception("Can not decrease key to a higher value")
        item.key = new_key
        self.bubble_up(item.i)

    def min(self):
        if len(self.h) < 2:
            raise Exception("Can not return minimum item from empty MinHeap")
        return self.h[1].content

    def empty(self):
        return len(self.h) < 2

    def print(self):
        print(list(map(lambda i: (i.key, i.content), self.h[1:])))


class MaxHeap:
    def __init__(self):
        self.__heap = MinHeap()

    def insert(self, x, key):
        self.__heap.insert(x, -key)

    def extract_max(self):
        return self.__heap.extract_min()

    def increase_key(self, x, new_key):
        self.__heap.decrease_key(x, -new_key)

    def max(self):
        return self.__heap.min()

    def empty(self):
        return self.__heap.empty()

    def print(self):
        print(list(map(lambda i: (i.content, -i.key), self.__heap.h[1:])))


if __name__ == '__main__':
    # Test minheap
    print("MIN HEAP:")
    q = MinHeap()

    q.insert("C", 4)
    q.insert("E", 10)
    q.insert("F", 12)
    q.insert("D", 5)
    q.insert("B", 2)
    q.insert("G", 14)
    q.insert("A", 19)
    q.print()
    print("min is: ", q.min())
    q.decrease_key("A", 1)
    print("min is: ", q.min())
    while not q.empty():
        print("extracted: ", q.extract_min())

    # Test maxheap
    print("\nMAX HEAP:")
    q = MaxHeap()

    q.insert("F", 4)
    q.insert("D", 10)
    q.insert("C", 12)
    q.insert("E", 5)
    q.insert("G", 2)
    q.insert("B", 14)
    q.insert("A", 1)
    q.print()
    print("max is: ", q.max())
    q.increase_key("A", 19)
    print("max is: ", q.max())
    while not q.empty():
        print("extracted: ", q.extract_max())
