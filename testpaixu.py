def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):  # 外层循环控制比较轮数
        for j in range(n-i-1):  # 内层循环控制每轮的比较次数
            if arr[j] > arr[j+1]:
                # 交换两个元素的位置
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

# 示例使用
arr = [12, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("排序后的数组：", sorted_arr)


def paixu(numarray):
    leng = len(numarray)
    
    for i in range(leng-1):
        for j in range(leng-i-1):
            if numarray[j] > numarray[j+1]:
                numarray[j], numarray[j+1] = numarray[j+1], numarray[j]
    return numarray

num = [51, 72, 23, 95, 73, 24, 92]

numarray1 = paixu(num[:])
print( numarray1)
