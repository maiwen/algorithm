
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

#快速排序
# 首先，它每次都是选择第一个元素都为主元，这个回合就是要确定主元的位置；然后，有两个指针，一个leftmark指向主元的后面一个位置，
# 另一个rightmark指向要排序的数组最后一个元素；接着，两个指针分别向中间移动，leftmark遇到比主元大的元素停止，rightmark遇到比主元小的元素停止，
# 如果此时leftmark<rightmark，也就是说中间还有未处理(未确定与主元大小关系)的元素，那么就交换leftmark和rightmark位置上的元素，
# 然后重复刚才的移动操作，直到rightmark<leftmark；最后，停止移动时候rightmark就是主元要放置的位置，因为它停在一个比主元小的元素的位置上，
# 之后交换主元和rightmark指向的元素即可。完了之后，递归地对主元左右两边的数组进行排序即可。
#
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)
def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)
def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
    return right_mark


def quickSort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quickSort(array, low, right - 1)
    quickSort(array, right + 1, high)

# 堆排序
def fixDown(a, k, n):  # 自顶向下堆化，从k开始堆化
    N = n - 1
    while 2 * k <= N:
        j = 2 * k
        if j < N and a[j] < a[j + 1]:  # 选出左右孩子节点中更大的那个。此为大根堆，如果要构造小根堆（或者降序排序），改为 a[j] > a[j + 1]
            j += 1
        if a[k] < a[j]:                # 此为大根堆，如果要构造小根堆（或者降序排序），改为 a[k] > a[j]
            a[k], a[j] = a[j], a[k]
            k = j
        else:
            break

def heapSort(l):
    l.insert(0,-1)           # 占位
    n = len(l) - 1
    for i in range(n // 2, 0, -1):
        fixDown(l, i, len(l))
    while n > 1:
        l[1], l[n] = l[n], l[1]
        fixDown(l, 1, n)
        n -= 1
    l.pop(0)          # 移除占位
    return l


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 16]
quickSort(a_list, 0, len(a_list)-1)
print(a_list)
                
            