import java.util.Random;

// This class implements selection sort.

public class selectionsort {
    //from stackoverflow
    public static int[] generateRandomArray(int[] array, int length){
        Random rand = new Random();
        for (int i = 0; i < length; i++) {
            array[i] = rand.nextInt(length*2);
        }
        return array;
    }

    public static int[] selectionSort(int[] arr) {
        int startIndex = 0;
        while (startIndex < arr.length) {
            int currentIndex = startIndex;
            int bestValue= arr[startIndex];
            while (currentIndex < arr.length) {
                if (arr[currentIndex] < bestValue){
                    bestValue = arr[currentIndex];
                    int temp = arr[startIndex];
                    arr[startIndex] = bestValue;
                    arr[currentIndex] = temp;
                }
                currentIndex++;
            }

            startIndex++;
        }
        return arr;  // Return the sorted array.  The original array remains unchanged.  This is a common idiom in Java.  The variable arr is passed by reference, so changes to arr within the method will affect the original array.  This is a good thing in this case, because we want to sort the original array.  If we wanted to sort a copy of the array, we would need to return a new array from the method.  But in this case, we
    }
    public static void main(String[] args) {

        int length = 100;  // Change this value to change the array size. 100 is a good starting point. 1000000 might take a while to sort.
        int[] array = new int[length];
        array = generateRandomArray(array , 100);
        System.out.println("Original Array: " + java.util.Arrays.toString(array));
        array= selectionSort(array);
        System.out.println("Sorted Array: " + java.util.Arrays.toString(array));


    }
    
}
