try:
    from .fake_gpio import GPIO # For running app
except ImportError:
    from fake_gpio import GPIO # For running main
# import RPi.GPIO as GPIO # For testing in Raspberry Pi
# import ...
from time import sleep
import random

class MotorController(object):

  def __init__(self):
    self.working = False
    self.current_direction = 'Motor Not Started'
    self.current_rotation = 'Motor Not Started'
    self.init = False

  def start_motor(self):
    self.PIN_STEP = 25 # do not change
    self.PIN_DIR = 8 # do not change
    self.working = False
    self.stop = False
    self.init = True

    CW = 1     # Clockwise Rotation
    CCW = 0    # Counterclockwise Rotation
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_DIR, GPIO.OUT)
    GPIO.setup(self.PIN_STEP, GPIO.OUT)

    random_number = round(random.SystemRandom().uniform(1, 100),2)
    if int(str(random_number).split('.')[0])%2 == 0:
        final_direction = CW
        self.current_direction = 'Clockwwise'
    else:
        final_direction = CCW
        self.current_direction = 'Anti Clockwise'

    if int(str(random_number).split('.')[1])%2 == 0:
        final_steps = 90
        self.current_rotation = '90 Degree'
    else:
        final_steps = 270
        self.current_rotation = '270 Degree'

    GPIO.output(self.PIN_DIR, final_direction)

    step_count = final_steps
    delay = .0208
    self.working = True
    x = 0
    print('Motor started')
    while x < step_count and not self.stop:
        print(F'Rotating {self.current_rotation} in {self.current_direction} direction')
        GPIO.output(self.PIN_STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(self.PIN_STEP, GPIO.LOW)
        sleep(delay)

    sleep(.5)

    GPIO.cleanup()
    self.working = False
    print('Motor stopped')

  def is_working(self):
    return [self.working,self.current_rotation,self.current_direction]

  def stop_motor(self):
    self.stop =True

  def clockwise_rotation(self):
    print('clockwise_rotation')
    if self.init and not self.working:
      print('clockwise_rotation_if')
      self.working = True
      CW = 1     # Clockwise Rotation

      GPIO.output(self.PIN_DIR, CW)
      delay = .0208      
      self.current_rotation = 'Manual'
      self.current_direction = 'Clockwwise'
      GPIO.output(self.PIN_STEP, GPIO.HIGH)
      sleep(delay)
      GPIO.output(self.PIN_STEP, GPIO.LOW)
      sleep(delay)

    self.working = False

  def counter_clockwise_rotation(self):
    
    if self.init and not self.working:
      
      self.working = True
      CCW = 0     # Clockwise Rotation

      GPIO.output(self.PIN_DIR, CCW)
      delay = .0208      
      self.current_rotation = 'Manual'
      self.current_direction = 'Counter Clockwwise'
      GPIO.output(self.PIN_STEP, GPIO.HIGH)
      sleep(delay)
      GPIO.output(self.PIN_STEP, GPIO.LOW)
      sleep(delay)
      print(F'Rotating {self.current_rotation} in {self.current_direction} direction')

    self.working = False



    