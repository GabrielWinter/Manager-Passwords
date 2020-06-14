import sqlite3
import os
import new_password
import searchall
import delete

ADMIN_PASSWORD = "admin"
connect = input("Enter your password: ")

while connect != ADMIN_PASSWORD:
	connect = input("Enter your password: ")
	if connect == 'q': break
	os.system('clear')


conn = sqlite3.connect('database.db')
c = conn.cursor()
print(conn)


while True:
	os.system('clear')
	print("\nWelcome to the Password Vault\n")
	print("Commands:")
	print("s = See all passwords")
	print("n = New password")
	print("d = Delete password")
	print("q = Quit")

	userInput = input("Enter command: ")
	if userInput == 's': searchall.search_all()
	elif userInput == 'n': new_password.new()
	elif userInput == 'd': delete.delete_password()
	elif userInput == 'q':
		break

