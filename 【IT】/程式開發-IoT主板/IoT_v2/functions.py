from time import *
import time;  # 引入time模块
#import Adafruit_DHT
M1A_pin = 4
M1B_pin = 5
M2A_pin = 6
M2B_pin = 7

def fun_now():
        nowD = time.strftime("%Y-%m-%d", time.localtime())
        nowH = time.strftime('%H', time.localtime())
        nowM = time.strftime('%M', time.localtime())
        nowDate = [str(nowD)]
        nowTime = [str(nowH)+":"+str(nowM)]
        #print(time.strftime("%Y", time.localtime())+"年"+time.strftime("%m", time.localtime())+"月"+time.strftime("%d", time.localtime())+"日")
        print("nowDate:",nowDate)
        print("nowTime",nowTime)
        return [nowDate,nowTime]
    
def temperature():
        t = [101,50]
        #h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, M1A_pin)
        #h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, M1B_pin)
        print("溫度:"+str(t))
        return [t[0],t[1]]
    
def humidity():
        h = [15,25]
        #h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, M2A_pin)
        #h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, M2B_pin)
        print("濕度:"+str(h))
        return [h[0],h[1]]
    
def main():
      print("Testing main function")
      print("------VAR PASS------")
      
if __name__ == '__main__':
      #main()
      fun_now()
      temperature()
      humidity()