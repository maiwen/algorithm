# -*- coding: utf-8 -*-
"""
Created on 2018/9/5 14:07

@author: vincent
"""
class Sort:
    def __init__(self):
        self.data = [12,15,85,52,65,20,89,58,256,33,85]

    def select_sort(self, nums):
        n = len(nums)
        while n > 0:
            max_index = 0
            for i in range(n):
                if nums[i] > nums[max_index]:
                    max_index = i
            nums[n-1], nums[max_index] = nums[max_index], nums[n-1]
            n -= 1
        return nums

    def bubble_sort(self, nums):
        n = len(nums)
        exchange = True
        while n > 0 and exchange:
            exchange = False
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    exchange = True
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            n -= 1
        return nums

    def insert_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return nums

    def shell_sort(self, nums):
        n = len(nums)
        h = 1
        while h < n / 3:
            h = h * 3 + 1
        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h and nums[j] < nums[j - h]:
                    nums[j], nums[j - h] = nums[j - h], nums[j]
                    j -= h
            h //= 3
        return nums

    def merge_sort(self, nums):
        print('split')
        if len(nums) > 1:
            n = len(nums)
            mid = n // 2
            left, right = nums[:mid], nums[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            i, j , k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = right[j]
                    j += 1
                    k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        print('merge')
        return nums

    def quickSort(a, l, r):

        if l >= r:
            return a

        x = a[l]
        i = l
        j = r

        while i <= j:
            while a[i] < x:
                i += 1
            while a[j] > x:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        quickSort(a, l, j)
        quickSort(a, i, r)

        return a

    def quick_sort(self, nums):
        self.quick_sort_helper(nums, 0, len(nums)-1)
        return nums

    def quick_sort_helper(self, nums, start, end):
        if start < end:
            split_index = self.split(nums, start, end)
            self.quick_sort_helper(nums, start, split_index)
            self.quick_sort_helper(nums, split_index+1, end)

    def split(self, nums, start, end):
        value = nums[start]
        left = start + 1
        right = end
        done = False
        while not done:
            while left <= right and nums[left] <= value:
                left += 1
            while left <= right and nums[right] >= value:
                right -= 1
            if left > right:
                done = True
            else:
                nums[left], nums[right] = nums[right], nums[left]
        nums[start], nums[right] = nums[right], nums[start]
        return right


    def heap_sort(self, nums):
        nums.insert(0,-1)
        n = len(nums)-1
        for i in range(n//2, 0, -1):
            self.sink(nums, i, n)
        while n > 1:
            nums[1], nums[n] = nums[n], nums[1]
            self.sink(nums, 1, n)
            n -= 1
        nums.pop(0)
        return nums

    def sink(self, nums, k, n):
        n -= 1
        while 2*k < n:
            j = 2*k
            if nums[j] < nums[j+1]:
                j += 1
            if nums[k] < nums[j]:
                nums[k], nums[j] = nums[j], nums[k]
                k = j
            else:
                break

if __name__ == '__main__':
    sort = Sort()
    print(sort.heap_sort(sort.data))