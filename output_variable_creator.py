TYPE_MESSAGES = {
    "byte":    "\nEnter a byte value (-128 to 127):\n",
    "short":   "\nEnter a short value (-32768 to 32767):\n",
    "int":     "\nEnter an int value:\n",
    "long":    "\nEnter a long value:\n",
    "float":   "\nEnter a float value (e.g., 3.14):\n",
    "double":  "\nEnter a double value (e.g., 3.14159):\n",
    "char":    "\nEnter a single character:\n",
    "boolean": "\nEnter boolean value (true or false):\n",
    "string":  "\nEnter any string:\n"
}

def is_valid_value(var_type, value):
    try:
        if var_type == "byte":
            return -128 <= int(value) <= 127
        if var_type == "short":
            return -32768 <= int(value) <= 32767
        if var_type in ("int", "long"):
            int(value)
        if var_type in ("float", "double"):
            float(value)
        if var_type == "char":
            return len(value) == 1
        if var_type == "boolean":
            return value in ("true", "false")
        if var_type == "string":
            return True
    except ValueError:
        return False
    return True

def main():
    while True:
        print("\nWelcome to the Variable Creator\n")

        var_name = input("Enter a variable name: \n")
        print("\nChoose a variable type:\n" + "\n".join(TYPE_MESSAGES.keys()) + "\n")
        var_type = input().strip().lower()

        if var_type not in TYPE_MESSAGES:
            print("\nUnsupported type. Program terminated.\n")
            break

        value = None
        while value is None:
            prompt = TYPE_MESSAGES[var_type]
            value = input(prompt).strip()
            if var_type == "boolean":
                value = value.lower()

            if not is_valid_value(var_type, value):
                print(f"Invalid {var_type}. Try again.\n")
                value = None

        print(f"\nVariable successfully declared:\n\nName: {var_name}\nType: {var_type}\nValue: {value}\n")

        if input("\nDo you want to create another variable? (yes/no): ").strip().lower() != "yes":
            print("\nExiting program. Goodbye!\n")
            break

if __name__ == "__main__":
    main()
