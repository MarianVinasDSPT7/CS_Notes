"""An image is represented by a 2-D array of integers, each integer representing 
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) *start row/ start column* representing the starting pixel (row and column) of 
the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 
4-directionally to the starting pixel of the same color as the starting pixel, plus
any pixels connected 4-directionally to those pixels (also with the same color as
the starting pixel), and so on. Replace the color of all of the aforementioned 
pixels with the newColor.

At the end, return the modified image.
"""

from collections import deque

class Solution:
    """
    Understand
    [[1,1,1],
     [2,2,0], valueToChange = 1, newColor = 2
     [1,0,1]]

     Plan
     1. Translate this into graph terminology
     totally possible to convert into a graph
     node = a pixel
     edges = neiboring pixels (up, down, left, right)

     2. Build your graph
     no need to build a graph, just use the matrix to traverse

     3. Traverse
     Start traversing at the starting point, change the color of that starting point
     Traverse the neighbors of that starting point (up, down, left, right)
     If the neighbor has the same original color as the starting point, then change that
     neighbors color as well
        Repeat until all valid neighbors are flood-filled
    """

    def floodFill(self, image, sr, sc, newColor):
        colorToChange = image[sr][sc]
        queue = deque()
        queue.append((sr, sc))
        visited = set()
        numRows, numColumns = len(image), len(image[0])

        while len(queue) > 0:
            currPoint = queue.popleft()
            currRow, currColumn, currPoint[0], currPoint[1]
            if currRow < 0 or currRow >= numRows or currColumn >= numColumns: # out of bounds
                continue
            if image[currRow][currColumn] != colorToChange:
                continue
            if currPoint in visited:
                continue
            visited.add(currPoint)
            image[currRow][currColumn] = newColor
            queue.append((currRow + 1, currColumn))
            queue.append((currRow - 1, currColumn))
            queue.append((currRow, currColumn + 1))
            queue.append((currRow, currColumn - 1))

        return image

# CSPT16/Artem Solution
""" 
Starting at a pixel,
Find all pixels that we need to change

get_neighbors for current_coord
    Look up
        down
        left
        right
        check if each coord has the same value
"""
def flood_fill(image, sr, sc, new_color):
    # Recursive DFS
    def dfs(current_row, current_column):
        # current_row, current_column combine to create a vertex
        # change the current vertex, to a new color
        original_color = image[current_row][current_column]
        image[current_row][current_column] = new_color

        # get all the neighbors
        # look up, down, left, right & recurse on any neighbors
        # look up
        if current_row >= 1 and image[current_row - 1][current_column] == original_color:
            dfs(current_row - 1, current_column)
        
        # look down
        if current_row > len(image)-1 and image[current_row + 1][current_column] == original_color:
            dfs(current_row + 1, current_column)
        
        # look left
        if current_column >= 1 and image[current_row][current_column  - 1] == original_color:
            dfs(current_row, current_column - 1)

        # look right
        if current_column < len(image[0]) - 1 and image[current_row][current_column  + 1] == original_color:
            dfs(current_row, current_column + 1)
    
    dfs(sr, sc)