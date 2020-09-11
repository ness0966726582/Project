
#數據庫https://docs.google.com/spreadsheets/d/1o2A_O2knmDKz3RYKrUhIzRsIuaE22e2YBA2DFJUYTZo/edit#gid=0
#圖表https://datastudio.google.com/u/0/reporting/aa60c4e1-2fef-4f24-8ecb-5559aa860943/page/2GIZB/edit

import functions as uf
import os
from apscheduler.schedulers.blocking import BlockingScheduler
#################################
#外部程式參數模組與判斷值
#################################
M1A_Name=0
M1B_Name=0
M1_H=0
M1_L=0
M2A_Name=0
M2B_Name=0
M2_H=0
M2_L=0
#####################################
#   隨時可調整定義：設定數值判斷       #
#####################################
#引用fintions 
main_now = []                  
main_temp = []                 
main_humi = []                 

now_date = ''                  #變數-日期/時間
now_time = ''                  #變數-日期/時間
DB = 0                        #變數-Sheet上傳內容
data_M1A = 0                  #變數-M2A資料
data_M1B = 0                  #變數-M2B資料
data_M2A = 0                  #變數-M2A資料
data_M2B = 0                  #變數-M2B資料
content_msg = 0               #變數-line告警內容

#---------暫存功能狀態-判斷---------#
data_sent = 0                 #判斷-發送行為---------------N/A
line_alarm = 0                #判斷-line告警
buzzer_alarm = 0              #判斷-BUZZER告警
button = 0                    #判斷-BUTTON狀態
abnormalM1A = 0               #判斷-M2A異常
abnormalM1B = 0               #判斷-M2B異常
abnormalM2A = 0               #判斷-M2A異常
abnormalM2B = 0               #判斷-M2B異常

#####################################
#           定義：實體腳位         
#####################################
buttonPin = 0                 #接收電位狀態
ledPin = 0                    #led on 表示關閉alarm
buzzerPin = 0                 #啟動alarm
lcdPin = 0                    #i2C

#####################################
#---------接口-狀態&LED&讀值---------#
#####################################
#第1-A組
judge_M1A = 0 #---------------------------------------------->SENSOR自動加入數值
led_M1A = 0 ;value_M1A = 0 #自動
#第1-B組
judge_M1B = 0 #---------------------------------------------->SENSOR自動加入數值
led_M1B = 0 ;value_M1B = 0 #自動
#第2-A組
judge_M2A = 0 #---------------------------------------------->SENSOR自動加入數值
led_M2A = 0 ;value_M2A = 0 #自動
#第2-B組
judge_M2B = 0 #---------------------------------------------->SENSOR自動加入數值
led_M2B = 0 ;value_M2B = 0 #自動


