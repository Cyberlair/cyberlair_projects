import string
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

print("Welcome to the Text Analyzer!")
print("Enter your text in a single line, then press Enter to analyze. Type 'q' to quit.")

while True:
    text = input("Your text: ").strip()

    if text.lower() == 'q':
        print("Exiting program...")
        break

    if not text:
        print("Text cannot be empty! Please enter some text.")
        continue

    processed_text = ""
    for i in range(len(text)):
        processed_text += text[i]
        if text[i] in '.!?-:':
            if i < len(text) - 1 and text[i + 1] not in ' \n':
                processed_text += ' '

    sentences = sent_tokenize(processed_text)
    sentence_count = len(sentences)

    words = word_tokenize(processed_text)
    filtered_words = []
    for word in words:
        if any(char.isalpha() for char in word):
            filtered_words.append(word)

    word_count = len(filtered_words)

    char_count = sum(1 for char in text if char.isalpha())

    word_freq = {}
    for word in words:
        word = word.lower()
        word = ''.join(char for char in word if char not in string.punctuation)
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    repeated_words = {word: count for word, count in word_freq.items() if count > 1}
    if repeated_words:
        print("Words repeated more than once:")
        for word, count in sorted(repeated_words.items(), key=lambda x: (-x[1], x[0])):
            print(f"'{word}' (used {count} times)")

    if word_freq:
        max_count = max(word_freq.values())
        most_common_words = [word for word, count in word_freq.items() if count == max_count]
        print("Most frequent word(s):")
        for word in sorted(most_common_words):
            print(f"'{word}' (used {max_count} times)")
    else:
        print("Most frequent word: 'N/A' (used 0 times)")

    print(f"Number of words: {word_count}")
    print(f"Number of letters: {char_count}")
    print(f"Number of sentences: {sentence_count}")
    print("Enter another text to analyze, or type 'q' to quit.")