import java.util.*;
import java.util.Arrays;

public class maxdifference {

	static int maxDifference(int[] nums) {
        if (nums == null || nums.length < 2) {
            // Not enough elements in the array
            System.out.println("Array should have at least two elements");
            return -1;
        }

        int minElement = nums[0];
        int maxDifference = nums[1] - nums[0];

        for (int i = 1; i < nums.length; i++) {
            int currentDifference = nums[i] - minElement;

            // Update maxDifference if a greater difference is found
            if (currentDifference > maxDifference) {
                maxDifference = currentDifference;
            }

            // Update minElement if a smaller element is found
            if (nums[i] < minElement) {
                minElement = nums[i];
            }
        }

        return maxDifference;
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 9, 5, 1, 3, 5};
        int result = maxDifference(nums);

        if (result != -1) {
            System.out.println("The maximum difference is " + result + ". The pair is (" + (nums[0] - result) + ", " + nums[0] + ")");
        }
    }
	
}
