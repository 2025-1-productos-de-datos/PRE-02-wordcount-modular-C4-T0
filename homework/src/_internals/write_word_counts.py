import os

def write_word_counts(counter, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
            for key, value in counter.items():
                f.write(f"{key}\t{value}\n")