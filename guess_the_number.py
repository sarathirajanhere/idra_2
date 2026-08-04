import random
def get_range():
    while True:
        try:
            low = int(input("Enter the lower bound: "))
            high = int(input("Enter the upper bound: "))
            if low >= high:
                print("Lower bound must be less than the upper bound.\n")
                continue
            return low, high
        except ValueError:
            print("Please enter valid integers.\n")
def get_max_attempts(low, high):
    print("\nSelect difficulty:")
    print("  1) Easy")
    print("  2) Medium")
    print("  3) Hard")
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in ("1", "2", "3"):
            size = high - low + 1
            if choice == "1":
                return max(size, 10)
            elif choice == "2":
                return max(size // 2, 7)
            else:
                return max(size // 4, 5)
        print("Please enter 1, 2, or 3.\n")
def get_guess(low, high):
    while True:
        try:
            guess = int(input(f"Enter your guess ({low}–{high}): "))
            if guess < low or guess > high:
                print(f"Guess must be between {low} and {high}.\n")
                continue
            return guess
        except ValueError:
            print("Please enter a valid integer.\n")
def play():
    print("=" * 42)
    print("NUMBER GUESSING GAME ")
    print("=" * 42)
    low, high = get_range()
    max_attempts = get_max_attempts(low, high)
    target = random.randint(low, high)
    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempt(s). Good luck!\n")
    for attempt in range(1, max_attempts + 1):
        guess = get_guess(low, high)
        remaining = max_attempts - attempt

        if guess == target:
            print(f"Correct! You got it in {attempt} attempt(s).\n")
            return True

        if guess < target:
            print(f"Too low!  (Attempts left: {remaining})\n")
        else:
            print(f"Too high! (Attempts left: {remaining})\n")

    print(f"Out of attempts! The number was {target}.\n")
    return False
def main():
    while True:
        play()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
if __name__ == "__main__":
    main()
