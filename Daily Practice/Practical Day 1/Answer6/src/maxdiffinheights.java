import java.util.*;
import java.util.Arrays;

public class maxdiffinheights {

	static int minimizeMaxDifference(int[] arr, int k) {
        int n = arr.length;

        // Sort the array
        Arrays.sort(arr);

        // Initialize the result with the difference between the tallest and shortest tower
        int result = arr[n - 1] - arr[0];

        // Iterate through the array and consider each tower as the potential minimum
        for (int i = 0; i < n - 1; i++) {
            int currentMin = Math.min(arr[0] + k, arr[i + 1] - k);
            int currentMax = Math.max(arr[i] + k, arr[n - 1] - k);

            // Update the result if the new configuration gives a smaller difference
            result = Math.min(result, currentMax - currentMin);
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 15, 10};
        int k1 = 6;
        System.out.println("Output for arr1: " + minimizeMaxDifference(arr1, k1));

        int[] arr2 = {1, 5, 15, 10};
        int k2 = 3;
        System.out.println("Output for arr2: " + minimizeMaxDifference(arr2, k2));
    }
	
}
