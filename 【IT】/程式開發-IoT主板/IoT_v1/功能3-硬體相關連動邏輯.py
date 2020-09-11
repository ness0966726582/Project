#####################################
#   隨時可調整定義：設定數值判斷       #
#####################################
#---------設定數值高/低---------#
M1_H = 50                     #變數-設定數值高/低
M1_L = 20                     #變數-設定數值高/低

now_date = 0                  #變數-日期/時間
now_time = 0                  #變數-日期/時間
DB = 0                        #變數-Sheet上傳內容

data_M1A = 0                  #變數-M1A資料
data_M1B = 0                  #變數-M1B資料
data_M2A = 0                  #變數-M2A資料
data_M2B = 0                  #變數-M2B資料
content_msg = 0               #變數-line告警內容

#---------暫存功能狀態-判斷---------#
data_sent = 0                 #判斷-發送行為---------------N/A
line_alarm = 0                #判斷-line告警
buzzer_alarm = 0              #判斷-BUZZER告警
button = 0                    #判斷-BUTTON狀態
abnormalM1A = 0               #判斷-M1A異常
abnormalM1B = 0               #判斷-M1B異常
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
judge_M1A =1
led_M1A = 0
value_M1A = 0 
#第1-B組
judge_M1B = 0
led_M1B = 0
value_M1B = 0
#第2-A組
judge_M2A = 0
led_M2A = 0
value_M2A = 0
#第2-B組
judge_M2B = 0
led_M2B = 0
value_M2B = 0 

#########################    
#-----刷新變數日期時間-----
#########################
def Now():
    global now_date, now_time   # 宣告函式中會用到全域變數a和c
    now_date = "2020-06-29"   
    now_time = "12:00"   
    
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
#-----刷新M1A讀取數值---------#
##############################
def Ｍ1A():
    global led_M1A,value_M1A,data_M1A
    if (judge_M1A == 1):  #VCC
        led_M1A = 1       #LED亮;表示有設備
        value_M1A = 60
        data_M1A = [led_M1A,value_M1A]
    else:
        led_M1A = 0
        value_M1A = 0
        data_M1A = [led_M1A,value_M1A]
    return data_M1A
#######################################
#-----檢查M1A取值並刷新告警變數---------#
#######################################
def check_M1A():
    global line_alarm,abnormalM1A,content_msg,buzzer_alarm
#測試用
#    if(data_M1A[1]=="讀取數值"):
    if(int(data_M1A[1])>int(M1_H) or int(data_M1A[1])<int(M1_L)):
        line_alarm = 1                #啟動Line告警
        abnormalM1A = 1               #狀態異常
        content_msg = "M1A-NG"
        send_msg()
    else:
        line_alarm = 0                #啟動Line告警
        abnormalM1A = 0               #狀態異常
        content_msg = "normal"
###########################
#-----傳送至LINE機器人------#
###########################
def send_msg():
    global line_alarm
    if (line_alarm == 1):
        print("異常設備:"+str(content_msg))
    else:
        line_alarm == 0
        
###########################
#---------現場告警---------#
###########################
def buzzer_Alarm():   
    if(button==0 and abnormalM1A==1):
        buzzerStart()              #告警參數調整
    else:
        buzzerStop()
        
def buzzerStart():
    global buzzerPin
    buzzerPin = 1 #啟動
def buzzerStop():
    global buzzerPin
    buzzerPin = 0 #停止
    
###########################
#         程式開始         #
###########################
def data_Refresh():
    Now()#刷新-時間
    checkButton()#刷新-按鈕狀態
    Ｍ1A()#刷新-接口狀態
    check_M1A()#刷新-判斷變數
    buzzer_Alarm()#判斷-現場告警
    
data_Refresh()
print("----刷新----")
print("日期/時間:" + str(now_date) + "/" + str(now_time))
print("【M1A模組_LED/Value:"+ str(data_M1A[0]) + "/" + str(data_M1A[1])+"】")
print("【M1A異常:"+ str(abnormalM1A) +"】【"+"LINE告警:" + str(line_alarm) +"】【"+  "LINE內容:" + str(content_msg +"】"))
print("【停止鈕Button_LED/State:"+ str(ledPin) + "/" + str(button)+"】")
print("【現場告警:"+str(buzzerPin)+"】")