try:
    with open("sample.txt", "r") as file:
        print("Reading the file content:")
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
