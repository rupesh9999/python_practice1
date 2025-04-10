from collections import Counter

class TextAnalyzer:
    """A class to analyze word frequencies in a text file."""

    def __init__(self, filename):
        """Initialize with a filename."""
        self.filename = filename
        self.words = []

    def read_file(self):
        """Read the file and store words in a list."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.words = file.read().lower().split()
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")
            self.words = []

    def count_words(self):
        """Count the frequency of each word in the list."""
        return len(self.words)
    
    def get_most_common(self, n=10):
        """Get the n most common words."""
        if not self.words:
            self.read_file()
        if not self.words:
            return []        
        word_counts = Counter(self.words)
        return word_counts.most_common(n)
