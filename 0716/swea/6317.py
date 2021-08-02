def max(*args):
    max_value = -1000000
    for arg in args:
        if(max_value < arg):
            max_value = arg
    return max_value

print(f'max(3, 5, 4, 1, 8, 10, 2) => {max(3, 5, 4, 1, 8, 10, 2)}')