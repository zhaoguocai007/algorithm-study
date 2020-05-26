"""
链表学习
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        cursor = self.head
        while cursor.next is not None:
            count = count + 1
            cursor = cursor.next
        return count

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def add(self):
        pass

    def append(self, value):
        node = Node(value)
        if self.is_empty():  # 如果为空链表则添加的第一个node为head
            self.head = node
        else:
            cursor = self.head
            while True:
                if cursor.next is None:
                    cursor.next = node
                    break
                cursor = cursor.next

    def items(self):
        pass

    def remove(self):
        pass

    def query(self):
        pass


if __name__ == '__main__':
    s = SingleLinkedList()
    print(s.is_empty())

    s.append(1)
    s.append(1)
    s.append(1)
    print(s.is_empty())
    print(s.length())
    print("---")

