# The Rod Tracker – Raspberry Pi Project (TU Ilmenau)

The **Rod Tracker** is a Raspberry Pi–based embedded system that combines real-time computer vision, motor control, and distance sensing to track a red marker (“rod”) in 3D space.  
Using OpenCV on the Raspberry Pi, the system detects a red object in a camera feed and continuously adjusts a stepper motor to keep the marker centered. An ultrasonic sensor measures distance to the target, and a Flask-based web interface allows users to monitor and control the system remotely.

---

## Key Features

- Real-time red marker detection
  - Live processing of camera frames using OpenCV.
  - Robust color-based segmentation and contour analysis in HSV/RGB color space.
  - Extracts marker position and converts it into a control signal.

- Closed-loop stepper motor control
  - Uses Raspberry Pi GPIO pins to drive a stepper motor.
  - Computes direction and number of steps based on marker offset from the image center.
  - Continuously updates motor position so the tracked rod stays in view.

- Ultrasonic distance measurement
  - Integrates an ultrasonic sensor to measure distance to the target.
  - Distance can be used to adapt behavior (e.g., stop tracking if too close).

- Web-based dashboard
  - Flask backend serving a lightweight web application.
  - Frontend built with HTML/CSS and JavaScript, using **Axios** for asynchronous requests.
  - Live status view (e.g., tracking state, distance) and basic control options (start/stop, mode switches).

---

## System Architecture

1. Perception – Computer Vision (Python + OpenCV)
- Captures frames from a camera attached to the Raspberry Pi.  
- Converts images to a suitable color space and applies thresholding to isolate the red marker.  
- Uses contour detection / centroid calculation to get the marker’s position in image coordinates.  

2. Control – Motor & Sensor Layer (GPIO) 
- Maps horizontal offset of the marker (left/right of image center) to a step direction and step count.  
- Drives the stepper motor via GPIO using the correct stepping sequence.  
- Reads the ultrasonic sensor to estimate the current distance and optionally adjust motion logic.

3. Web Interface – Flask + JavaScript  
- Flask application exposes REST-like endpoints for:
  - Fetching current system state (marker position, distance, motor state).
  - Controlling the system (start/stop tracking, manual commands).
- Frontend uses Axios to poll or subscribe to updates and render them dynamically without page reloads.

---

## Technology Stack

- Hardware
  - Raspberry Pi (with GPIO access)
  - USB / Pi camera
  - Stepper motor + driver
  - Ultrasonic distance sensor

- Software
  - Python(core logic, OpenCV, Flask)
  - OpenCV for image processing and marker detection
  - Flask for the web server and REST API
  - JavaScript + Axiosfor the browser client
  - HTML/CSS for the dashboard UI
  - Shell / PowerShell scripts for environment setup


### Prerequisites

- Raspberry Pi with:
  - A supported camera module or USB camera
  - Configured GPIO access
  - Python 3.x installed
- Stepper motor, driver board, and ultrasonic sensor wired to the Pi.



This project was developed as part of the **Raspberry Pi Project** at **TU Ilmenau**, focusing on the integration of embedded hardware and real-time computer vision in a practical application.
