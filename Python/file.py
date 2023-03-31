while True:
    try:
        filename = input("Enter the filename: ")
        with open(filename, "r") as file:
            print(file.read())
        break
    except FileNotFoundError:
        print("Error: File not found. Please enter a valid filename.")
