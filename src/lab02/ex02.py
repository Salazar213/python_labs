def transpose(mat1):
    rez_mat1 = []
    try:
        dlin_strok = set(list(map(len,mat1)))
        size_strok = len(mat1)
        size_stolb = int(list(map(len,mat1))[0]) 
    except:
        pass
    i = 0
    j = 0
    dict ={}
    if (len(dlin_strok) !=1 and mat1!=[]) or mat1 == [] or type(mat1) == str :
        return "ValueError"
    # else:
    #     for stroki in mat1:
    #         for elem in stroki:
    #             dict.update({(i,j):elem})
    #             j+=1
    #         i+=1
    #         j=0
    j = 0
    k = 0
    # for k in range(0,size_stolb):
    #     rez_mat1.append([])
    #     for j in range(0,size_strok):
    #         dobavl = dict.get((j,k))
    #         if (dobavl) != None:
    #             rez_mat1[k].append(dobavl)
    # return rez_mat1
    for k in range(0,size_stolb):
        rez_mat1.append([])
        for j in range(0,size_strok):
            dobavl = mat1[j][k]
            if dobavl != None:
                rez_mat1[k].append(dobavl)
    return rez_mat1



def row_sums(mat2):
    # rez_mat2 = []
    try:
        dlin_strok = set(list(map(len,mat2)))
        # size_strok = len(mat2)
        # size_stolb = int(list(map(len,mat2))[0]) 
    except:
        pass
    # i = 0
    # j = 0
    # dict ={}
    if (len(dlin_strok) !=1 and mat2!=[]) or mat2 == [] or type(mat2) == str :
        return "ValueError"
    else:
        return list(map(sum,mat2))
    

def col_sums(mat3):
    return row_sums(transpose(mat3))


print(transpose([[1, 2, 3], [4, 5, 6]]))