from typing import List, Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[List[int]], l2: Optional[List[int]]) -> List[int]:
        """
        Approach: We will use a two-pointer technique to compare elements from both lists and append the smaller one to our result list.
        
        Time Complexity: O(n + m) where n and m are the lengths of the input lists. This is because we are scanning through each element once.
        
        Space Complexity: O(n + m) as in the worst case, all elements will be stored in our result list.
        """
        # Initialize an empty list to store our result
        result = []
        
        # Initialize two pointers, one for each list
        i, j = 0, 0
        
        # Continue until we have scanned through both lists
        while i < len(l1) and j < len(l2):
            # If the current element in l1 is smaller, append it to our result and move the pointer forward
            if l1[i] < l2[j]:
                result.append(l1[i])
                i += 1
            # Otherwise, append the current element from l2 and move its pointer forward
            else:
                result.append(l2[j])
                j += 1
        
        # If there are remaining elements in either list, append them to our result
        while i < len(l1):
            result.append(l1[i])
            i += 1
        while j < len(l2):
            result.append(l2[j])
            j += 1
        
        # Return the merged and sorted list
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists([1,2,3], [4,5,6]))  # Expected: [1,2,3,4,5,6]
    print(s.mergeTwoLists([1], [1]))  # Expected: [1,1]
    print(s.mergeTwoLists([1], [2]))  # Expected: [1,2]