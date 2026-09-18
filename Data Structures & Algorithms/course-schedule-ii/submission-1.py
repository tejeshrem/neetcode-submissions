class Solution:
    def findOrder(self, numCourses, prerequisites):
        prereq = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False

            # None means completely processed
            if prereq[crs] is None:
                return True

            cycle.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)

            # mark as fully processed
            prereq[crs] = None

            output.append(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output