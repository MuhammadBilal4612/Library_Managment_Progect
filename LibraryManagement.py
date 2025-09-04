import json

print("Welcome to the Virtual Library")
print("1. Buy\n2. Return")
value = int(input("Enter a number from above according to your purpose: "))

# Load JSON data
with open("first.json", "r") as f:
    data = json.load(f)
    students = data["data"]["student_name"]
    books = data["data"]["book_names"]

if value == 1:
    name = input("Enter your name: ")
    if name in students:
        book_name = input("Which book do you want to read? Enter book name: ")
        book_found = None
        for book in books:
            if book["name"].lower() == book_name.lower():
                book_found = book
                break
        if book_found:
            print(f"This book is available for {book_found['price']} Rs.")
            amount = int(input("Enter amount to purchase this book: "))
            print("You have successfully purchased this book for seven days.")
            print("If you do not return the book after seven days, the fine will be 30 Rs.")
        else:
            print("This book is currently unavailable.")
    else:
        print(f"{name} is not a student of our university. So, {name} is not eligible for the university library.")

elif value == 2:
    name = input("Enter your name: ")
    book_name = input("Enter book name: ")
    book_found = None
    for book in books:
        if book["name"].lower() == book_name.lower():
            book_found = book
            break
    if book_found:
        print(f"Your dues for the book are {book_found['price']} Rs.")
        amount = int(input("Please submit the dues first: "))
        print("You have submitted the book successfully.")
    else:
        print("This book is not recognized in our system.")
