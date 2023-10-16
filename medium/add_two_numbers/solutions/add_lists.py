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

        def add_lists(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            new_node = ListNode(digit)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            new_node.next = add_lists(l1, l2, carry)

            return new_node

        return linkedlist_to_list(add_lists(l1, l2, 0)) # type convertion for test cases