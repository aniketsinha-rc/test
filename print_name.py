import os

def main():
    # Access the name passed as an environment variable
    name = os.getenv('MY_NAME')

    # Print the name
    print("Name:", name)

if __name__ == "__main__":
    main()
