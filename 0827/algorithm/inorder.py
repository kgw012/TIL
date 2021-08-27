# swea 1231 '중위순회'

def inorder(tree, node):
    if tree[node] == 0:
        return

    global result

    inorder(tree, 2 * node)
    result += tree[node]
    inorder(tree, 2 * node + 1)

    return


if __name__ == '__main__':
    T = 10

    for t in range(1, T+1):
        N = int(input())
        tree = [0 for _ in range(256 + 1)]

        for n in range(N):
            input_data = input().split()
            node = int(input_data[0])
            value = input_data[1]

            tree[node] = value

        result = ''
        inorder(tree, 1)

        print('#{} {}'.format(t, result))
