import bubblesort.bubblesort
import selectionsort
import bubblesort
import random

import selectionsort.selectionsort

Algo = input("""-----Select sorting algorithm------
      enter S for Selection Sort
      enter B for Bubble Sort
      """)

Arraylength = int(input("""-----Enter array length for the sorting algorithm-----
                        """))
Array = [random.randint(0, round(Arraylength * 2)) for i in range(Arraylength)]



getRuntime = input("""Kowalski Analyse?
      enter 1 for True
      and 0 for False
      """)

extensiveLogging = input("""Do you want extensive logging enabled?
      enter 1 for True
      and 0 for False
      """)

if extensiveLogging == "1":
    print("starting with array: " , Array)

print("starting the sorting...")

if Algo == "S" or Algo == "s":
    if getRuntime == "1":
        Array = selectionsort.selectionsort.sortWithRuntime(Array)
    else:
        Array = selectionsort.selectionsort.sort(Array)

elif Algo == "B" or Algo == "b":
    if getRuntime == "1":
        Array = bubblesort.bubblesort.sortWithRuntime(Array)
    else:
        Array = bubblesort.bubblesort.sort(Array)
if extensiveLogging == "1":
    print("finished with Array: " , Array)
