import sys
from ._internals.preprocess_lines import preprocess_lines
from ._internals.count_words import count_words
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_dir> <output_dir>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    all_lines = read_all_lines(input_dir)

    all_lines = preprocess_lines(all_lines)

    words = split_into_words(all_lines)

    counter = count_words(words)

    write_word_counts(counter, output_dir)

if __name__ == "__main__":
    main()