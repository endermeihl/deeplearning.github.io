def binary_search(list,item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid+1
        if guess > item:
            high = mid - 1
        else:
            low =  mid + 1
    return None

my_list=[1,3,5,7,9]
print(binary_search(my_list,5))


def binary_search_stack(list,item):
    low=0
    high = len(list) - 1
    mid = int((low + high)/2)
    guess = list[mid]
    if guess == item:
        return mid+1
    if guess > item:
        return binary_search_stack(list(low,mid-1),item)
    else:
        return binary_search_stack(list(mid+1,high),item)

print(binary_search_stack(my_list,5))