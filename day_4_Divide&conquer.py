# def merge_sort(arr, si, ei):
#     # Base case: single element
#     if si >= ei:
#         return

#     # Find middle
#     mid = (si + ei) // 2

#     # Recursively sort both halves
#     merge_sort(arr, si, mid)
#     merge_sort(arr, mid + 1, ei)

#     # Merge the sorted halves
#     merge(arr, si, mid, ei)


# def merge(arr, si, mid, ei):
#     temp = []
#     i = si
#     j = mid + 1

#     # Merge two sorted parts
#     while i <= mid and j <= ei:
#         if arr[i] <= arr[j]:
#             temp.append(arr[i])
#             i += 1
#         else:
#             temp.append(arr[j])
#             j += 1

#     # Remaining elements from left half
#     while i <= mid:
#         temp.append(arr[i])
#         i += 1

#     # Remaining elements from right half
#     while j <= ei:
#         temp.append(arr[j])
#         j += 1

#     # Copy back to original array
#     for k in range(len(temp)):
#         arr[si + k] = temp[k]


# # Example
# arr = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(arr, 0, len(arr) - 1)
# print(arr)


def quick_sort(arr, si, ei):
    # Base case
    if si >= ei:
        return

    # Partition the array
    p_index = partition(arr, si, ei)

    # Recursively sort left and right parts
    quick_sort(arr, si, p_index - 1)
    quick_sort(arr, p_index + 1, ei)


def partition(arr, si, ei):
    pivot = arr[ei]   # choosing last element as pivot
    i = si - 1

    for j in range(si, ei):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[ei] = arr[ei], arr[i + 1]
    return i + 1


# Example usage
arr = [6, 3, 9, 5, 2, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
