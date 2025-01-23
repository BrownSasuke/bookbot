def count_words(text):
    # Splitting the text into words
    words = text.split()
    # Counting the number of words
    return len(words)

def count_characters(text):
    # Counting the number of characters
    char_count = {}

    # Iterating through the text
    for char in text:
        char = char.lower()  # Converting the character to lowercase
        
        # Only count alphabetic characters (no spaces, punctuation, or symbols)
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1  # Incrementing the count of the character
            else:
                char_count[char] = 1  # Initializing the count of the character

    return char_count

def generate_report(file_contents):
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    # Convert the character count dictionary into a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]

    # Sort the list of dictionaries by the 'num' key (frequency of characters)
    char_list.sort(reverse=True, key=lambda x: x["num"])

    # Print report header
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Print character frequencies (excluding spaces and punctuation)
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")

def main():
    # Pathing to the file
    path_to_file = "./books/frankenstein.txt"

    try:
        # Opening the file
        with open(path_to_file, "r") as f:
            file_contents = f.read()

        # Generate and print the report
        generate_report(file_contents)

    except FileNotFoundError as e:
        print(f"Error: {e}")

# Calling the function
if __name__ == "__main__":
    main()
