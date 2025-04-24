"""
Task:
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.
To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.
land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].
Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.
https://leetcode.com/problems/find-all-groups-of-farmland/description/
"""
class Solution(object):
	def findFarmland(self, land):
		"""
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
		groups = []
		h = len(land)
		w = len(land[0])

		for i in range(h):
			for j in range(w):
				if land[i][j] == 1 and not ((j != 0 and land[i][j-1] == 1) or (i != 0 and land[i-1][j] == 1)):	# the top-left (not a part of current field on thr rigth or bellow)
					x = j
					y = i
					for k in range(i, h):
						if land[k][x] == 0:
							y = k-1			# the downest cell of the farmland
							break
						if (k == h-1):
							y = k
							break
					for k in range(j, w):
						if land[y][k] == 0:
							x = k-1 			# the rightest cell of the framland
							break
						if (k == w-1):
							x = k
							break

					groups.append([i, j, y, x])

		return groups
