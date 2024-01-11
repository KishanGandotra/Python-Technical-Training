import java.util.*;
import java.util.Arrays;

public class firstnonrepeating {

	static int findFirstNonRepeating(int[] arr) {
        // Create a HashMap to store the frequency of each element
        HashMap<Integer, Integer> frequencyMap = new HashMap<>();

        // Iterate through the array to populate the frequencyMap
        for (int num : arr) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Iterate through the array to find the first non-repeating element
        for (int num : arr) {
            if (frequencyMap.get(num) == 1) {
                return num;
            }
        }

        // If no non-repeating element is found, return a sentinel value (e.g., -1)
        return -1;
    }

    public static void main(String[] args) {
        int[] arr1 = {-1, 2, -1, 3, 0};
        int result1 = findFirstNonRepeating(arr1);
        System.out.println("Output for arr1: " + result1);

        int[] arr2 = {9, 4, 9, 6, 7, 4};
        int result2 = findFirstNonRepeating(arr2);
        System.out.println("Output for arr2: " + result2);
    }
	
}
