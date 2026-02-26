class Solution:
    def addCourse(self, courseSchedule: List[List[int]], numCourses: int) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 1
            return True

        for course in courseSchedule:
            graph[course[0]].append(course[1])

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True