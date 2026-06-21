# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while True:
            min_idx = -1
            min_val = None

            for i, node in enumerate(lists):
                if node is not None:
                    if min_val is None or node.val < min_val:
                        min_val = node.val
                        min_idx = i

            if min_idx == -1:
                break


            chosen = lists[min_idx]
            lists[min_idx] = chosen.next
            tail.next = chosen
            tail = tail.next

        tail.next = None
        return dummy.next
        