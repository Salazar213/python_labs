def min_max(nums1):
    if len(nums1) == 0 or [''] == nums1:
        return "ValueError"
    else:
        miimum = min(nums1)
        maximum = max(nums1)
        return (miimum,maximum)
    

def unique_sorted(nums2):
    a = list()
    if nums2 != ['']:
        nums2 = sorted(set(nums2))
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
    if fl!=1:
        return spis
    

def transpose(mat1):
    rez_mat1 = []
    size_stolb = 0
    size_strok = 0 
    try:
        size_strok = len(mat1)
        size_stolb = int(list(map(len,mat1))[0]) 
    except:
        return []
    i = 0
    j = 0
    rvanost = set(map(len,mat1))
    if (len(rvanost) !=1 and mat1!=[]) or type(mat1) == str :
        return "ValueError"
    j = 0
    k = 0
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
    if (len(dlin_strok) !=1 and mat2!=[]) or mat2 == [] or type(mat2) == str:
        return "ValueError"
    else:
        return list(map(sum,mat2))
    


def format_record(rec):
    # rec = list(rec)
    if len(rec) == 3:

        fio = rec[0]
        group = rec[1]
        gpa = rec[2]
    if len(rec)!=3 or group == '':
        return"ValueError"
    if type(fio) == str and type(group) == str and type(gpa) == float:
            try:
                name, surname, patronymic  = fio.split()
            except:
                 fio+=" None"
                 name, surname, patronymic  = fio.split()
            if patronymic == "None":
                 patronymic = ""
            else:
                 patronymic = patronymic[:-4]
            name = name.capitalize()
            surname = surname.capitalize()
            patronymic = patronymic.capitalize()
            if patronymic != '':
                initials = f"{name} {surname[0]}.{patronymic[0]}."
            else:
                 initials = f"{name} {surname[0]}."
    else:
        return "TypeError"
    ans = f"{initials}, гр. {group}, GPA {gpa:.2f}"
    return ans
