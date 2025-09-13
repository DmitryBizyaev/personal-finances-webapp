import sqlite3
import db_data


# creating db
def create_db(db_name):
	connection = sqlite3.connect(db_name)
	connection.close()

	return None


# creating classes table in db
def create_classes_table(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Classes (
	class_id INTEGER PRIMARY KEY,
	student_id INTEGER NOT NULL,
	weekday_id INTEGER NOT NULL,
	class_time_id INTEGER NOT NULL,
	class_name_id INTEGER NOT NULL
	)
	''')

	connection.commit()
	connection.close()

	return None


def create_students_table(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Students (
	student_id INTEGER PRIMARY KEY,
	student_firstname TEXT NOT NULL,
	student_lastname TEXT NOT NULL
	)
	''')

	connection.commit()
	connection.close()

	return None


# creating classes times table in db
def create_classes_times_table(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Classes_Times (
	class_time_id INTEGER NOT NULL PRIMARY KEY,
	class_time TEXT NOT NULL
	)
	''')

	connection.commit()
	connection.close()

	return None


# creating classes names table in db
def create_classes_names_table(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Classes_Names (
	class_name_id INTEGER NOT NULL PRIMARY KEY,
	class_name TEXT NOT NULL
	)
	''')

	connection.commit()
	connection.close()

	return None


def create_weekdays_table(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Weekdays (
	weekday_id INTEGER NOT NULL PRIMARY KEY,
	weekday_name TEXT NOT NULL
	)
	''')

	connection.commit()
	connection.close()

	return None


def create_telegram_users_table(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Telegram_Users (
	user_id INTEGER NOT NULL PRIMARY KEY,
	student_id INTEGER NOT NULL
	)
	''')

	connection.commit()
	connection.close()

	return None


# filling db
def fill_students_table(db_name, data):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for d in data:
  		cursor.execute(
  			'INSERT INTO Students (student_firstname, student_lastname) VALUES (?, ?)',
  			d)

	connection.commit()
	connection.close()

	return None


# filling db
def fill_classes_times_table(db_name, data):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for d in data:
  		cursor.execute(
  			'INSERT INTO Classes_Times (class_time_id, class_time) VALUES (?, ?)',
  			d)

	connection.commit()
	connection.close()

	return None


# filling db
def fill_classes_names_table(db_name, data):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for d in data:
  		cursor.execute(
  			'INSERT INTO Classes_Names (class_name_id, class_name) VALUES (?, ?)',
  			d)

	connection.commit()
	connection.close()

	return None


# filling db
def fill_weekdays_table(db_name, data):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for d in data:
  		cursor.execute(
  			'INSERT INTO Weekdays (weekday_id, weekday_name) VALUES (?, ?)',
  			d)

	connection.commit()
	connection.close()

	return None


# filling db
def fill_classes_table(db_name, data):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for d in data:
  		cursor.execute(
  			'INSERT INTO Classes (student_id, weekday_id, class_time_id, class_name_id) VALUES (?, ?, ?, ?)',
  			d)

	connection.commit()
	connection.close()

	return None


def fill_telegram_users_table(db_name, data):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for d in data:
  		cursor.execute(
  			'INSERT INTO Telegram_Users (user_id, student_id) VALUES (?, ?)',
  			d)

	connection.commit()
	connection.close()

	return None


def main():
	DATABASE_NAME = 'schedule.db'
	create_db(DATABASE_NAME)
	create_students_table(DATABASE_NAME)
	create_classes_times_table(DATABASE_NAME)
	create_classes_names_table(DATABASE_NAME)
	create_weekdays_table(DATABASE_NAME)
	create_classes_table(DATABASE_NAME)
	create_telegram_users_table(DATABASE_NAME)
	fill_students_table(DATABASE_NAME, db_data.student_data)
	fill_classes_times_table(DATABASE_NAME, db_data.classes_times_data)
	fill_classes_names_table(DATABASE_NAME, db_data.classes_names_data)
	fill_weekdays_table(DATABASE_NAME, db_data.weekdays_data)
	fill_classes_table(DATABASE_NAME, db_data.classes_data)
	fill_telegram_users_table(DATABASE_NAME, db_data.telegram_data)


if __name__ == '__main__':
	main()