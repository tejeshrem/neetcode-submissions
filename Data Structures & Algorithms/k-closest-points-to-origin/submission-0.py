class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''

        input - 5 coordinates     create empty array of len 5 

        iterate through the input

        find the dist from the origin of each given coordinate 

        distance: coordinates 

        array of the distances we've found so far

        use the distances in our array as a key to get the k closest 

        return the k closest 

        '''

        dist_map = defaultdict(list)
        distances = []
        
        def find_distance(x, y) -> float:
            return math.sqrt(x**2 + y**2)

        for x, y in points:
            distance = find_distance(x, y)

            dist_map[distance].append([x, y])
            if distance not in distances:
                distances.append(distance) 

        distances.sort()
        res = []
        for dist in distances:
            for point in dist_map[dist]:
                if k > 0:
                    res.append(point) 
                    k -= 1
        return res 




