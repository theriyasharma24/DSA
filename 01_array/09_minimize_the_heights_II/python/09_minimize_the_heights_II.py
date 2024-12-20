class Solution:
     def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        result = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            max_height = max(arr[-1] - k, arr[i - 1] + k)
            min_height = min(arr[0] + k, arr[i] - k)
            result = min(result, max_height - min_height)
        return result

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends

#Time Complexity - O(nlogn)
#Space Complexity - O(1)