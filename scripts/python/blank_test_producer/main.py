import os
import re
import random


def mask_words(sentence, percentage):
    words = re.findall(r'\w+', sentence)  # Extract words only for processing
    # Calculate number of words to mask
    num_to_mask = round(len(words) * (percentage / 100))
    if num_to_mask == 0:
        # Ensure at least one word is masked if there are words
        num_to_mask = 1 if len(words) > 0 else 0

    masked_indices = random.sample(range(len(words)), min(
        num_to_mask, len(words)))  # Random indices to mask, avoid error

    masked_sentence = []
    word_index = 0
    for part in re.split(r'(\w+)', sentence):  # Split sentence maintaining delimiters
        if part.isalpha() and word_index in masked_indices:  # Check if part is a word and should be masked
            mask_length = len(part) + random.randint(3,
                                                     6)  # Length of the mask
            masked_sentence.append('_' * mask_length)
            word_index += 1
        else:
            masked_sentence.append(part)
            if part.isalpha():
                word_index += 1

    return ''.join(masked_sentence)


def process_files(input_dir, output_dir, percentage):
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, 'r') as file:
                text = file.read()

            # Split into sentences at period or newline
            sentences = re.split(r'(?<=\.|\n)', text)
            modified_text = ''
            total_original_words = 0
            total_modified_words = 0

            for sentence in sentences:
                original_words = len(re.findall(r'\w+', sentence))
                masked_sentence = mask_words(sentence, percentage)
                modified_words = len(re.findall(r'\w+', masked_sentence))

                total_original_words += original_words
                total_modified_words += modified_words
                modified_text += masked_sentence + ' '

            with open(output_path, 'w') as file:
                file.write(modified_text.strip())

            print(f"Processed '{filename}': Original words = " +
                  f"{total_original_words}, Modified words = {total_modified_words}")


if __name__ == "__main__":
    percentage = float(
        input("Enter the percentage of words to mask out (%): "))
    input_dir = 'input'
    output_dir = 'output'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    process_files(input_dir, output_dir, percentage)
