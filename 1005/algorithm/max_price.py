def dfs(numbers, k):
    global max_number, sorted_numbers, numbers_set
    if k == 0:
        number = int(''.join(numbers))

        if number > max_number:
            max_number = number
        return
    
    if numbers == sorted_numbers:
        numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        dfs(numbers, k - 1)
        numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        return
    
    numbers_str = ''.join(numbers)
    if numbers_str in numbers_set:
        return

    numbers_set.add(numbers_str)
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            dfs(numbers, k - 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]
    
    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        numbers, k = input().split()
        numbers = list(numbers)
        k = int(k)

        sorted_numbers = sorted(numbers, reverse=True)
        numbers_set = set()

        max_number = 0

        dfs(numbers, k)

        print(f'#{t} {max_number}')
