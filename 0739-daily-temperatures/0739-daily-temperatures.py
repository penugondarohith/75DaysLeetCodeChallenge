class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []              # store indices
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res