import csv

with open('user_file.csv', mode='w') as user_file:
    user_writer = csv.writer(user_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    username = input("Enter a username: ")
    password = input("Enter a password: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    user_writer.writerow([username, password, name, age])
