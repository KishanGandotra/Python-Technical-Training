import java.util.*;
import java.util.Arrays;

public class productofelements {

	 static int[] getProductArray(int[] nums) {
	        int n = nums.length;

	        // Arrays to store product values to the left and right of each element
	        int[] leftProducts = new int[n];
	        int[] rightProducts = new int[n];

	        // Initialize the product arrays
	        leftProducts[0] = 1;
	        rightProducts[n - 1] = 1;

	        // Calculate products to the left of each element
	        for (int i = 1; i < n; i++) {
	            leftProducts[i] = leftProducts[i - 1] * nums[i - 1];
	        }

	        // Calculate products to the right of each element
	        for (int i = n - 2; i >= 0; i--) {
	            rightProducts[i] = rightProducts[i + 1] * nums[i + 1];
	        }

	        // Calculate the final product array
	        int[] result = new int[n];
	        for (int i = 0; i < n; i++) {
	            result[i] = leftProducts[i] * rightProducts[i];
	        }

	        return result;
	    }

	    public static void main(String[] args) {
	        int[] nums1 = {1, 2, 3, 4, 5};
	        int[] result1 = getProductArray(nums1);
	        System.out.println(Arrays.toString(result1));

	        int[] nums2 = {5, 3, 4, 2, 6, 8};
	        int[] result2 = getProductArray(nums2);
	        System.out.println(Arrays.toString(result2));
	    }
	
}
