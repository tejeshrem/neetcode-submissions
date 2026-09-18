class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair:pair[0])

        output = [intervals[0]]

        for start, end in intervals:
            final = output[-1][1]

            if start <= final:
                output[-1] = [output[-1][0], max(end, output[-1][1])]
            else:
                output.append([start, end])

        return output