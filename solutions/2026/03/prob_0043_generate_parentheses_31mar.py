from typing import List, Optional
import itertools

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Approach: 
        Time Complexity: O(4^n / n^(3/2))
        Space Complexity: O(4^n / n^(3/2))
        """
        # Generate all possible combinations of (left, right) pairs
        pairs = list(itertools.product(range(n), range(n)))
        
        def is_valid(p):
            left, right = 0, 0
            for l, r in p:
                if l > n or r > n:
                    return False
                left += l
                right += r
            return left == right
        
        # Filter out invalid combinations
        valid_pairs = [p for p in pairs if is_valid(p)]
        
        def generate(s, left, right):
            if len(s) == 2 * n:
                result.append(''.join(map(str, s)))
                return
            
            for l in range(left, n + 1):
                for r in range(right, n + 1):
                    if l != r and l <= n - r:
                        new_s = list(s)
                        new_s.append(l)
                        generate(new_s, l + 1, r)
                        new_s.pop()
                        new_s.append(r)
                        generate(new_s, l + 1, r + 1)
        
        result = []
        generate([], 0, 0)
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))  # Expected: ['((()))', '(()())', '(())()', '()(())', '()()()' ]