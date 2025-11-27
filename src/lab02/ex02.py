def transpose(mat1):
    rez_mat1 = []
    size_stolb = 0
    size_strok = 0
    try:
        size_strok = len(mat1)
        size_stolb = int(list(map(len, mat1))[0])
    except:
        return []
    i = 0
    j = 0
    rvanost = set(map(len, mat1))
    if (len(rvanost) != 1 and mat1 != []) or type(mat1) == str:
        return "ValueError"
    j = 0
    k = 0
    for k in range(0, size_stolb):
        rez_mat1.append([])
        for j in range(0, size_strok):
            dobavl = mat1[j][k]
            if dobavl != None:
                rez_mat1[k].append(dobavl)
    return rez_mat1


def row_sums(mat2):
    # rez_mat2 = []
    try:
        dlin_strok = set(list(map(len, mat2)))
        # size_strok = len(mat2)
        # size_stolb = int(list(map(len,mat2))[0])
    except:
        pass
    # i = 0
    # j = 0
    # dict ={}
    if (len(dlin_strok) != 1 and mat2 != []) or mat2 == [] or type(mat2) == str:
        return "ValueError"
    else:
        return list(map(sum, mat2))


def col_sums(mat3):
    return row_sums(transpose(mat3))


a = [[1, 2, 3], [4, 5, 6]]
b = [[-1, 1], [10, -10]]
c = [[0, 0], [0, 0]]
d = [[1, 2], [3]]
print(a, col_sums(a), b, col_sums(b), c, col_sums(c), d, col_sums(d), sep="\n")
