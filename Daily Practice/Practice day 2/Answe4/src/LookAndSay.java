import java.util.*;
import java.util.Arrays;
public class LookAndSay {
    // Function to generate the next term in the Look-and-Say sequence
    static String nextTerm(String str) {
        StringBuilder result = new StringBuilder();

        // Traverse the given sequence
        for (int i = 0; i < str.length(); i++) {
            int count = 1; // Initialize count for current character

            // Count occurrences of the current character
            while (i + 1 < str.length() && str.charAt(i) == str.charAt(i + 1)) {
                i++;
                count++;
            }

            // Append count and current character to result
            result.append(count).append(str.charAt(i));
        }

        // Return the generated term
        return result.toString();
    }

    // Function to find the n'th term in the Look-and-Say sequence
    static String nthTerm(int n) {
        if (n == 1) {
            return "1";
        }

        String result = "1";

        // Generate the n'th term by iteratively calling nextTerm
        for (int i = 2; i <= n; i++) {
            result = nextTerm(result);
        }

        return result;
    }

    public static void main(String[] args) {
        int n1 = 3;
        System.out.println("The " + n1 + "'th term is: " + nthTerm(n1));

        int n2 = 5;
        System.out.println("The " + n2 + "'th term is: " + nthTerm(n2));
    }
}