from flask import Flask, render_template, request, redirect
import app_db_requests
import app_functions


app = Flask(__name__)

@app.route("/")
def start_page():
	student_list = app_db_requests.get_students(DATABASE_NAME)
	return render_template("start-page-template.html", students=student_list)


@app.route("/schedule")
def schedule_page():

	student_list = app_db_requests.get_students(DATABASE_NAME)

	current_student_id = request.args.get('student')

	print(current_student_id)

	current_schedule = app_db_requests.get_classes(DATABASE_NAME, int(current_student_id))

	return render_template(
		"schedule-template.html",
		students=student_list,
		weekdays=CLASSES_WEEKDAYS, 
		times=CLASSES_TIMES, 
		classes=CLASSES_NAMES, 
		schedule=current_schedule,
		student_id=current_student_id)


@app.route("/update", methods=['POST'])
def schedule_table():
	current_student_id = request.args.get('student')

	data = app_functions.convert_update_data(
		current_student_id,
		request.form.to_dict()
	)

	app_db_requests.set_schedule(DATABASE_NAME, data)

	return redirect(f'/schedule?student={current_student_id}')


if __name__ == '__main__':

	DATABASE_NAME = 'schedule.db'

	CLASSES_TIMES = dict(app_db_requests.get_classes_times(DATABASE_NAME))
	CLASSES_WEEKDAYS = dict(app_db_requests.get_weekdays(DATABASE_NAME))
	CLASSES_NAMES = dict(app_db_requests.get_classes_names(DATABASE_NAME))

	app.run(host="0.0.0.0", port="5000")