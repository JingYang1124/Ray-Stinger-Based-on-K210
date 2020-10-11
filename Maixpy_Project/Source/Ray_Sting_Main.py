import sensor
import image
import lcd
import time
from machine import UART
from motor import changePWM
from motor import MotorInit
from fpioa_manager import fm
from machine import Timer,PWM
from Blob_Handler import Blob_Handler

MotorInit()
lcd.init(freq=15000000)
sensor.reset()
sensor.set_vflip(1)
sensor.set_hmirror(1)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
red_threshold   = (27, 100, 19, 62, 127, -128)
x = 0
y = 0
old_x = 160
old_y = 120
PWM_LW = 0
PWM_RW = 0
Silent_Count = 0
Wait_Flag = 3
Snapshot_Count = 0
Result = [0,0,0]
while True:
  img=sensor.snapshot()
  if Wait_Flag == 0:
    Snapshot_Count += 1
  if Snapshot_Count == 10:
    if Silent_Count >=5:
      pwm_wheel = changePWM(0, 160, 120, 1000)
      Wait_Flag = 3
    Snapshot_Count = 0
    Silent_Count = 0
  blobs = img.find_blobs([red_threshold])
  sumx = 0
  sumy = 0
  if blobs:
    if Wait_Flag > 0:
      Wait_Flag -= 1
    Result = Blob_Handler(blobs,old_x,old_y)
    tmp=img.draw_cross(int(Result[0]),int(Result[1]))
  lcd.display(img)
  if Wait_Flag == 0 and 6 >= len(blobs) >= 1 and Result[1] > 110 and Result[2] < 400:
    pwm_wheel = changePWM(len(blobs), Result[0], Result[1], Result[2])
    #lcd.draw_string(0, 20, str(pwm_wheel[0]) + "   " + str(pwm_wheel[1]))
  else:
    if Wait_Flag == 0:
      Silent_Count += 1
  lcd.draw_string(0, 0, str(Result[0]) + " + " + str(Result[1]), lcd.RED, lcd.BLACK)
  old_x = Result[0]
  old_y = Result[1]

