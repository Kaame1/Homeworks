# BINARY SEARCH

x = [1,3,5,9,10,13,14,25,27,34,45,67,123,164,200,230,245,400,699]
n = int(input('eneter number--'))
def binary_search(my_list,my_number):
    try: 
        mid = len(x)//2 
        mid_relative = len(x)//2 
        while True:
            if my_number == my_list[mid]:
                return mid
            if my_number > my_list[mid]:
                mid = mid + (mid_relative // 2)
                mid_relative = (mid_relative // 2) + 1
                continue
            if my_number < my_list[mid]:      
                mid = mid - (mid_relative // 2)
                mid_relative = (mid_relative // 2) + 1
                continue 
    except IndexError: 
        return print('yor number not in your lit')
print('n<index>==',binary_search(x,n))
