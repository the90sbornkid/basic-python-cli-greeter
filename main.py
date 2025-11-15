def greet(name: str) -> str:
    """
    Return a greeting message.
    """
    return f"Hello, {name}! Welcome to the program."

def main():
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

if __name__ == "__main__":
    main()
