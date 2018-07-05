#coding=utf-8
def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
            return pos
        else:
            pos += 1
    return 'not found'
list = [1, 2, 32, 8, 17, 19, 42, 13,0,66,88]
# print(sequential_search(list,33))


def binary_search(a_list,item):
    low = 0
    high = len(a_list) - 1
    found = False
    while low <= high and not found:
        mid = (high+low) // 2
        if a_list[mid] == item:
            found = True
            return mid
        elif a_list[mid] < item:
            low = mid + 1
        elif a_list[mid] > item:
            high = mid - 1
    return 'not found'
# print(binary_search(list,88))

#除法取余法实现的哈希函数
def myHash(data,hashLength,):
    return data % hashLength
#哈希表检索数据
def searchHash(hash,hashLength,data):
    hashAddress=myHash(data,hashLength)
   #指定hashAddress存在，但并非关键值，则用开放寻址法解决
    while hash.get(hashAddress) and hash[hashAddress]!=data:
        hashAddress+=1
        hashAddress=hashAddress%hashLength
    if hash.get(hashAddress)==None:
        return None
    return hashAddress

#数据插入哈希表
def insertHash(hash,hashLength,data):
    hashAddress=myHash(data,hashLength)
    #如果key存在说明应经被别人占用， 需要解决冲突
    while(hash.get(hashAddress)):
        #用开放寻执法
        hashAddress+=1
        hashAddress=myHash(data,hashLength)
    hash[hashAddress]=data

if __name__ == '__main__':
    hashLength=20
    L=[13, 29, 27, 28, 26, 30, 38 ]
    hash={}
    for i in L:
        insertHash(hash,hashLength,i)
    result=searchHash(hash,hashLength,30)
    if result:
        print("数据已找到，索引位置在",result)
        print(hash[result])
    else:
        print("没有找到数据")


