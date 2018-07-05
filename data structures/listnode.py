class listnode():
    def __init__(self, val):
        self.val = val
        self.next = None

class dlistnode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


# 反转链表
def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


l1 = listnode(10)
l2 = listnode(20)
l3 = listnode(30)
l1.next = l2
l2.next = l3

print(reverse(l1).next.val)
