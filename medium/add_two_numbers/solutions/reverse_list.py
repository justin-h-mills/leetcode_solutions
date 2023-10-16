from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ******* TYPE CONVERTION FOR TEST CASES **********
def list_to_linkedlist(to_convert):
    head = ListNode()
    dummy_node = head

    for i in range(len(to_convert)):
        dummy_node.val = to_convert[i]

        try:
            new_node = ListNode(to_convert[i+1])
        except:
            new_node = None
              
        dummy_node.next = new_node
        dummy_node = new_node
    
    return head

def linkedlist_to_list(to_convert: ListNode):
    temp_list = list()

    while to_convert != None:
        temp_list.append(to_convert.val)
        to_convert = to_convert.next
    return temp_list

# *************************************************

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list_to_linkedlist(l1) # type convertion for test cases
        l2 = list_to_linkedlist(l2) # type convertion for test cases

        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        l1 = reverse_list(l1)
        l2 = reverse_list(l2)

        carry = 0
        dummy_head = ListNode()
        current = dummy_head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return linkedlist_to_list(dummy_head.next) # type convertion for test cases