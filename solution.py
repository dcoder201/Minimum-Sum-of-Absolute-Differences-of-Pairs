class Solution:
    def findMinSum(self, A,B,N):
        s=0
        A.sort()
        B.sort()
        for i in range(N):
            s+=abs(A[i]-B[i])
        return(s)
