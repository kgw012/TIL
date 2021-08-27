def preorder(result, node):
    if node == 0:
        return result

    global left
    global right

    result.append(node)
    preorder(result, left[node])
    preorder(result, right[node])

    return result


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        V = int(input())

        left = [0 for _ in range(V + 1)]
        right = [0 for _ in range(V + 1)]

        for _ in range(V - 1):
            p, c = map(int, input().split())
            if left[p] == 0:
                left[p] = c
            else:
                right[p] = c

        pre_list = preorder([], 1)

        print('#{}'.format(t), end=' ')
        print(*pre_list)
