# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f'Node data: {self.val}'

class Solution(object):

    def mergeTwoLists(self, l1, l2):

        

mySolution = Solution()
mySolution.mergeTwoLists([1,2,4], [1,3,4])
# print(mySolution)