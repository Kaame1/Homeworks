# BINARY SEARCH

def binary_search(my_list,my_number):
    min_list = 0
    max_list = len(my_list) - 1
    while min_list <= max_list:
        mid = (min_list + max_list) // 2
        if my_list[mid] == my_number:
            return mid
        elif my_list[mid] < my_number:
            min_list = mid + 1
        else:
            max_list = mid - 1
    return 'your number not in your list'        
x = [1,3,5,9,10,13,14,25,27,34,45,67,123,164,200,230,245,400,699]
n = int(input('eneter number--'))
print('n<index>==',binary_search(x,n))
