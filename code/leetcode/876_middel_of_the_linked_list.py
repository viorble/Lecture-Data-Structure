class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        
        # 快慢指針移動
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def traverse(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next

# initiate a linked list    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

head = node1

my_list = Solution()
middle = my_list.middleNode(head)
my_list.traverse(middle)


