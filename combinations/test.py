# solution 1: recursive (divide and conquer)
def combinations(indices):

    if len(indices) == 1:
        yield indices

    for i, ele in enumerate(indices):
        for comb in combinations(indices[:i] + indices[i+1:]):
            yield ([ele] + comb)

for comb in combinations([0,1,2,3]):
    print(comb)

# solution 2: iterative appraoch (possibly in-place?)
def combinations_iter(indices):

    i = len(indices) - 1

    while True:
        has_result = False
        for i in range(len(indices)-1, 0, -1):
            is_break = False
            for j in range(i-1, -1, -1):
                if indices[i] > indices[j]:
                    indices[i], indices[j] = indices[j], indices[i]
                else:
                    continue

                if len(indices[j+1:]) > 1:
                    indices[j+1:] = sorted(indices[j+1:])

                yield indices
                is_break = True
                has_result = True
                break

            if is_break:
                break
        if not has_result:
            break

arr = ["a","b","c","d"]
print(arr)
for comb in combinations_iter(list(range(len(arr)))):
    print([arr[i] for i in comb])
