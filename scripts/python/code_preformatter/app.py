import textwrap


def print_with_lines(input_filename, output_filename, width=80):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        lines = infile.readlines()

        for i, line in enumerate(lines, 1):
            wrapped_lines = textwrap.wrap(line, width=width)
            for wrapped_line in wrapped_lines:
                outfile.write(f"{i:>4}: {wrapped_line}\n")


input_filename = 'input/yourfile.s'  # Replace with your input file name
output_filename = 'output/yourfile_edited.s'  # Output file
print_with_lines(input_filename, output_filename)
