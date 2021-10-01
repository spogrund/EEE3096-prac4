import threading
import digitalio
import datetime
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from datetime import datetime
import math
count=0
start = datetime.now()
waits = [1,5,10]
wait =1
print('Runtime    Temp Reading   Temp         Light Reading')
dir(board) 
def print_time_thread():
  global wait
  thread = threading.Timer(wait, print_time_thread)
  thread.daemon = True
  thread.start()
  spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
  cs = digitalio.DigitalInOut(board.D5)

  mcp = MCP.MCP3008(spi, cs)

  chan = AnalogIn(mcp, MCP.P0)
  chan2 = AnalogIn(mcp,MCP.P1)
  end = datetime.now()
  print(str(math.floor((end-start).total_seconds())) + '          ' + str(chan2.value) + '          ' + str(chan2.value/1000) + '       '+str( chan.value))



def btnChangeWaitPressed():
   global count,wait,waits
   count = count+1
   if count>2:
       count=0
   wait = waits[count]
   print(wait)
if __name__ == "__main__":
   
   print_time_thread()
   while True:
      pass





