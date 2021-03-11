from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formtted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formtted_name + '.')
