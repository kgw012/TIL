def preorder(node):
    if node == 0:
        return

    global left
    global right

    print(node, end=' ')
    preorder(left[node])
    preorder(right[node])

    return


def postorder(node):
    if node == 0:
        return

    global left
    global right

    postorder(left[node])
    postorder(right[node])
    print(node, end=' ')

    return


def inorder(node):
    if node == 0:
        return

    global left
    global right

    inorder(left[node])
    print(node, end=' ')
    inorder(right[node])


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

    preorder(1)
    print()
    postorder(1)
    print()
    inorder(1)
    print()