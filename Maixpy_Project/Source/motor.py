import sensor
import image
import lcd
import time
from fpioa_manager import fm
from machine import Timer,PWM

tim1 = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
tim2 = Timer(Timer.TIMER0, Timer.CHANNEL1, mode=Timer.MODE_PWM)
tim3 = Timer(Timer.TIMER0, Timer.CHANNEL2, mode=Timer.MODE_PWM)
tim4 = Timer(Timer.TIMER0, Timer.CHANNEL3, mode=Timer.MODE_PWM)
ch_LW = PWM(tim1, freq=100, duty=0, pin=14)
ch_RW = PWM(tim2, freq=100, duty=0, pin=13)
ch_SO = PWM(tim3, freq=100, duty=0, pin=8)
ch_SB = PWM(tim4, freq=100, duty=0, pin=12)



def MotorInit():
  ch_LW.duty(0)
  ch_RW.duty(0)
  ch_SO.duty(0)
  ch_SB.duty(0)

def changePWM(n, x, y, dis):
  pwm_L = 0
  pwm_R = 0
  if 6 >= n >= 1 and dis < 400 and y > 110:
    #pwm_L = (240 - y) * (1 - (200 - x)/200)
    #pwm_R = (240 - y) * (1 + (200 - x)/200)
    pwm_L = (33) * (1 - 0.6*(180 - x)/150)
    pwm_R = (33) * (1 + 0.6*(180 - x)/150)
  if pwm_L < 0:
    pwm_L = 0
  if pwm_R < 0:
    pwm_R = 0
  if 120 < x < 160 and 165 < y < 185:
    ch_SO.duty(90)
    time.sleep_ms(600)
    ch_SO.duty(0)
    time.sleep_ms(300)
    ch_SB.duty(90)
    time.sleep_ms(600)
    ch_SB.duty(0)
  ch_LW.duty(int(pwm_L))
  ch_RW.duty(int(pwm_R))
  return pwm_L,pwm_R

