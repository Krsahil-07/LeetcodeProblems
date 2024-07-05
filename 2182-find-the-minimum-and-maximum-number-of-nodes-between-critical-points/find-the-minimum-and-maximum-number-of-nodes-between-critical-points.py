# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head.val
        h1=head.next
        ans=[]
        node=2
        while h1 and h1.next:
            if (h1.val>prev and h1.next.val<h1.val) or (h1.val<prev and h1.next.val>h1.val):
                ans.append(node)
            prev=h1.val
            h1=h1.next
            node+=1
        print((ans))
        if len(ans)==0 or len(ans)==1:
            return [-1,-1]
        elif len(ans)==2:
            return [ans[1]-ans[0],ans[1]-ans[0]]
        else:
            
            minm=ans[1]-ans[0]
            for i in range(1,len(ans)-1):
                minm=min(minm,ans[i+1]-ans[i])
            maxm=ans[-1]-ans[0]
            for ii in range(1,len(ans)-2):
                maxm=max(maxm,ans[ii+1]-ans[ii])
            return [minm,maxm]

        