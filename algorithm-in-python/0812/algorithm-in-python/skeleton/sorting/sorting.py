import random
from time import  perf_counter

def get_insert_idx(res, elem, 
        cmp = lambda x, y: x if x > y else y, ):

    for i, e in enumerate(res):
        case = cmp(elem, e)
        if elem == cmp(elem, e): # elem > e:
            return i 
    
    return len(res)


def sort3_insert(lst, cmp = lambda x, y: x if x > y else y):
    res = []

    for elem in lst:
        new_idx = get_insert_idx(res, elem, cmp = cmp)
        res.insert(new_idx, elem)
    
    return res 


lst = []
for i in range(10000): 
    lst.append(random.randint(1,10000))


def merge(left, right, cmp):
    result_list = []

    while not left == [] and not right == []: 
        if cmp(left[0], right[0]) == left[0]: 
            result_list.append(left.pop(0))
        else: 
            result_list.append(right.pop(0))
    
    if left == []: 
        result_list += right
    else: 
        result_list += left 
    return result_list

def merge_sort(lst, cmp = lambda x, y: x if x > y else y):
    if len(lst) <= 1:
        return lst
    n = len(lst)//2
    left_lst = lst[:n]
    right_lst = lst[n:]
    left = merge_sort(left_lst,cmp=cmp)
    right = merge_sort(right_lst,cmp=cmp)

    return merge(left, right, cmp)

begin = perf_counter()
merge_sort(lst)
end = perf_counter() 
print("걸린 시간은 : ",end - begin )

begin = perf_counter()
sorted(lst)
end = perf_counter()
print("sorted에 걸린 시간은 : ", end-begin)

    
def partition(lst, low, high, cmp = lambda x, y: x if x > y else y):
    i = low - 1  # index of smaller element
    pivot = lst[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if cmp(lst[j], pivot) == pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]  # swap

    lst[i + 1], lst[high] = lst[high], lst[i + 1]  # swap
    return i + 1


def quick_sort(lst, cmp = lambda x, y: x if x > y else y):

    return quick_sort_util(lst, 0, len(lst)-1, cmp = lambda x, y: x if x > y else y)

def quick_sort_util(lst, low, high, cmp = lambda x, y: x if x > y else y):
    if low < high:
        partition_index = partition(lst, low, high, cmp = lambda x, y: x if x > y else y)

        # recursively sort elements before partition and after partition
        quick_sort_util(lst, low, partition_index - 1)
        quick_sort_util(lst, partition_index + 1, high)
        
    return lst 


def tim_sort(lst, cmp = lambda x, y: x if x > y else y):
    return lst 