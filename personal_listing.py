class Person:
    def __init__(self):
        self.name = ""
        self.fruits = []

    def set_name(self, name):
        self.name = name

    def add_fruit(self, fruit):
        if len(self.fruits) < 3:
            self.fruits.append(fruit)

    def get_name(self):
        return self.name

    def get_fruits(self):
        return self.fruits


def main():
    while True:
        people = []

        for _ in range(3):
            person = Person()
            person.set_name(input("Type your name: "))

            print("\nWhat's your favorite foods: ")
            for _ in range(3):
                person.add_fruit(input())

            print("\nInformation captation finished\n")
            people.append(person)

        input_name = input("Identify yourself: ")

        found = False
        for p in people:
            if p.get_name().lower() == input_name.lower():
                print(f"\n{p.get_name()}, your favorite foods are: {', '.join(p.get_fruits())}\n")
                print("\nProgram ended\n")
                found = True
                break

        if not found:
            print("\nInvalid person")
            print("Program ended\n")

        continue_answer = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if continue_answer != "yes":
            print("\nExiting program. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
