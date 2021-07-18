def solution(nums):
    data_set = set(nums)
    select = int(len(nums) / 2)
    if(len(data_set) < select):
        return len(data_set)
    else: return select

nums = [3,1,2,3]
print(solution(nums))