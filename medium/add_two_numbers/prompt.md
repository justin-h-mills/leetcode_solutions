# **[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)**


## **Prompt:**

You are given two **non-empty** linked lists representing two non-negative integeers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers do not contain any leading zero, except the number 0 itself.

### **Example 1:**

```
(2) -> (4) -> (3) l1
(5) -> (6) -> (4) l2
(7) -> (0) -> (8) result

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

### **Example 2:**

```
(0) l1
(0) l2
(0) result

Input: l1 = [0], l2 = [0]
Output: [0]
```

### **Example 3:**

```
(9) -> (9) -> (9) -> (9) -> (9) -> (9) -> (9)        l1
(9) -> (9) -> (9) -> (9)                             l2
(8) -> (9) -> (9) -> (9) -> (0) -> (0) -> (0) -> (1) result

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

### **Constraints**

* The number of nodes in each linked list is in the range $[1, 100]$

* $0 <= Node.val <= 9$

* It is guaranteed that the list represents a number that does not have leading zeros.

### **initial code:**

``` python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optiona[ListNode]:
```

<br>

## **Add Lists**

The "Add Lists" solution adds two numbers represented by linked lists in reverse order. It processes the digits one by one, considering carry values for overflow, and returns a new linked list as the result.

### **Pseudocode**

```
1. Define a function called addTwoNumbers that takes two ListNode objects, l1 and l2, and returns a ListNode.
2. Define an inner function called add_lists that takes l1, l2, and a carry value as parameters.
3. In add_lists:
   a. If both l1 and l2 are None and carry is 0, return None.
   b. Set val1 to the value of l1.val if l1 is not None, otherwise set it to 0.
   c. Set val2 to the value of l2.val if l2 is not None, otherwise set it to 0.
   d. Calculate the total sum of val1, val2, and carry.
   e. Calculate carry as the integer division of total by 10.
   f. Calculate digit as the remainder of the total when divided by 10.
   g. Create a new ListNode called new_node with the value of digit.
   h. Update l1 to the next node if l1 is not None, otherwise set l1 to None.
   i. Update l2 to the next node if l2 is not None, otherwise set l2 to None.
   j. Set new_node's next attribute to the result of a recursive call to add_lists with updated l1, l2, and carry.
4. Return the result of calling add_lists with l1, l2, and an initial carry value of 0.
```

### **Solution Code**

``` python
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        return add_lists(l1, l2, 0)
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(max(m, n))$, where m = length of l1 & n = length of l2.

* Space Complexity: $O(max(m, n))$, where m = length of l1 & n = length of l2.

<br>

## **Iterative**

The "Iterative" solution also adds two numbers from linked lists in reverse order, but it does so iteratively without recursion. It maintains a carry value and constructs the result linked list as it goes.

### **Pseudocode**

```
1. Initialize a new ListNode as 'solution' and set it to 0.
2. Create a 'dummy_head' ListNode and set it equal to 'solution'.
3. Initialize a 'carry' variable to 0.
4. While there are elements in 'l1', 'l2', or there's a 'carry':
   a. Get the value from 'l1' (if exists) or set it to 0.
   b. Get the value from 'l2' (if exists) or set it to 0.
   c. Calculate the sum of 'value_l1', 'value_l2', and 'carry' and store the carry and result.
   d. Create a new ListNode 'out' with the calculated result.
   e. Connect 'dummy_head' to 'out' as the next ListNode.
   f. Move 'dummy_head' to the newly created 'out'.
   g. Move 'l1' to the next element (if exists) or set it to None.
   h. Move 'l2' to the next element (if exists) or set it to None.
5. Return the 'next' of 'solution' as the result.
```

### **Solution Code**

``` python
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = ListNode(0)
        dummy_head = solution
        carry = 0
        
        while l1 or l2 or carry:
            value_l1 = (l1.val if l1 else 0)
            value_l2 = (l2.val if l2 else 0)
            
            carry, out = divmod(value_l1 + value_l2 + carry, 10)
            
            dummy_head.next = ListNode(out)
            dummy_head = dummy_head.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return solution.next
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(max(m, n))$, where m = length of l1 & n = length of l2.

* Space Complexity: $O(max(m, n))$, where m = length of l1 & n = length of l2.

<br>

## **Reverse List**

The "Reverse List" solution reverses the input lists, adds the digits in the correct order, and then reverses the result back. This approach simplifies handling the input lists but involves reversing the result at the end.

### **Pseudocode**

```
1. Define a function 'reverse_list' that takes a 'head' as input.
   a. Initialize 'prev' as None.
   b. Initialize 'current' as 'head'.
   c. While 'current' is not None:
      i. Set 'next_node' as the next node of 'current'.
      ii. Set the 'next' of 'current' to 'prev'.
      iii. Update 'prev' to 'current'.
      iv. Update 'current' to 'next_node'.
   d. Return 'prev' as the reversed list.
2. Reverse 'l1' using the 'reverse_list' function.
3. Reverse 'l2' using the 'reverse_list' function.
4. Initialize 'carry' to 0.
5. Create a 'dummy_head' ListNode.
6. Set 'current' as 'dummy_head'.
7. While 'l1' or 'l2' or 'carry' have elements:
   a. Get 'val1' from 'l1' (if 'l1' exists) or set it to 0.
   b. Get 'val2' from 'l2' (if 'l2' exists) or set it to 0.
   c. Calculate 'total' as the sum of 'val1', 'val2', and 'carry'.
   d. Update 'carry' as the integer division of 'total' by 10.
   e. Create a new ListNode with the value 'total % 10' and set it as the 'next' of 'current'.
   f. Update 'current' to the newly created ListNode.
   g. If 'l1' exists, move 'l1' to the next element.
   h. If 'l2' exists, move 'l2' to the next element.
8. Reverse the list starting from 'dummy_head.next' using the 'reverse_list' function.
9. Return the reversed list.
```

### **Solution Code**

``` python
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

        return reverse_list(dummy_head.next)
```

### **Time and Space Complexity Analysis**

* Time Complexity: $O(max(m, n))$, where m = length of l1 & n = length of l2.

* Space Complexity: $O(max(m, n))$, where m = length of l1 & n = length of l2.