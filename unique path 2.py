class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        t = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    t[i][j] = 0

        for i in range(m):
            if t[i][0] == 0:
                while i < m:
                    t[i][0] = 0
                    i = i + 1
            else:
                t[i][0] = 1

        for j in range(n):
            if t[0][j] == 0:
                while j < n:
                    t[0][j] = 0
                    j = j + 1
            else:
                t[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if t[i][j] != 0:
                    t[i][j] = t[i][j - 1] + t[i - 1][j]

        for val in t:
            print(val)


if __name__ == '__main__':
    obstacleGrid = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    Solution().uniquePathsWithObstacles(obstacleGrid)
