import os

def read_all_lines(input_dir):
    all_lines = []
    input_file_list=os.listdir(input_dir)
    for filename in input_file_list:
        file_path = os.path.join(input_dir, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)

    return all_lines