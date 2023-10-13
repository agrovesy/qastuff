#dictionary

books = {
    "J.R.R. Tolkien": [
        "The Lord of the Rings",
        "Book 2: 'The Hobbit'",
        "Book 3: 'The Silmarillion'"
    ],
    "J.K. Rowling": [
        "Harry Potter and the Sorcerer's Stone",
        "Harry Potter and the Chamber of Secrets",
        "Harry Potter and the Prisoner of Azkaban"
    ],
    "F. Scott Fitzgerald": [
        "The Catcher in the Rye",
        "The Great Gatsby",
        "ender Is the Night"
    ]
}

#name = input("enter author name: ")

#print(", ".join(books[name]))

grade = int(input("insert a grade: "))

if grade >= 85:
    print("distinction")
    
elif 65 <= grade <=85:
    print("pass")
    
else:
    print("fail")
    

