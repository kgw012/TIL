def preorder(lst, node):
    if node == 0:
        return

    global left
    global right

    lst.append(node)
    preorder(lst, left[node])
    preorder(lst, right[node])

    return


def postorder(lst, node):
    if node == 0:
        return

    global left
    global right

    postorder(lst, left[node])
    postorder(lst, right[node])
    lst.append(node)

    return


def inorder(lst, node):
    if node == 0:
        return

    global left
    global right

    inorder(lst, left[node])
    lst.append(node)
    inorder(lst, right[node])


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

    pre_list = []
    preorder(pre_list, 1)
    print(*pre_list)

    post_list = []
    postorder(post_list, 1)
    print(*post_list)

    in_list = []
    inorder(in_list, 1)
    print(*in_list)
