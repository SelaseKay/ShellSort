import math


def s_sort(nums: list):
    list_len = len(nums)
    interval = get_interval(list_len)
    while interval != 0:
        for idx in range(list_len):
            idx2 = idx + interval
            if idx2 > list_len - 1:
                break
            elif idx2 < list_len and nums[idx] > nums[idx2]:
                swap_pos(nums, idx, idx2)
                idx2 = idx - interval
                if idx2 >= 0 and nums[idx2] > nums[idx]:
                    swap_pos(nums, idx2, idx)
        interval = get_interval(interval)
    return nums


def get_interval(num):
    return math.floor(num / 2)


def swap_pos(num_list, idx, idx2):
    temp = num_list[idx]
    num_list[idx] = num_list[idx2]
    num_list[idx2] = temp
    return num_list


print(s_sort([4, 3, 2, 6, 10, 7, 9, 11, 8, 1]))
