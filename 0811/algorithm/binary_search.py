def binary_search(arr, num):

    st = 0
    ed = len(arr)

    while st < ed:
        md = (st + ed) // 2
        if arr[md] == num:
            return md
        elif arr[md] < num:
            st = md + 1
            continue
        else:
            ed = md

    return -1




if __name__=='__main__':

    arr = [2 * i for i in range(50)]

    for i in range(100):
        result = binary_search(arr, i)
        if result == -1:
            print('못 찾음 : {}'.format(i))
        else:
            print('찾음 : {}'.format(result))