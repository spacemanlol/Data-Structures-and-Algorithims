// Java program for implementation of Insertion Sort
class InsertionSort {
    void insertionsort(int arr[])
    {
        int n = arr.length;
        
        for(int i = 1; i < n - 1; i++){
            int key = arr[i];
            int j = i - 1;

            while(j >= 0 && key < arr[j]){
                arr[j + 1] = arr[j];
                j -= 1;
            }
            arr[j+1] = key;

        }

    }
  
    /* Prints the array */
    void printArray(int arr[])
    {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
  
    // Driver method to test above
    public static void main(String args[])
    {
        InsertionSort ob = new InsertionSort();
        int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
        ob.insertionsort(arr);
        System.out.println("Sorted array");
        ob.printArray(arr);
    }
}