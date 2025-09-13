import sqlite3


def get_classes(db_name, student_id):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'SELECT weekday_id, class_time_id, class_name_id FROM Classes WHERE student_id = ?',
		(str(student_id), )
		)

	data = cursor.fetchall()
	connection.close()

	return data


def get_classes_times(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'''SELECT * FROM Classes_Times'''
		)

	data = cursor.fetchall()
	connection.close()

	return data


def get_classes_names(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'''SELECT * FROM Classes_Names'''
		)

	data = cursor.fetchall()
	connection.close()

	return data


def get_weekdays(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'''SELECT * FROM Weekdays'''
		)

	data = cursor.fetchall()
	connection.close()

	return data


def get_students(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'''SELECT * FROM Students'''
		)

	data = cursor.fetchall()
	connection.close()

	return data


def set_schedule(db_name, data):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for d in data:

		cursor.execute(
			'UPDATE Classes SET class_name_id = ? WHERE student_id = ? AND weekday_id = ? AND class_time_id = ?',
			d
			)

	connection.commit()
	connection.close()

	return None


if __name__ == '__main__':

	DATABASE_NAME = 'schedule.db'
	print(get_classes_times(DATABASE_NAME))
	print(get_classes_names(DATABASE_NAME))
	print(get_weekdays(DATABASE_NAME))
	print(get_students(DATABASE_NAME))
	print(get_classes(DATABASE_NAME, 1))