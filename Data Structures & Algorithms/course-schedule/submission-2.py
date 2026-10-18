class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adjact_table = defaultdict(list)

        for course, prereq in prerequisites:
            adjact_table[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        res_order = []

        while queue:
            cur_course = queue.popleft()
            res_order.append(cur_course)

            for next_course in adjact_table[cur_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return len(res_order) == numCourses