# Функция для конвертации получаемых при обновлении
# расписания данных в корректный вид для помещения
# в базу данных.
# student_id, {"weekday - class_time": class_name}  =>
# => [(class_name, student_id, weekday, class_time)]
# !!! ИМЕННО ТАКОЙ ПОРЯДОК (см. фун. set_schedule) !!!
def convert_update_data(student_id, data):
	result = []

	for key in data.keys():
		result.append((str(data[key]), str(student_id)) + tuple(key.split('-')))

	return result


def get_empty_schedule():
	pass