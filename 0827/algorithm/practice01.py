def dfs(node):
    if node == 0:
        return

    global left
    global right

    print(node)
    left_node = left[node]
    right_node = right[node]

    dfs(left_node)
    dfs(right_node)
    return


if __name__ == '__main__':
    left = [0 for _ in range(11)]
    right = [0 for _ in range(11)]

    left[1] = 3
    left[3] = 2
    left[5] = 7
    left[7] = 9
    left[9] = 10

    right[1] = 5
    right[3] = 6
    right[5] = 8
    right[8] = 4

    dfs(1)