def build_creds():
    Output1="creds.json"
    with open(Output1, 'w') as outfile:
            outfile.write('{\n')
            outfile.write(' "type": "service_account",\n')
            outfile.write(' "project_id": "iot-key",\n')
            outfile.write(' "private_key_id": "04bfee8f7ce749ecf204b0a400a6fb0df510e050",\n')
            outfile.write(' "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCwSm4OvJF67leV\\nJDB69u+ALeSQu/abm9sK9ihYHXNqDeFlOnP1F/9UvUdpmYPqzOZP+ZPzCh1ffM9O\\n/ksOEA9RDZEpw48YK5+YTcTkIaMwxsGB3Snf000vlTqfuM9s1ogZ7e3E61tiL1Ng\\nET6JD/RAhLsp5yXQOGoKNY6Sy4FLUSt1wGLPtHpqczpCxn9QeClII3QSAH2Z9Bx/\\nb3aNp1iF3tOiCgZckV2leABIHEiUW/XpwJWf8jAp1Xzmn6M7CEhva0eYl4HSrhCl\\n4cpCOr7yyod/UeVrg4VIN3PEtN4fN4Miha7sripuDuqVZEnMVl3VU0svgRuYScGx\\nnPX50AjdAgMBAAECggEAEMTGVY+D6mS7yaYbbcQ0VtscAn+76Y74gGvsEtRGU1Wx\\nAA8rKCqZW8b0q9ZG5obeoh0pgLTlw1yctDUFuveLGsNxcJQMoJjHAavlaRUhWoqQ\\nAy7K2g1Vf7Za+7C5cO8Hxij2yhmLDpAAMcNM0VPGVia/TjE8TGM5WZxA4goKfo6N\\niCAj+EoRlTR2YOjlzdcmaRQBqi+I1SYOs9l7mqk9tnnkXzy+sU8f0huLxlyF6SGV\\n0ynw84KbTgPIOP1YSdOwAmAZCzYgDZ0StaH9ZtJSnWgb8qWh900EWf0/zbboEz90\\n1JekUyLjAYlX8e0+1fYfNEBwTpnXT763l6cSdsF9LwKBgQDr2l1HSNkTGvBqpnMr\\naz2HRbwsz5GKG4TeolHTy6W48Qj79DRtcFmMabcrVo/qpB6DHrZTSryVAkOw6tiv\\nswWBAg2azFTE1JnrjTYDDIKndnfbgJiDM65idSVeVwiB+DkLWY/t76uBbSC4oaeV\\ngbEwNeMidciseSyF6HFnvMC+0wKBgQC/WY7IzT/z3nluRncYLqTFmrwzPto6o/P7\\nC8QnhN83DVU/9h6rtVOs6FwtLZoucGMpppp43Suic9ix2q6NqpNvRqZWkRBKjTk4\\npi1R9bcMEtCJ+Y2oPR37M8HGBYHL72HYTyUezK4x3eg6Q4Ve1MQwqrm4T9h7pmmc\\nFam0zogrjwKBgQDKS12+islGDdEwaNxX3X/EyxeAB/l5T+lDXE57Ly1R18ww72EY\\njUkBmps1XOXMCEDzjiAsiOn/lRWiZYy+BvstkClDIQeEXCY5V8GAE/bs1Dwx1bb6\\nshVc9cW7iUMO1212QrelCfE87fEm6+Dl53unMlFDeWtKJBUANkMvC0L3aQKBgDz7\\n9wTKXYKEuiDKNnSvkPYljaurcXPVAxJUuqx5rYZnKm9bKoVBIizuVUpUyVnZmdER\\ndxPkMV7yGvL8JjuiTKDfXG4kh5OrFLyYQcNoU3F2oZ4Huf0PlXmVEkHhSW/MmFuP\\nRd5eD3p3JedD08LYfrqf/tbeI7ms3OXRBahJVp7DAoGBAKXGZUqyZPsXiqNtUqLf\\nN1PaYPWvjj5jQ5EVrvzh46lcMNnMogfiTOnawljysuwHB3MPuwJQiwU643krnIbv\\nKMFedkMtrNjcFYwpIz4pYLteeVSpi2m9lzfEB224Qm8jEkqLkIFyv9lI6ENjTJjH\\ntK48l2AY9Unu7uE9mMF7i1xx\\n-----END PRIVATE KEY-----\\n",\n')
            outfile.write(' "client_email": "iot-key@iot-key.iam.gserviceaccount.com",\n')
            outfile.write(' "client_id": "117881879252775568735",\n')
            outfile.write(' "auth_uri": "https://accounts.google.com/o/oauth2/auth",\n')
            outfile.write(' "token_uri": "https://oauth2.googleapis.com/token",\n')
            outfile.write(' "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\n')
            outfile.write(' "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/iot-key%40iot-key.iam.gserviceaccount.com"\n')
            outfile.write('}')
def remove_creds():
    import os, sys
    os.remove("creds.json")

