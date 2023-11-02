"""
Module fourth algo lab
"""
import collections


def count_islands(map_islands):
    """
    Function to count number of islands in map
    :param map_islands:  matrix of islands
    :return: number islands
    """

    if not map_islands:
        return 0

    rows = len(map_islands)
    cols = len(map_islands[0])
    num_islands_in_map = 0
    visited_elems = set()

    def bfs(start_row, start_col):
        queue = collections.deque()
        visited_elems.add((start_row, start_col))
        queue.append((start_row, start_col))

        while queue:
            # Directions:
            #     X  X   X
            #      \ | /
            #   X <- 1 -> X
            #      / | \
            #     X  X  X
            directions = [
                [-1, -1],
                [-1, 0],
                [-1, 1],
                [0, -1],
                [0, 1],
                [1, -1],
                [1, 0],
                [1, 1],
            ]
            row, col = queue.popleft()
            for d_row, d_col in directions:
                if (
                    row + d_row in range(rows)
                    and col + d_col in range(cols)
                    and map_islands[row + d_row][col + d_col] == 1
                    and (row + d_row, col + d_col) not in visited_elems
                ):
                    queue.append((row + d_row, col + d_col))
                    visited_elems.add((row + d_row, col + d_col))

    for i in range(rows):
        for j in range(cols):
            if map_islands[i][j] == 1 and (i, j) not in visited_elems:
                bfs(i, j)
                num_islands_in_map += 1

    return num_islands_in_map


if __name__ == "__main__":
    # beautiful_map_to_count_islands = [
    #     ["0",  1,   1,  "0", "0", "0", "0",  1,   1,  "0"],
    #     ["0",  1,   1,   1,   1,  "0", "0", "0",  1,   1 ],
    #     [ 1,   1,  "0", "0", "0", "0", "0", "0",  1,   1 ],
    #     [ 1,  "0", "0", "0", "0",  1,  "0", "0", "0", "0"],
    #     ["0", "0",  1,  "0", "0",  1,  "0", "0", "0",  1 ],
    #     [ 1,  "0", "0", "0", "0", "0", "0", "0", "0",  1 ],
    #     [ 1,   1,   1,   1,  "0",  1,   1,   1,   1,   1 ],
    #     [ 1,   1,   1,   1,  "0",  1,   1,   1,   1,  "0"],
    #     ["0",  1,   1,   1,  "0", "0", "0", "0",  1,   1 ],
    #     ["0", "0", "0", "0", "0",  1,  "0", "0", "0", "0"]
    # ]

    map_to_count_islands = [
        [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    ]

    print(count_islands(map_to_count_islands))
