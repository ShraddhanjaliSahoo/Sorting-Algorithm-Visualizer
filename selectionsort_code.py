import time

def selection_sort(data, drawrectangle, delay):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j

            drawrectangle(data, ["yellow" if x == j or x == min_index else "red" for x in range(n)])
            time.sleep(delay)

        data[i], data[min_index] = data[min_index], data[i]
        drawrectangle(data, ["green" if x == i else "red" for x in range(n)])
        time.sleep(delay)

    drawrectangle(data, ["blue" for _ in range(n)])
