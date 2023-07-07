#проверить является ли изограмой
def is_isogram(isg:str):
    isg = isg.lower()
    word = []
    for i in isg:
        if i in word:
            return False
        else:
            word.append(i)
    return True