def Sendsheet():
    build_creds()
    ###################################
    #            程式宣告區             #
    ###################################
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials 
    #from pprint import pprint

    ###################################
    #           獲取授權與連結           #
    ###################################
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) #權限金鑰
    remove_creds()
    print(creds)
    client = gspread.authorize(creds)           #使用金鑰
    
    print(client)
    sheet = client.open("2020_IoT數據庫").worksheet('IT-OFFICE')#指定googlesheet
    
    ###################################
    #             寫入方式             #
    ###################################
    row1 = "-","-","M1條件式","-","M2條件式","-"
    row2 = "-","-","高","低","高","低"
    row3 = "-","-",M1_H,M1_L,M2_H,M2_L
    a=['=If(AND(C3>=C7,C7>=C3),"PASS","FAIL")']
    row5 = "-","模組狀態",str(a)[3:39],"M1B帶公式","M2A帶公式","M2B帶公式"
    row6 = "日期","時間",str(M1A_Name),str(M1B_Name),str(M2A_Name),str(M2B_Name)
    row7 = (now_date[2:12]),(now_time[2:7]),int(data_M1A[1]),int(data_M1B[1]),int(data_M2A[1]),int(data_M2B[1])
    #print(title)
    #print(text)
    '''
    index = 1
    sheet.insert_row(row1, index)
    index = 2
    sheet.insert_row(row2, index)
    index = 3
    sheet.insert_row(row3, index)
    '''
    index = 5
    #sheet.insert_row(row5, index)
    '''
    index = 6
    sheet.insert_row(row6, index)
    '''
    index = 7
    sheet.insert_row(row7, index)
    
#################################
#主程式取得~文件.txt
#################################
def getSETUP():
    global M1_H,M1_L
    global M1A_Name,M1B_Name
    global M2_H,M2_L
    global M2A_Name,M2B_Name
    '''
    取得數值module.txt
    '''
    f = open(r'module.txt')
    old = []
    for line in f:
        old.append(line)
        
    data=[ str(old[0]).replace('\n', ''),str(old[1]).replace('\n', ''),str(old[2]).replace('\n', ''),
           str(old[3]).replace('\n', ''),str(old[4]).replace('\n', ''),str(old[5]).replace('\n', ''),
           str(old[6]).replace('\n', ''),str(old[7]).replace('\n', ''),str(old[8]).replace('\n', ''),
           str(old[9]).replace('\n', ''),str(old[10]).replace('\n', ''),str(old[11]).replace('\n', ''),]
    
    M1A=[data[0].replace('\n', ''),data[1].replace('\n', ''),data[2].replace('\n', '')]
    M1B=[data[3].replace('\n', ''),data[4].replace('\n', ''),data[5].replace('\n', '')]
    M2A=[data[6].replace('\n', ''),data[7].replace('\n', ''),data[8].replace('\n', '')]
    M2B=[data[9].replace('\n', ''),data[10].replace('\n', ''),data[11].replace('\n', '')]
    
    #print("模組一 :"+str(M1)); print("模組二 :"+str(M2))
    M1A_Name=M1A[0]; M1_H=M1A[1]; M1_L=M1A[2]      #共用參數
    M1B_Name=M1B[0]; M1_H=M1B[1]; M1_L=M1B[2]      #共用參數
    M2A_Name=M2A[0]; M2_H=M2A[1]; M2_L=M2A[2]      #共用參數
    M2B_Name=M2B[0]; M2_H=M2B[1]; M2_L=M2B[2]      #共用參數
    
#########################    
#-----刷新變數日期時間-----
#########################
def Now():
    global now_date, now_time   # 宣告函式中會用到全域變數a和c
    now_date = str(main_now[0])   
    now_time = str(main_now[1])
    
#########################
#-----刷新變數按鈕狀態-----
#########################
def checkButton():
    global ledPin,button
    if(buttonPin == 1): #當按下按鈕
        ledPin = 1    #LED亮;表示停止
        button = 1    #暫存-按鈕狀態
    else:
        button = 0
##############################
#-----刷新M1讀取數值---------#
##############################
def Ｍ1A():
    global led_M1A,value_M1A,data_M1A
    if (int(judge_M1A) == 1):  #VCC
        led_M1A = 1       #LED亮;表示有設備
        value_M1A = main_temp[0] #---------------------------------------------->SENSOR自動加入數值
        data_M1A = [str(led_M1A),str(value_M1A)]
    else:
        led_M1A = 0
        value_M1A = main_temp[0] #---------------------------------------------->SENSOR自動加入數值
        data_M1A = [str(led_M1A),str(value_M1A)]
    #return data_M2A

