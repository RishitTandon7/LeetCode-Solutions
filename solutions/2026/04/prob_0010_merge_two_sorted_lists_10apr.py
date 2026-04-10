from typing import List, Optional

class Solution:
    def mergeTwoLists(self, l1: Optional[List[int]], l2: Optional[List[int]]) -> Optional[List[int]]:
        """
        Approach: We will use a two-pointer technique to compare elements from both lists and add the smaller one to our result list.
        
        Time Complexity: O(n + m) where n and m are the lengths of the input lists. This is because we need to traverse each element in both lists once.
        
        Space Complexity: O(n + m) as well, since we will be creating a new list that contains all elements from both input lists.
        """
        # Initialize an empty list to store our result
        result = []
        
        # Initialize two pointers, one for each list
        i = j = 0
        
        # Traverse both lists until we reach the end of either one
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                # If the current element in l1 is smaller, add it to our result list and move the pointer forward
                result.append(l1[i])
                i += 1
            else:
                # If the current element in l2 is smaller (or equal), add it to our result list and move the pointer forward
                result.append(l2[j])
                j += 1
        
        # At this point, we have traversed one of the lists completely. Add any remaining elements from the other list to our result.
        while i < len(l1):
            result.append(l1[i])
            i += 1
        while j < len(l2):
            result.append(l2[j])
            j += 1
        
        # Return our result list
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists([1, 2, 3], [4, 5, 6]))  # Expected: [1, 2, 3, 4, 5, 6]
    print(s.mergeTwoLists([], [0, 1, 2]))  # Expected: [0, 1, 2]
    print(s.mergeTwoLists([0], []))  # Expected: [0]