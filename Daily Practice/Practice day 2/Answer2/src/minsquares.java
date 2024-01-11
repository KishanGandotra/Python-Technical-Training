import java.util.*;
import java.util.Arrays;

public class minsquares {
     
	public static int [] minSquares (n){
		 int[] dp = new int[n + 1];

	     // Initialize the array with maximum possible values
	     Arrays.fill(dp, Integer.MAX_VALUE);

	     // Base case: 0 requires 0 squares
	     dp[0] = 0;

	     // Fill the dp array bottom-up
	     for (int i = 1; i <= n; i++) {
	         // Try every square less than or equal to i
	         for (int j = 1; j * j <= i; j++) {
	             dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
	         }
	     }

	     return dp[n];
	 }
	
    public static void main(String[] args) {
        System.out.println(minSquares(100)); // Output: 1
        System.out.println(minSquares(6));   // Output: 3    
    }

}
