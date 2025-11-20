import time

def quick_sort(data, drawrectangle, delay):
    quick_sort_recursive(data, 0, len(data) - 1, drawrectangle, delay)
    drawrectangle(data, ["blue" for _ in range(len(data))])

def quick_sort_recursive(data, low, high, drawrectangle, delay):
    if low < high:
        pivot_index = partition(data, low, high, drawrectangle, delay)
        quick_sort_recursive(data, low, pivot_index - 1, drawrectangle, delay)
        quick_sort_recursive(data, pivot_index + 1, high, drawrectangle, delay)

def partition(data, low, high, drawrectangle, delay):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        drawrectangle(data, ["yellow" if x == j or x == high else "red" for x in range(len(data))])
        time.sleep(delay)

        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            drawrectangle(data, ["green" if x == i or x == j else "red" for x in range(len(data))])
            time.sleep(delay)

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1
