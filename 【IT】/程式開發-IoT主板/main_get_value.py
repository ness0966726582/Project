import functions as uf
import os
from apscheduler.schedulers.blocking import BlockingScheduler

#主程式取得外部程式數值
def tick():
    main_now = uf.fun_now()
    print('Tick! The data is: ',main_now[0] )
    print('Tick! The time is: ',main_now[1] )
    
    main_temp = uf.temperature()
    print('Tick! The temperature is: ',main_temp[0] )
    print('Tick! The temperature is: ',main_temp[1] )
    
    main_humi = uf.humidity()
    print('Tick! The humidity is: ',main_humi[0] )
    print('Tick! The humidity is: ',main_humi[1] )
    
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', hour='00-23',minute='00-59') #每小時的每分鐘取得時間
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
    
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass