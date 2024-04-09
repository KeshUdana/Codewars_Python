def remove_first_and_last_chars(input_string):
    # Check if the string has at least two characters
    if len(input_string) >= 2:
        # Use string slicing to remove the first and last characters
        result_string = input_string[1:-1]
        return result_string
    else:
        # Return the original string if it has less than two characters
        return input_string

# Example usage:
original_string = "example"
modified_string = remove_first_and_last_chars(original_string)
print(modified_string)
