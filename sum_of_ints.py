def two_numbers_steve(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def main(): 
    nums = [2, 7, 11, 15]
    target = 9
    print(two_numbers_steve(nums, target))

main()