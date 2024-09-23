class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        n = len(s)
        # dp[i] will store the minimum number of extra characters if we consider up to index i-1 of s
        dp = [0] * (n + 1)

        # Precompute the lengths of words in the dictionary
        word_lengths = set(len(word) for word in dictionary)
        
        # Initialize dp array to be large, as we are looking for minimum
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1  # If no match, consider this character as extra

            # Only check substrings with lengths that exist in the dictionary
            for length in word_lengths:
                if i >= length and s[i - length:i] in dictionary:
                    dp[i] = min(dp[i], dp[i - length])

        return dp[n]


        
