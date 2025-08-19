try:
    from .fake_gpio import GPIO # For running app
except ImportError:
    from fake_gpio import GPIO # For running main
# import RPi.GPIO as GPIO # For testing in Raspberry Pi
import time

class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    self.color_from_distance = []
    self.flag = False
    print('Sensor controller initiated')

  def track_rod(self):
    GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(self.PIN_ECHO, GPIO.IN)
    # set Trigger to HIGH
    counter = 0
    measures = []
    total_sum = 0
    self.flag = True
    while counter < 20:
    

      GPIO.output(self.PIN_TRIGGER, True)

      time.sleep(0.00001)
      GPIO.output(self.PIN_TRIGGER, False)

      StartTime = time.time()
      StopTime = time.time()
      
      
      while GPIO.input(self.PIN_ECHO) == 0:
          StartTime = time.time()

      
      while GPIO.input(self.PIN_ECHO) == 1:
          StopTime = time.time()

      # time difference 
      TimeElapsed = StopTime - StartTime

      curr_distance = (TimeElapsed * 34300) / 2
      measures.append(curr_distance)
      total_sum = total_sum + curr_distance
      counter = counter + 1

    print(total_sum)
    self.distance = total_sum/20
    
    if (self.distance >= 14 and self.distance <= 19):
      self.color_from_distance.append(True)
    else:
      self.color_from_distance.append(False)
    if (self.distance >= 9 and self.distance <= 14):
      self.color_from_distance.append(True)
    else:
      self.color_from_distance.append(False)
    if(self.distance >= 4 and self.distance <= 9):
      self.color_from_distance.append(True)
    else:
      self.color_from_distance.append(False)
 
    print('Monitoring')
    self.flag = False
    return self.distance

  def get_distance(self):
    return self.distance

  def get_color_from_distance(self):
    while self.flag:
      pass
    
    return self.color_from_distance
