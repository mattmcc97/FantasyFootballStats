from flask import Flask, request, render_template, jsonify
import fantasyJSONpull
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/position_list', methods=['POST'])
def position_list():
	team = request.form['team']
	position = request.form['position']
	print(team)
	if team:
		print(fantasyJSONpull.filter_by_position(int(team), int(position)))
		return render_template('index.html',team = fantasyJSONpull.team_name_from_id(team), 
			position = fantasyJSONpull.position_name_from_element_type(position), 
			position_list = fantasyJSONpull.filter_by_position(int(team), int(position)),
			image_code = "20658")
	else:
		return render_template("index.html")

if __name__ == "__main__":
	app.run(debug="True")