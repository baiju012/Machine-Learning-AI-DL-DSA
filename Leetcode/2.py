# Input: Two linked lists l1 and l2 representing two non-negative integers.
# The digits are stored in reverse order, meaning the 1's digit is at the head of the list.
# Example: l1 = [2 -> 4 -> 3] and l2 = [5 -> 6 -> 4] represent the numbers 342 and 465.
# Output: A linked list representing the sum of the two input numbers.
# For the example above, the output should be [7 -> 0 -> 8], which represents 807.



# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
# self.val = x
# self.next None

class Solution:
  def addTwoNumber(self, l1: ListNode, l2: ListNode) -> ListNode:
    left = 0
    dummy = cur = ListNode(-1)
    while l1 or l2 or left:
      left, sm = divmod(sum(1 and 1.val or 0 for 1 in (l1, l2)) +left, 10)
      cur.next = cur = ListNode(sm)
      l1 = l1 and l1.next
      l2 = l2 and l2.next
    return dummy.next 







class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = 0  # Carry-over value (initially zero)
        dummy = cur = ListNode(-1)  # Dummy node to serve as the start of the result list
        
        while l1 or l2 or left:  # Loop continues as long as there are digits to add or a carry-over
            # Compute the sum of the current digits plus carry-over
            left, sm = divmod(sum(l and l.val or 0 for l in (l1, l2)) + left, 10)
            
            # Create a new node with the computed digit and move the current pointer
            cur.next = cur = ListNode(sm)
            
            # Move to the next nodes in the lists
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        
        return dummy.next  # Return the next node after the dummy (the start of the result list)
