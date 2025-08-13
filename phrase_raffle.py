import random

def main():
    first_run = True

    while True:
        phrases = []

        if first_run:
            answer = input("Do you wish to raffle a phrase? (yes/no): ").strip().lower()
            if answer != "yes":
                print("No phrase will be raffled. Goodbye!")
                break
            first_run = False

        print("Please enter 3 phrases:")
        for i in range(1, 4):
            phrase = input(f"Phrase {i}: ")
            phrases.append(phrase)

        chosen_phrase = random.choice(phrases)
        print("Your random phrase is:", chosen_phrase)

        continue_answer = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if continue_answer != "yes":
            print("\nExiting program. Goodbye!\n")
            break

if __name__ == "__main__":
    main()
