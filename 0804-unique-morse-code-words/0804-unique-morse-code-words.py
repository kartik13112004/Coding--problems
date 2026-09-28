class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:

        # Morse code for letters a to z
        # Index 0 = a, index 1 = b, ..., index 25 = z
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.",
            "--.", "....", "..", ".---", "-.-", ".-..",
            "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        # All English letters in the same order as the Morse list
        letters = "abcdefghijklmnopqrstuvwxyz"

        # Create a dictionary:
        # a → .-
        # b → -...
        # c → -.-.
        # ...
        # z → --..
        mapping = dict(zip(letters, morse))

        # This list will store the complete Morse code
        # of each word
        result = []

        # Take one word at a time
        for word in words:

            # Start with an empty string for the current word
            morse_word = ""

            # Go through each character of the current word
            for i in range(len(word)):

                # Get the character using word[i]
                # Find its Morse code using mapping[word[i]]
                # Add that Morse code to morse_word
                morse_word = morse_word + mapping[word[i]]

            # After converting the complete word,
            # add its Morse code to the result list
            result.append(morse_word)

        # set(result) removes duplicate Morse codes
        # len() counts how many unique Morse codes are left
        return len(set(result))