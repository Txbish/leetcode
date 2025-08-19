class Solution:
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)  # convert to list for mutability
        i, j = 0, len(s) - 1

        while i < j:
            # Move left pointer until it finds a vowel
            while i < j and s[i] not in vowels:
                i += 1
            # Move right pointer until it finds a vowel
            while i < j and s[j] not in vowels:
                j -= 1

            # Swap vowels
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
