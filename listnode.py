class linkedlistnode():
    def __init__(self, val):
        self.val = val
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


l1 = linkedlistnode(10)
l2 = linkedlistnode(20)
l3 = linkedlistnode(30)
l1.next = l2
l2.next = l3

print(reverse(l1).next.val)
