import time

def sort(Arr):
    startIndex = 0
    
    while startIndex < len(Arr):
        currentIndex = startIndex
        lowestIndex = currentIndex

        while currentIndex < len(Arr):
            if Arr[currentIndex] < Arr[lowestIndex]:
                lowestIndex = currentIndex
            currentIndex += 1
        
        Arr[startIndex], Arr[lowestIndex] = Arr[lowestIndex], Arr[startIndex]

        startIndex += 1
    return Arr

def sortWithRuntime(Arr):

    listComparisons = 0
    Switches = 0
    start = time.time_ns()

    startIndex = 0
    
    while startIndex < len(Arr):
        currentIndex = startIndex
        lowestIndex = currentIndex
        listComparisons += 1

        while currentIndex < len(Arr):
            listComparisons += 1
            if Arr[currentIndex] < Arr[lowestIndex]:
                lowestIndex = currentIndex
            currentIndex += 1
            listComparisons += 1
        
        Arr[startIndex], Arr[lowestIndex] = Arr[lowestIndex], Arr[startIndex]
        Switches += 1
        startIndex += 1
    end = time.time_ns()
    runtime = end - start
    print("done")
    print(f"needed {Switches} value switches and {listComparisons} comparisons in Array")
    print("runtime: " , runtime , " nanoseconds  or ", runtime / 1000000000, " seconds." )
    return Arr