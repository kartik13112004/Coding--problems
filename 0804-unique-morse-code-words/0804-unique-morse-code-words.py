class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:

        # Morse code for a to z
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.",
            "--.", "....", "..", ".---", "-.-", ".-..",
            "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        # English letters in the same order
        letters = "abcdefghijklmnopqrstuvwxyz"

        # Create letter → Morse mapping
        mapping = dict(zip(letters, morse))

        # Store Morse representation of each word
        result = []

        # Process each word
        for word in words:

            # Start empty Morse string
            morse_word = ""

            # Process each character
            for i in range(len(word)):

                # Get Morse code and add it
                morse_word = morse_word + mapping[word[i]]

            # Store complete Morse representation
            result.append(morse_word)

        # Remove duplicates and return the number of unique representations
        return len(set(result))