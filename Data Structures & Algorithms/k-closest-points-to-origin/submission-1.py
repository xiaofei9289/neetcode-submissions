class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.get_distance)
        return points[:k]

    def get_distance(self,p):
        return p[0]**2 + p[1]**2
        