def Ｍ1B():
    global led_M1B,value_M1B,data_M1B
    if (int(judge_M1B) == 1):  #VCC
        led_M1B = 1       #LED亮;表示有設備
        value_M1B = main_temp[1] #---------------------------------------------->SENSOR自動加入數值
        data_M1B = [str(led_M1B),str(value_M1B)]
    else:
        led_M1B = 0
        value_M1B = main_temp[1] #---------------------------------------------->SENSOR自動加入數值
        data_M1B = [str(led_M1B),str(value_M1B)]
    #return data_M2B
##############################
#-----刷新M2讀取數值---------#
##############################
def Ｍ2A():
    global led_M2A,value_M2A,data_M2A
    if (judge_M2A == 1):  #VCC
        led_M2A = 1       #LED亮;表示有設備
        value_M2A = main_humi[0] #---------------------------------------------->SENSOR自動加入數值
        data_M2A = [led_M2A,value_M2A]
    else:
        led_M2A = 0
        value_M2A = main_humi[0] #---------------------------------------------->SENSOR自動加入數值
        data_M2A = [led_M2A,value_M2A]
    #return data_M2A

def Ｍ2B():
    global led_M2B,value_M2B,data_M2B
    if (judge_M2B == 1):  #VCC
        led_M2B = 1       #LED亮;表示有設備
        value_M2B = main_humi[1] #---------------------------------------------->SENSOR自動加入數值
        data_M2B = [led_M2B,value_M2B]
    else:
        led_M2B = 0
        value_M2B = main_humi[1] #---------------------------------------------->SENSOR自動加入數值
        data_M2B = [led_M2B,value_M2B]
    #return data_M2B 
#######################################
#-----檢查M1取值並刷新告警變數---------#
#######################################
def check_M1A():
    global line_alarm,abnormalM1A,content_msg,buzzer_alarm
#測試用
#    if(data_M1A[1]=="讀取數值"):
    if(int(data_M1A[1])>int(M1_H) or int(data_M1A[1])<int(M1_L)):
        line_alarm = 1                #啟動Line告警
        abnormalM1A = 1               #狀態異常
        content_msg = "M1A-NG\n"+str(M1A_Name)+"數值 : "+str(data_M1A[1])
        send_msg()
        #print("----刷新----FAIL")
    else:
        line_alarm = 0                #啟動Line告警
        abnormalM1A = 0               #狀態異常
        content_msg = "normal"
        print("----M1A刷新----PASS")

def check_M1B():
    global line_alarm,abnormalM1B,content_msg,buzzer_alarm
#測試用
#    if(data_M1B[1]=="讀取數值"):
    if(int(data_M1B[1])>int(M1_H) or int(data_M1B[1])<int(M1_L)):
        line_alarm = 1                #啟動Line告警
        abnormalM1B = 1               #狀態異常
        content_msg = "M1B-NG"
        send_msg()
        #print("----刷新----FAIL")
    else:
        line_alarm = 0                #啟動Line告警
        abnormalM1B = 0               #狀態異常
        content_msg = "normal"
        print("----M1B刷新----PASS") 
#######################################
#-----檢查M2取值並刷新告警變數---------#
#######################################
def check_M2A():
    global line_alarm,abnormalM2A,content_msg,buzzer_alarm

    if(int(data_M2A[1])>int(M2_H) or int(data_M2A[1])<int(M2_L)):
        line_alarm = 1                #啟動Line告警
        abnormalM2A = 1               #狀態異常
        content_msg = "M2A-NG"
        send_msg()
        #print("----刷新----FAIL")
    else:
        line_alarm = 0                #啟動Line告警
        abnormalM2A = 0               #狀態異常
        content_msg = "normal"
        print("----M2A刷新----PASS")

def check_M2B():
    global line_alarm,abnormalM2B,content_msg,buzzer_alarm

    if(int(data_M2B[1])>int(M2_H) or int(data_M2B[1])<int(M2_L)):
        line_alarm = 1                #啟動Line告警
        abnormalM2B = 1               #狀態異常
        content_msg = "M2B-NG"
        send_msg()
        #print("----刷新----FAIL")
    else:
        line_alarm = 0                #啟動Line告警
        abnormalM2B = 0               #狀態異常
        content_msg = "normal"
        print("----M2B刷新----PASS")
        
