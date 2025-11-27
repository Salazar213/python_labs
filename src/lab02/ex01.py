def min_max(nums1):
    if len(nums1) == 0 or [""] == nums1:
        return "ValueError"
    else:
        miimum = min(nums1)
        maximum = max(nums1)
        return (miimum, maximum)


def unique_sorted(nums2):
    # nums2 = list(input().split(','))
    # nums2 = list(map(beauty, spis))
    a = list()
    if nums2 != [""]:
        nums2 = list(set(list(nums2)))
        return nums2
    else:
        return a


def flatten(nums3):
    fl = 0
    spis = list()
    for item in nums3:
        if type(item) == tuple or type(item) == list:

            spis.extend(item)
        elif type(item) == str:
            fl = 1
            return "TypeError"
        else:
            spis.append(item)
    if fl != 1:
        return spis


def beauty(x):
    if "." in x:
        return float(x)
    elif "" == x:
        return x
    else:
        return int(x)


# print(f"{flatten([[1, 2], "ab"])}")


# spis = list(input().split(','))
# spis = list(map(beauty, spis))
# print([3, -1, 5, 5, 0])
# print(min_max([3, -1, 5, 5, 0]))
# print([42])
# print(min_max([42]))
# print([-5, -2, -9])
# print(min_max([-5, -2, -9]))
# print([])
# print(min_max([]))
# print([1.5, 2, 2.0, -3.1])
# print(min_max([1.5, 2, 2.0, -3.1]))
# print([3, 1, 2, 1, 3])
# print(unique_sorted([3, 1, 2, 1, 3]))
# print([])
# print(unique_sorted([]))
# print([-1, -1, 0, 2, 2])
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print([1.0, 1, 2.5, 2.5, 0])
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
# print([[1, 2], [3, 4]])
# print(flatten([[1, 2], [3, 4]]))
# print(([1, 2], (3, 4, 5)))
# print(flatten(([1, 2], (3, 4, 5))))
# print([[1], [], [2, 3]])
# print(flatten([[1], [], [2, 3]]))
# print([[1, 2], "ab"])
# print(flatten([[1, 2], "ab"]))
