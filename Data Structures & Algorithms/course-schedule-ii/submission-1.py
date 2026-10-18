

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        adj_table = defaultdict(list)

        for course, prereq in prerequisites:
            adj_table[prereq].append(course)
            in_degree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        res_order = []

        while queue:
            cur_course = queue.popleft()
            res_order.append(cur_course)

            for next_course in adj_table[cur_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return res_order if len(res_order) == numCourses else []