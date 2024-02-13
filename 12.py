def capitalize_words_in_file(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Capitalize the first letter of every word
        capitalized_content = ' '.join(word.capitalize() for word in content.split())

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(capitalized_content)

        print("Capitalization completed. Modified content saved to", output_file)

    except FileNotFoundError:
        print("Input file not found.")
    except IOError:
        print("An error occurred while processing the file.")

