import time

# Merge Sort with Visualization
def merge_sort(data, drawrectangle, delay):
    merge_sort_recursive(data, 0, len(data) - 1, drawrectangle, delay)
    drawrectangle(data, ["blue" for _ in range(len(data))])


def merge_sort_recursive(data, left, right, drawrectangle, delay):
    if left < right:
        mid = (left + right) // 2

        merge_sort_recursive(data, left, mid, drawrectangle, delay)
        merge_sort_recursive(data, mid + 1, right, drawrectangle, delay)

        merge(data, left, mid, right, drawrectangle, delay)


def merge(data, left, mid, right, drawrectangle, delay):
    left_part = data[left:mid + 1]
    right_part = data[mid + 1:right + 1]

    i = j = 0
    k = left

    # Merging two sorted halves
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            data[k] = left_part[i]
            i += 1
        else:
            data[k] = right_part[j]
            j += 1
        
        drawrectangle(data, ["green" if x == k else "red" for x in range(len(data))])
        time.sleep(delay)
        k += 1

    # Copy remaining elements of left side
    while i < len(left_part):
        data[k] = left_part[i]
        i += 1
        drawrectangle(data, ["green" if x == k else "red" for x in range(len(data))])
        time.sleep(delay)
        k += 1

    # Copy remaining elements of right side
    while j < len(right_part):
        data[k] = right_part[j]
        j += 1
        drawrectangle(data, ["green" if x == k else "red" for x in range(len(data))])
        time.sleep(delay)
        k += 1
