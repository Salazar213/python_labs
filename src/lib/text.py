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



def normalize (text1: str, casefold: bool = True , yo2e:bool = True)-> str:
    if type(text1) != str:
        raise TypeError("Неверный тип данныхх")
    if yo2e:
        text1 = text1.replace('ё','е')
        text1 = text1.replace("Ё","Е")
    
    if casefold:
        text1 = text1.casefold()

    text1 = ' '.join(text1.split())
    text1 = ' '.join(text1.split('\t'))
    text1 = ' '.join(text1.split('\r'))
    text1 = ' '.join(text1.split('\n'))

    return text1
def tokenize(text2: str) -> list[str]:
    
    alph1 = ',./~!@#$%^&*()<>}{=+!"№;%:?*()—'
    alph2 = "'"
    alph3 = '_-'
    alph_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'
    for i in alph1:
        text2 = text2.replace(i, ' ')
    for j in alph2:
        text2 = text2.replace(j, ' ')
    text2 = [_ for _ in text2]
    for i in range(len(text2)):
        try:
            if (text2[i] in alph3) and (text2[i-1] in alph_letters and text2[i+1] in alph_letters):
                pass
            else:
                if text2[i] in alph3:
                    text2[i] = ' '
        except:
            if text2[i] in alph3:
                text2[i] = ' '
    text2 = ''.join(text2)
    text2 = text2.split()
    i = 0
    for element in text2:
        
        for letter in element:
            if not(letter in alph_letters) and letter not in alph3:
                element = element.replace(letter,'')
                text2[i] = element
        i+=1
    text2 = [i for i in text2 if i!=""]
    return text2


def count_freq(tokens: list[str]) -> dict[str, int]:
    ans = dict()
    if type(tokens) != list:
        raise TypeError(f"Не верный тип данных должно быть list, передано {type(tokens)}")
    try:

        if type(tokens[0])!=str:
            raise TypeError(f'"Не верный тип данных должно быть list[str], передано list[{type(tokens[0])}]"')
    except:
        pass

    try:
        type_tokens = set(list(map(type, tokens)))
        if len(set)!=1:
            raise TypeError(f"Внутри списка строки разных типов данных {type_tokens}")
    except:
        pass
    for element in tokens:
        if element not in ans:
            ans.update({element : tokens.count(element)})
    return ans


def top_n(freq: dict[str, int], n: int = 5)-> list[tuple[str, int]]:
    if  type(freq) != dict:
        raise TypeError(f'Не верный тип данных должно быть dict, передано {type(freq)}')
    if  type(n) != int:
        raise TypeError(f'Не верный тип данных должно быть int, передано {type(n)}')
    freq = sorted(freq.items(),key=lambda x: (-x[1],x[0]))
    if n >len(freq):
        return freq
    else:
        return freq[:n]


def count_freq_top(tokens: list[str]) -> dict[str, int]:
    tokens = list(input().split())
    ans = dict()
    for element in tokens:
        if element not in ans:
            ans.update({element : tokens.count(element)})
    return(f"Всего слов: {len(tokens)}")