#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened using DFS.
    Args:
        boxes (List[List[int]]): A list of lists representing locked boxes and their keys.
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    def dfs(box, visited):
        visited[box] = True
        for key in boxes[box]:
            if not visited[key]:
                dfs(key, visited)

    n = len(boxes)
    visited = [False] * n
    dfs(0, visited)  # Start DFS from the first box

    return all(visited)
