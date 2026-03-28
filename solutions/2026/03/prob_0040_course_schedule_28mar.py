from typing import List, Optional
from collections import defaultdict, deque

class Solution:
    def addEdge(self, u: int, v: int) -> None:
        self.graph[u].append(v)
    
    def dfs(self, node: int, visited: set, path: list) -> bool:
        visited.add(node)
        path.append(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if not self.dfs(neighbor, visited, path):
                    return False
        path.pop()
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            self.addEdge(x, y)

        visited = set()
        for i in range(numCourses):
            if i not in visited:
                if not self.dfs(i, visited, []):
                    return False
        return True

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(4, [[1,0],[2,0],[3,1],[3,2]]))  # Expected: True
    print(s.canFinish(4, [[1,0],[2,0],[3,1],[3,2],[3,0]]))  # Expected: False