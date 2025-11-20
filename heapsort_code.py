import time

def heap_sort(data, drawrectangle, delay):
    n = len(data)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawrectangle, delay)

    # Extract elements
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        drawrectangle(data, ["green" if x == i else "red" for x in range(n)])
        time.sleep(delay)
        heapify(data, i, 0, drawrectangle, delay)

    drawrectangle(data, ["blue" for _ in range(n)])

def heapify(data, n, i, drawrectangle, delay):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawrectangle(data, ["yellow" if x == i or x == largest else "red" for x in range(n)])
        time.sleep(delay)
        heapify(data, n, largest, drawrectangle, delay)
