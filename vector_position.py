def display_position(position, length=10):
    if position < 1:
        position = 1
    elif position > length:
        position = length
    vector = ['-'] * length
    vector[position - 1] = 'x'
    return ''.join(vector)

def main():
    print("\nWelcome to the Vector Position Locator!\n")
    vector_length = 10

    while True:
        user_input = input(f"Please enter your position (1 to {vector_length}) or type 'exit' to quit:\n> ").strip()
        if user_input.lower() == 'exit':
            print("\nExiting program... Thank you for using the Vector Position Locator. Goodbye!\n")
            break

        if not user_input.isdigit():
            print("\nOops! That doesn't look like a valid number. Please try again.\n")
            continue

        pos = int(user_input)
        if not (1 <= pos <= vector_length):
            print(f"\nYour input is out of range! Please enter a number between 1 and {vector_length}.\n")
            continue

        position_display = display_position(pos, vector_length)
        print(f"\nYour position in the vector is:\n({position_display})\n")

if __name__ == "__main__":
    main()