from flask import Flask, render_template, Response, request, jsonify
from datetime import datetime
from task3_sensor_control.sensor_controller import SensorController
from task2_motor_control.motor_controller import MotorController
import re
import os


app = Flask(__name__)

sensor_controller = SensorController()
motor_controller = MotorController()

# @app.route("/")
# def home():
#     return "Testing Flask Project !"

# Server view to access the app and display the index template
@app.route('/')
def index():
    return render_template('index.html')

# Server view to start the motor
@app.route('/start_motor')
def start_motor():
    motor_controller.start_motor()
    return { 'success': True }

# Server view to stop the motor
@app.route('/stop_motor')
def stop_motor():
    motor_controller.stop_motor()
    return { 'success': True }

@app.route('/manual_clockwise_motor')
def manual_clockwise_motor():
    motor_controller.clockwise_rotation()
    return { 'success': True }

@app.route('/manual_counter_clockwise_motor')
def manual_counter_clockwise_motor():
    motor_controller.counter_clockwise_rotation()
    return { 'success': True }

# Server view to get status of the motor (working or not working)
@app.route('/motor_status')
def motor_status():
    status = motor_controller.is_working()
    return jsonify(status)



@app.route('/get_distance')
def hello_there(name = None):
    distance = sensor_controller.track_rod()
    return jsonify(distance)


    # return render_template(
    #     "hello_there.html",
    #     action = 'Total Distance',
    #     value=str(distance),
    #     date=datetime.now()
    # )

@app.route('/get_color_from_distance')
def get_color_from_distance():
    color = sensor_controller.get_color_from_distance()
    return jsonify(color)


    # return render_template(
    #     "hello_there.html",
    #     action = 'Color Detected',
    #     value=str(color),
    #     date=datetime.now()
    # )



if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))

