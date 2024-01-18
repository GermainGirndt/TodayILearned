import os
import textwrap


def print_with_lines(input_filename, output_filename, width=80):
    print(input_filename)
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        lines = infile.readlines()

        for i, line in enumerate(lines, 1):
            wrapped_lines = textwrap.wrap(line, width=width)
            for wrapped_line in wrapped_lines:
                outfile.write(f"{i:>4}: {wrapped_line}\n")


def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        # Construct a corresponding output directory
        output_root = root.replace(input_dir, output_dir, 1)
        if not os.path.exists(output_root):
            os.makedirs(output_root)

        for file in files:
            input_filename = os.path.join(root, file)
            output_filename = os.path.join(output_root, file)
            print_with_lines(input_filename, output_filename)


# Set your input and output directories here
input_directory = 'input'
output_directory = 'output'
process_directory(input_directory, output_directory)
