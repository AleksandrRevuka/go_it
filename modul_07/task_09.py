def all_sub_lists(lst):
    subs = [[]]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            subs.append(lst[i:j])
    return sorted(subs, key=len)


help(sorted)
print(all_sub_lists([4, 6, 1, 3]))
# повертає [[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]

