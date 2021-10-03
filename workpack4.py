
import threading
import digitalio
import datetime
import busio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from datetime import datetime
import math
dir(board)
count=0
start = datetime.now()
waits = [1,5,10]
wait =1
print("Runtime        Temp Reading   Temp           Light Reading")
def print_time_thread():
  global wait,btn   
  
  thread = threading.Timer(wait, print_time_thread)
  thread.daemon = True
  thread.start()
  spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
  cs = digitalio.DigitalInOut(board.D5)
  
  
  mcp = MCP.MCP3008(spi, cs)

  chan = AnalogIn(mcp, MCP.P0)
  chan2 = AnalogIn(mcp,MCP.P1)
  end = datetime.now()
  
  temp = ((chan2.voltage-0.5)*100)
  print("{:15s}{:15s}{:15s}{:15s}".format( str(round((end-start).total_seconds(),2)), str(round(chan2.value,2)), str(round(temp,2)), str(round(chan.value,2))))



def btnChangeWaitPressed():
   global wait,count,waits
   count = count+1
   if count>2:
       count = 0
       return waits[0]
   wait = waits[count]
   return wait
   print(wait)

if __name__ == "__main__":
   global btn
   btn = digitalio.DigitalInOut(board.D23)
   btn.direction = digitalio.Direction.INPUT
   btn.pull = digitalio.Pull.DOWN
  
  
   print_time_thread()
   while True:
      
      if btn.value:
      
         wait = btnChangeWaitPressed()
         
     
      time.sleep(0.1)
      pass






