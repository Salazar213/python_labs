import string
def normilize (text1: str, casefold: bool = True , yo2e:bool = True)-> str:
    if yo2e:
        text1 = text1.replace('ё','е')
        text1 = text1.replace("Ё","Е")
    
    if casefold == True:
        text1 = text1.casefold()
    text1 = ' '.join(text1.split())
    text1 = ' '.join(text1.split('\t'))
    text1 = ' '.join(text1.split('\r'))
    text1 = ' '.join(text1.split('\n'))

    return text1
def tokenize(text2: str) -> list[str]:
    
    alph1 = ',./~!@#$%^&*()+!"№;%:?*()—'
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
    print (text2)
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
    for element in tokens:
        if element not in ans:
            ans.update({element : tokens.count(element)})
    return ans


def top_n(freq: dict[str, int], n: int = 5)-> list[tuple[str, int]]:
    
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
    

print(top_n({"aa":2,"bb":2,"cc":1},3))