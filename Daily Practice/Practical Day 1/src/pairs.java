import java.util.Arrays;
import java.util.HashMap;
import java.util.*;

public class pairs {

	static void findPair(int[] nums, int target) {
        // Create a HashMap to store elements and their differences from the target
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            int difference = target - num;

            // Check if the difference exists in the map
            if (map.containsKey(difference)) {
                System.out.println("Pair found (" + difference + ", " + num + ")");
                return; // You can also store the pair in a data structure or perform any other necessary action
            }

            // If difference is not found, add the current element and its difference to the map
            map.put(num, difference);
        }

        // If no pair is found
        System.out.println("Pair not found");
    }

    public static void main(String[] args) {
        int[] nums = {8, 7, 2, 5, 3, 1};
        int target = 10;

        findPair(nums, target);
    }
}
