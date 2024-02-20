def process_file(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                print(line.strip())  # strip() removes leading and trailing whitespace, including the newline character
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_two_digit_number(input_string):
    first_digit = ""
    last_digit = ""
    for char in input_string:
        if char.isdigit():
            if first_digit == "":
                first_digit = char
            last_digit = char


def main():
    file_path = "input.txt"
    process_file(file_path)

if __name__ == "__main__":
    main()