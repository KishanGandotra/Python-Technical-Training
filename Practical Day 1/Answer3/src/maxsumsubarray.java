import java.util.*;
import java.util.Arrays;

public class maxsumsubarray {
	 static int maxSubarraySumCircular(int[] nums) {
	        int n = nums.length;

	        // Case 1: Maximum sum subarray without circular wrapping
	        int maxNormal = kadane(nums);

	        // Case 2: Maximum sum subarray with circular wrapping
	        int totalSum = 0;
	        for (int num : nums) {
	            totalSum += num;
	        }

	        // Invert the signs of the array elements and find the minimum sum subarray
	        int[] invertedNums = new int[n];
	        for (int i = 0; i < n; i++) {
	            invertedNums[i] = -nums[i];
	        }

	        int maxCircular = totalSum + kadane(invertedNums);

	        // Return the maximum of the two cases
	        return Math.max(maxNormal, maxCircular);
	    }

	    // Kadane's algorithm to find the maximum sum subarray
	    static int kadane(int[] nums) {
	        int maxSum = nums[0];
	        int currentSum = nums[0];

	        for (int i = 1; i < nums.length; i++) {
	            currentSum = Math.max(nums[i], currentSum + nums[i]);
	            maxSum = Math.max(maxSum, currentSum);
	        }

	        return maxSum;
	    }

	    public static void main(String[] args) {
	        int[] nums = {2, 1, -5, 4, -3, 1, -3, 4, -1};
	        int result = maxSubarraySumCircular(nums);
	        System.out.println("Subarray with the largest sum is " + Arrays.toString(getMaxSubarray(nums, result)) + " with sum " + result);
	    }

	    // Helper function to get the subarray with the maximum sum
	    static int[] getMaxSubarray(int[] nums, int maxSum) {
	        int currentSum = 0;
	        int startIndex = 0;
	        int endIndex = 0;
	        int tempStartIndex = 0;

	        for (int i = 0; i < nums.length; i++) {
	            currentSum += nums[i];

	            if (currentSum > maxSum) {
	                maxSum = currentSum;
	                startIndex = tempStartIndex;
	                endIndex = i;
	            }

	            if (currentSum < 0) {
	                currentSum = 0;
	                tempStartIndex = i + 1;
	            }
	        }

	        return Arrays.copyOfRange(nums, startIndex, endIndex + 1);
	    }
	
	
}

