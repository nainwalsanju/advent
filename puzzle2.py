def process_file(file_path):
  try:
    sum = 0
    with open(file_path, "r") as file:
      for line in file:
        # print(line.strip())
        sum += int(create_two_digit_number(replace_with_numbers(line.strip())))
        # print(sum)
    print(sum)
  except FileNotFoundError:
    print(f"File '{file_path}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")


def create_two_digit_number(input_string) -> str:
    first_digit = ""
    last_digit = ""
    for char in input_string:
        if char.isdigit():
            if first_digit == "":
                first_digit = char
            last_digit = char
    print(first_digit+last_digit)
    return first_digit + last_digit


def replace_with_numbers(input_string):
    replacements = {
      'zero': 'z0o',
      'one': 'o1e',
      'two': 't2o',
      'three': 't3e',
      'four': 'f4r',
      'five': 'f5e',
      'six': 's6x',
      'seven': 's7n',
      'eight': 'e8t',
      'nine': 'n9e'
    }
    for word, digit in replacements.items():
        if all(char not in input_string for char in word):
            input_string = input_string.replace(word, digit)
    print(input_string)
    return input_string

def main():
  file_path = "input.txt"
  process_file(file_path)


if __name__ == "__main__":
  main()
