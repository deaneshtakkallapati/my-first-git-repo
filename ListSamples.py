# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:18:30 2024

@author: DEANESH
"""

def remove_element(nums, remove_element):
    new_list = []
    count = 0
    for i in range(len(nums)):
        if remove_element != nums[i]:
            new_list.append(nums[i])
        else:
            count = count + 1
    return count, new_list
            
def remove_duplicates(my_list):
    a = set()
    for i in my_list:
        a.add(i)
    return sorted(a)

def keep_max_occur_elements_mentioned(my_list, occurence_count):
    element_dict = {}; updated_list = []
    for i in my_list:
        if i in element_dict:
            if element_dict[i] < occurence_count:
                element_dict[i] = element_dict[i] + 1; updated_list.append(i)
        else:
            element_dict[i] =  1
            updated_list.append(i)
    return updated_list

def max_occur_element(my_list):
    element_dict = {}
    max_value = 0
    max_element = None
    for i in my_list:
        if i in element_dict:
            element_dict[i] = element_dict[i] + 1
            if max_value < element_dict[i]:
                max_value = element_dict[i]; max_element = i
        else:
            element_dict[i] =  1
            if max_value < 1:
                max_element = i; max_value = 1
                

    return max_element, max_value

def rotate_array_from_index_no(nums, index_no):
    updated_list = []
    pre_index_list = nums[0:index_no+1]
    post_index_list = nums[index_no+1:len(nums)]
    updated_list = post_index_list
    for element in pre_index_list:
        updated_list.append(element)
    print(updated_list)
    return updated_list
    
def merge_lists(my_list_1, my_list_2):
    return []

nums = ['a', 'b', 'c', 'd', 'b','e', 'b','c','c','a','e','x','x','a','a','a']
remove_val = 'b'

# remove_element
count, updated_list = remove_element(nums, remove_val)

# remove_duplicates
res = remove_duplicates(nums)

# keep_max_occur_elements_mentioned
res = keep_max_occur_elements_mentioned(nums, 2)

# max_occur_element
max_element, max_value  = max_occur_element(nums)

nums = [1,2,3,4,5]; index_no = 2
res = rotate_array_from_index_no(nums, index_no)

head = [1,2,3,3,4,4,5]
a = list(set(my_list))

head = [1,4,3,2,5,2]; x = 3
updated_list = []
for i in head:
    if i < x:
        updated_list.append(i)
for i in head:
    if i >=x:
        updated_list.append(i)

print(updated_list)




