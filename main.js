/**
 * Updates the current color, distance and motor status calling teh corresponding methods
 */
 function updateStatus() {
  // Update current color based on Open CV
  
  
  // Update motor status
  updateMotorStatus()
  
  // Update current distance
  updateDistance()

  // Update current color based on distance from rod
  updateCurrentColorDistance()


}

/**
 * Update the current color based on OpenCV
 */
 async function updateCurrentColorOpenCV() {
  try {
    // Request color from server
    const requestResult = await requestColorFromOpenCV()
    console.log(requestResult.data)
    const heading_html_element = document.getElementById('distanceFromUltrasonic')
    heading_html_element.innerHTML = requestResult.data
    // Get the HTML element where the status is displayed
    const green_open_cv = document.getElementById('green_open_cv')
    green_open_cv.innerHTML = requestResult.data[0]
    const purple_open_cv = document.getElementById('purple_open_cv')
    purple_open_cv.innerHTML = requestResult.data[1]
    const yellow_open_cv = document.getElementById('yellow_open_cv')
    yellow_open_cv.innerHTML = requestResult.data[2]
  } catch (e) {
    console.log('Error getting the color based on OpenCV', e)
    updateStatus('Error getting the color based on OpenCV')
  }
}

/**
 * Function to request the server to update the current color based on OpenCV
 */
 function requestColorFromOpenCV () {
  try {
    // Make request to server
    console.log('calling distance')
    return axios.get('/get_distance')
    
  } catch (e) {
    console.log('Error getting the status', e)
    updateStatus('Error getting the status')
  }
}


/**
 * Function to request the server to start the motor
 */
async function requestStartMotor () {
  timer = setInterval(updateMotorStatus, 1000)
  try {
    console.log("starting the motor ")
    return axios.get('/start_motor')
  } catch (e) {
    console.log('Error starting the motor status', e)
    updateStatus('Error starting the motor status')
  }
  
  
}


/**
 * Function to request the server to stop the motor
 */
function requestStopMotor () {
  try {
    console.log("stopping the motor ")
    return axios.get('/stop_motor')
  } catch (e) {
    console.log('Error stopping the motor ', e)
    updateStatus('Error stopping the motor ')
  }
}


/**
 * Function to request the server to start the motor
 */
 function requestMotorStatus () {
  try {
    console.log("getting the motor status")
    return axios.get('/motor_status')
  } catch (e) {
    console.log('Error getting the motor status', e)
    updateStatus('Error getting the motor status')
  }
}

/**
 * Update the status of the motor
 * @param {String} status 
 */
async function updateMotorStatus() {
  const requestResult = await requestMotorStatus()
  console.log(requestResult.data)
  const motor_status = document.getElementById('task_3_motor_status')
  motor_status.innerHTML = requestResult.data[0]
  const rotation_status = document.getElementById('task_3_rotation_status')
  rotation_status.innerHTML = requestResult.data[1]
  const direction_status = document.getElementById('task_3_direction_status')
  direction_status.innerHTML = requestResult.data[2]
  
}

/**
 * Update the current color based on distance sensor
 */
async function updateDistance() {
  const requestResult = await requestDistance()
  console.log(requestResult.data)
  const heading_html_element = document.getElementById('task_2_distance')
  heading_html_element.innerHTML = requestResult.data
}


/**
 * Function to request the server to get the distance from
 * the rod to the ultrasonic sensor
 */
function requestDistance() {
  try{
    console.log("getting distance by taking median of 20 measurements")
    return axios.get('/get_distance')
  } catch (e) {
    console.log('Error getting the distance from rod to utrasonic sensor', e)
    updateStatus('Error getting the distance from rod to utrasonic sensor')
  }
}


/**
 * Update the current color based on distance sensor
 */
 async function updateCurrentColorDistance() {
  const requestResult = await requestColorFromDistance()
  console.log(requestResult.data)
  const green_html_element = document.getElementById('task_2_green')
  green_html_element.innerHTML = requestResult.data[0]
  const purple_html_element = document.getElementById('task_2_yellow')
  purple_html_element.innerHTML = requestResult.data[1]
  const yellow_html_element = document.getElementById('task_2_purple')
  yellow_html_element.innerHTML = requestResult.data[2]
}


function myFunction(event) {
  let unicode= event.which;
  if (unicode  == '67' || unicode  == '99' ) {
  	console.log(unicode);
    try {
      console.log("calling clockwise motor manually")
      return axios.get('/manual_clockwise_motor')
    } catch (e) {
      console.log('Error calling clockwise motor manually', e)
      updateStatus('Error calling clockwise motor manually')
    }
  }
  
   if (unicode  == '65' || unicode  == '97' ) {
  	console.log(unicode);
    try {
      console.log("calling counter clockwise motor manually")
      return axios.get('/manual_counter_clockwise_motor')
    } catch (e) {
      console.log('Error calling counter clockwise motor manually', e)
      updateStatus('Error calling counter clockwise motor manually')
    }


  }
	
}

/**
 * Function to request the server to get the color based
 * on distance only
 */
function requestColorFromDistance() {
  try {
    console.log("getting the color based on distance")
    return axios.get('/get_color_from_distance')
  } catch (e) {
    console.log('Error getting the color based on distance', e)
    updateStatus('Error getting the color based on distance')
  }
}
