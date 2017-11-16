
def short_bubble_sort(a_list):
    sortlen = len(a_list) - 1
    exchange = True
    while sortlen > 0 and exchange:
        exchange = False
        for i in range(sortlen):
            if a_list[i] > a_list[i+1]:
                exchange = True
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        sortlen -= 1

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        a_list[fill_slot],a_list[pos_of_max]=a_list[pos_of_max],a_list[fill_slot]

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position-1] > current_value:
            a_list[position] = a_list[position-1]
            position = position - 1
        a_list[position] = current_value
        
def merge_sort(a_list):
    print('split.')
    if len(a_list)>1:
        mid = len(a_list)//2
        left = a_list[:mid]
        right = a_list[mid:]
        merge_sort(left)
        merge_sort(right)
        i= 0 
        j= 0
        k =0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a_list[k]=left[i]
                i += 1
                k += 1
            else:
                a_list[k]=right[j]
                j += 1
                k += 1
        while i < len(left):
            a_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a_list[k] = right[j]
            j += 1
            k += 1  
    print('merge')
    
    
    
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)
                
            