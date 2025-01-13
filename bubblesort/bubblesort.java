

import java.util.Random;

public class bubblesort {
    public static int[] generateRandomArray(int[] array, int length){
        Random rand = new Random();
        for (int i = 0; i < length; i++) {
            array[i] = rand.nextInt(length*2);
        }
        return array;
    }

    public static int[] bubbleSort(int[] arr){
        int endIndex = arr.length;
        while(endIndex > 0){
            int currentIndex = 0;
            while(currentIndex < endIndex - 1){
                if(arr[currentIndex] > arr[currentIndex + 1]){
                    int temp = arr[currentIndex];
                    arr[currentIndex] = arr[currentIndex + 1];
                    arr[currentIndex + 1] = temp;
                }
                currentIndex++;
            }
            endIndex--;

        }
        return arr;  // Return the sorted array.  The original array remains unchanged.  This is a common idiom in Java.  The variable arr is passed by reference, so changes to arr within the method will affect the original array.  This is a good thing in this case, because we want to sort the original array.  If we wanted to sort a copy of the array, we would need to return a new array from the method.  But in this case, we
    }

    public static void main(String[] args){

        int length = 100;  // Change this value to change the array size. 100 is a good starting point. 1000000 might take a while to sort.
        int[] array = new int[length];
        array = generateRandomArray(array, 100);
        System.out.println("started with array:"+ java.util.Arrays.toString(array));
        array = bubbleSort(array);
        System.out.println("sorted array: "+ java.util.Arrays.toString(array));

    }
}
