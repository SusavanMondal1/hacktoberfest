class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
            low=0
            high=n-1

            while low<=high:
                mid=low+high/2

                if arr[mid]==k:
                    return mid
                elif arr[mid]>k:
                    high=mid-1

                else:
                    low=mid+1

            return -1
