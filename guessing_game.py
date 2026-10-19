import random


def get_attempts(score):
    return int(score[1])


def show_leaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            scores = [
                line.strip().split(",")
                for line in f if line.strip()
            ]

        scores = sorted(scores, key=get_attempts)

        print("\n------ LEADERBOARD ------")

        for player, attempts in scores[:5]:
            print(f"{player}: {attempts} attempts")

    except FileNotFoundError:
        print("No scores yet. Be the first to play!")


def guess():
    print("******* Welcome to Guess the Number *******")

    print("\nCHOOSE YOUR DIFFICULTY")
    print("1. EASY (0-50)")
    print("2. MEDIUM (0-100)")
    print("3. HARD (0-500)")

    while True:
        try:
            ch = int(input("Enter your choice (1, 2 or 3): "))

            if ch in (1, 2, 3):
                break

            print("Please select a valid difficulty.")

        except ValueError:
            print("Please enter a number.")

    if ch == 1:
        act = random.randint(0, 50)
    elif ch == 2:
        act = random.randint(0, 100)
    else:
        act = random.randint(0, 500)

    name = input("Enter your name: ").strip()

    if not name:
        name = "Player"

    name = name.replace(",", " ")

    attempts = 0

    while True:
        try:
            gue = int(input("\nEnter your guess: "))
        except ValueError:
            print("Only whole numbers are allowed!")
            continue

        attempts += 1

        diff = abs(act - gue)

        if gue == act:
            print(f"\nHurray {name}! You guessed correctly!")
            break

        elif diff < 10:
            print("You're very close! Keep trying!")

            hint = input("Want a hint? (yes/no): ").lower()

            if hint == "yes":
                if gue < act:
                    print("Try guessing a little higher!")
                else:
                    print("Try guessing a little lower!")

        elif diff < 30:
            print("You're pretty close!")

        elif diff < 50:
            print("You're getting there!")

        else:
            print("You're COLD! Too far from the number!")

    print(f"\nNumber of attempts taken: {attempts}")

    with open("leaderboard.txt", "a") as f:
        f.write(f"{name},{attempts}\n")

    print("Thank you for playing!")

    show_leaderboard()


if __name__ == "__main__":
    guess()