import time

def sort(Arr):

    endIndex = len(Arr) - 1
    while endIndex > 0:
        currentIndex = 1

        while currentIndex < endIndex:
            if Arr[currentIndex] < Arr[currentIndex - 1]:
                Arr[currentIndex], Arr[currentIndex - 1] = Arr[currentIndex-1], Arr[currentIndex]

            currentIndex += 1
        endIndex -= 1
    return Arr

def sortWithRuntime(Arr):

    Comparisons = 0
    Switches = 0
    start = time.time_ns()

    endIndex = len(Arr) - 1
    while endIndex > 0:
        Comparisons += 1
        currentIndex = 1

        while currentIndex <= endIndex:
            Comparisons += 1
            if Arr[currentIndex] < Arr[currentIndex - 1]:

                Arr[currentIndex], Arr[currentIndex - 1] = Arr[currentIndex-1], Arr[currentIndex]
                Switches += 1
            currentIndex += 1
            Comparisons += 1
        endIndex -= 1

    end = time.time_ns()
    runtime = end - start
    print("done")
    print(f"needed {Switches} value switches and {Comparisons} comparisons")
    print("runtime: " , runtime , " nanoseconds  or ", runtime / 1000000000, " seconds." )
    return Arr