###########################
#-----傳送至LINE機器人------#
###########################
def send_msg():
    global line_alarm
    if (line_alarm == 1):
        print("異常設備"+str(content_msg))
    else:
        line_alarm == 0
        
###########################
#---------現場告警---------#
###########################
def buzzer_Alarm():   
    if(button==0 and abnormalM2A==1):
        buzzerStart()              #告警參數調整
    else:
        buzzerStop()
        
def buzzerStart():
    global buzzerPin
    buzzerPin = 1 #啟動
def buzzerStop():
    global buzzerPin
    buzzerPin = 0 #停止

############################
#         取得functions.py   
############################
def get_functions():
    global main_now,main_temp,main_humi
    main_now = uf.fun_now()
    main_temp = uf.temperature()
    main_humi = uf.humidity()
    
###########################
#         程式開始         #
###########################
def data_Refresh():
    get_functions()
    Now()#刷新-時間
    checkButton()#刷新-按鈕狀態
    Ｍ1A()#刷新-接口狀態
    check_M1A()#刷新-判斷變數
    Ｍ1B()#刷新-接口狀態
    check_M1B()#刷新-判斷變數
    Ｍ2A()
    check_M2A()
    Ｍ2B()
    check_M2B()
    buzzer_Alarm()#判斷-現場告警

##################################
#取得感測器資訊引用functions.py
##################################
def tick():
    getSETUP()
    data_Refresh()
    Sendsheet()
    #print('now_date:',now_date)
    #print('now_time:',now_time)
    #print('M1A_Name:',M1A_Name)
    #print('Tick! The temperature is: ',main_temp[0] )
    #print('M1B_Name:',M1B_Name)
    #print('Tick! The temperature is: ',main_temp[1] )
    #print('M2A_Name:',M2A_Name)
    #print('Tick! The humidity is: ',main_humi[0] )
    #print('M2B_Name:',M2B_Name)
    #print('Tick! The humidity is: ',main_humi[1] )
    #print('Tick! The data is: ',main_now[0] )
    #print('Tick! The time is: ',main_now[1] )
    
    #print('Tick! The temperature is: ',main_temp[1] )
    #print('Tick! The humidity is: ',main_humi[1] )
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', hour='00-23',minute='00-59') #每小時的每分鐘取得時間
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
    
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

'''
getSETUP()
print("==================== 取得文字 ============================")
print("M1A:"+ str(M1A_Name)+ "/" + str(M1_H) + "/" + str(M1_L))
print("M2A:"+ str(M2A_Name)+ "/" + str(M2_H) + "/" + str(M2_L))
print("=========================================================")

data_Refresh()
print("=================M1A=================")
print("日期/時間:" + str(now_date) + "/" + str(now_time))
print("【M1A模組_LED/Value:"+ str(data_M1A[0]) + "/" + str(data_M1A[1])+"】")
print("【M1A異常:"+ str(abnormalM1A) +"】【"+"LINE告警:" + str(line_alarm) +"】【"+  "LINE內容:" + str(content_msg +"】"))
print("【停止鈕Button_LED/State:"+ str(ledPin) + "/" + str(button)+"】")
print("【現場告警:"+str(buzzerPin)+"】")
print("=================M2A=================")
print("日期/時間:" + str(now_date) + "/" + str(now_time))
print("【M2A模組_LED/Value:"+ str(data_M2A[0]) + "/" + str(data_M2A[1])+"】")
print("【M2A異常:"+ str(abnormalM2A) +"】【"+"LINE告警:" + str(line_alarm) +"】【"+  "LINE內容:" + str(content_msg +"】"))
print("【停止鈕Button_LED/State:"+ str(ledPin) + "/" + str(button)+"】")
print("【現場告警:"+str(buzzerPin)+"】")

除錯DEBUG
print(M1_H)
print(M1_L)
print(str(data_M1A[1]))
print(M2_H)
print(M2_L)
print(str(data_M2A[1]))
'''