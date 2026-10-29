
import string
import secrets


def generate_password(length):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )
    return password


def main():
    print("===== RANDOM PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length (8-64): "))

        if length < 8 or length > 64:
            print("Error: Choose a length between 8 and 64.")
            return

        password = generate_password(length)

        print("\nYour generated password is:")
        print(password)
        print(f"Password length: {len(password)}")

    except ValueError:
        print("Error: Enter a whole number for the length.")


if __name__ == "__main__":
    main()
