class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B =nums1,nums2
        total=len(A) + len(B)
        half = total//2
        if len(B) < len(A):
            A,B =B,A
        l,r = 0, len(A)-1   
        while True:
            mid = (l+r)//2
            j=half - mid - 2
            A_left=A[mid] if mid >=0 else float("-infinity")
            B_left=B[j] if j >=0 else float("-infinity")
            A_rigth=A[mid+1] if (mid + 1) < len(A) else float('infinity')
            B_rigth=B[j+1] if (j+1) < len(B) else float('infinity')
            if A_left <= B_rigth and B_left <= A_rigth:
                if total % 2:
                    return min(A_rigth,B_rigth)
                return (max(A_left,B_left)  +  min(A_rigth,B_rigth) )/2
            elif A_left > B_rigth:
                r=mid -1
            else:
                l=mid +1        
