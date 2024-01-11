import java.util.*;
import java.util.Arrays;
public class MinSquaresSum {
    // Function to find the minimum number of squares that sum to n
    static int minSquares(int n) {
        // Create a table to store results of subproblems
        int[] ansarr = new int[n + 1];

        // Base case: 0 squares are needed for 0
        ansarr[0] = 0;

        // Initialize the table with maximum possible value
        for (int i = 1; i <= n; i++) {
            ansarr[i] = Integer.MAX_VALUE;
        }

        // Compute minimum squares required for all values from 1 to n
        for (int i = 1; i <= n; i++) {
            // Go through all smaller numbers
            for (int j = 1; j * j <= i; j++) {
                ansarr[i] = Math.min(ansarr[i], 1 + ansarr[i - j * j]);
            }
        }

        // The final result is stored in dp[n]
        return ansarr[n];
    }

    public static void main(String[] args) {
        int n1 = 100;
        System.out.println("Minimum number of squares for " + n1 + ": " + minSquares(n1));

        int n2 = 6;
        System.out.println("Minimum number of squares for " + n2 + ": " + minSquares(n2));
    }
}
