'''

Given 3 Inputs count, per_page, page_number

print 4 previous page number, current_page,  4 next page numbers

example: count = 100, per_page = 20, page_number = 3

output: 1 2 3 4 5
'''

def get_page_details(count, per_page, page_number):
    total_pages = count//per_page + (1 if count%per_page else 0)
    page_nos = list(range(1,total_pages+1))
    index = page_nos.index(page_number)
    return get_previous_page_nos(page_nos, index) + get_next_page_nos(page_nos, index)

def get_previous_page_nos(page_nos, index):
    return page_nos[:index] if index < 4 else page_nos[index-4:index]

def get_next_page_nos(page_nos, index):
    return page_nos[index:index+5]
'''
Find the maximum sum of the sub array
example: arr = [1, 2, 3, -2, 5]
output: 9
'''

# print(get_page_details(100, 5, 19))
# arr = [1, 2, 3, -2, 5]

arr = [-1,-1,-2,-3,-4]

max_val = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)+1):
        if not max_val:
            max_val = (arr[i] + arr[j])
        else:
            val = arr[i] + sum(arr[i+1:j])
            if val > max_val:
                max_val = val

print(max_val)




# print(sum(arr))