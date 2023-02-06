def bst(arr, tar) -> int:
    if arr is None:
        return -1
    mid = int(len(arr) / 2)
    if arr[mid] == tar:
        return mid
    if tar > arr[mid]:
        return bst(arr[mid+1:], tar)
    else:
        return bst(arr[:mid], tar)