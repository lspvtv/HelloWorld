import csv
import json
from __init__ import get_path

# Считываем данные из CSV и JSON файлов
books_file = get_path('books.csv')
with open(books_file, 'r') as f:
    books = list(csv.DictReader(f))

users_file = get_path('users.json')
with open(users_file, 'r') as f:
    users = json.load(f)

inform_users = []
for person in range(len(users)):
    in_user = {
        "name": users[person]["name"],
        "gender": users[person]["gender"],
        "address": users[person]["address"],
        "age": users[person]["age"],
        "books": []
    }
    inform_users.append(in_user)

short_books = []
for book in range(len(books)):
    about_book = {
        "Title": books[book]["Title"],
        "Author": books[book]["Author"],
        "Pages": books[book]["Pages"],
        "Genre": books[book]["Genre"]
    }
    short_books.append(about_book)

books_count = len(short_books) // len(inform_users)
residuals = len(short_books) % len(inform_users)
book_index = 0
for user in range(len(inform_users)):
    user_books = short_books[book_index:book_index + books_count]
    if residuals > 0:
        user_books.append(short_books[book_index + books_count])
        residuals -= 1
        book_index += 1

    inform_users[user]["books"] = user_books
    book_index += books_count

# Записываем результат в JSON файл
with open(get_path('result.json'), 'w') as f:
    json.dump(inform_users, f, indent=4)
