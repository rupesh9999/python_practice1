from text_analyzer import TextAnalyzer

# Create an instance of TextAnalyzer with a sample text file
analyzer = TextAnalyzer('sample.txt')

# Read the file and analyze it
analyzer.read_file()

# Display results
total_words = analyzer.get_word_count()
common_words = analyzer.get_most_common(3)

print(f"Total words in the file: {total_words}")
print("Top 3 most common words:")
for word, count in common_words:
    print(f"'{word}': {count} times")