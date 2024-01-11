import java.util.*;
import java.util.HashSet;

public class wordbreak {

	public static void main(String[] args) {
        Set<String> dictionary = new HashSet<String>(Arrays.asList("i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"));

        System.out.println(wordBreak("ilike", dictionary)); // Output: Yes
        System.out.println(wordBreak("ilikesamsung", dictionary)); // Output: Yes
    }

    public static boolean wordBreak(String s, Set<String> dictionary) {
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true; // Empty string can be segmented

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && dictionary.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
	
}
