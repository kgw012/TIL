def preorder(values, lst, node):
    if node >= len(values) or values[node] == 0:
        return lst

    lst.append(values[node])
    preorder(values, lst, 2*node)
    preorder(values, lst, 2*node + 1)

    return lst


def inorder(values, lst, node):
    if node >= len(values) or values[node] == 0:
        return lst

    inorder(values, lst, 2*node)
    lst.append(values[node])
    inorder(values, lst, 2*node + 1)

    return lst


def postorder(values, lst, node):
    if node >= len(values) or values[node] == 0:
        return lst

    postorder(values, lst, 2*node)
    postorder(values, lst, 2*node + 1)
    lst.append(values[node])

    return lst


if __name__ == '__main__':
    values = [0 for _ in range(33)]
    values[1] = 1
    values[2] = 3
    values[3] = 5
    values[4] = 2
    values[5] = 6
    values[6] = 7
    values[7] = 8
    values[12] = 9
    values[15] = 4
    values[24] = 10

    pre_list = preorder(values, [], 1)
    in_list = inorder(values, [], 1)
    post_list = postorder(values, [], 1)

    print(*pre_list)
    print(*in_list)
    print(*post_list)
