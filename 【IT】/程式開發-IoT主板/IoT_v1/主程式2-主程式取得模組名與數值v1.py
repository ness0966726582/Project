#################################
#外部程式參數模組與判斷值
#################################
M1A=0
M1_H=0
M1_L=0
M2A=0
M2_H=0
M2_L=0
#####################################
#   隨時可調整定義：設定數值判斷       #
#####################################
#---------設定數值高/低---------#

now_date = 0                  #變數-日期/時間
now_time = 0                  #變數-日期/時間
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

#################################
#主程式取得~文件.txt
#################################
def getSETUP():
    global M1A_Name,M1_H,M1_L
    global M2A_Name,M2_H,M2_L
    '''
    取得數值module.txt
    '''
    f = open(r'module.txt')
    old = []
    for line in f:
        old.append(line)
        
    data=[ str(old[0]).replace('\n', ''),str(old[1]).replace('\n', ''),str(old[2]).replace('\n', ''),
           str(old[3]).replace('\n', ''),str(old[4]).replace('\n', ''),str(old[5]).replace('\n', '')]
    
    M1=[data[0].replace('\n', ''),data[1].replace('\n', ''),data[2].replace('\n', '')]
    M2=[data[3].replace('\n', ''),data[4].replace('\n', ''),data[5].replace('\n', '')]
    #print("模組一 :"+str(M1)); print("模組二 :"+str(M2))
    M1A_Name=M1[0]; M1_H=M1[1]; M1_L=M1[2]      #共用參數
    M2A_Name=M2[0]; M2_H=M2[1]; M2_L=M2[2]      #共用參數
    
#########################    
#-----刷新變數日期時間-----
#########################
def Now():
    global now_date, now_time   # 宣告函式中會用到全域變數a和c
    now_date = "20202-07-14"   
    now_time = "12:01"   
    
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
#-----刷新M2A讀取數值---------#
##############################
def Ｍ1A():
    global led_M1A,value_M1A,data_M1A
    if (int(judge_M1A) == 1):  #VCC
        led_M1A = 1       #LED亮;表示有設備
        value_M1A = 60 #---------------------------------------------->SENSOR自動加入數值
        data_M1A = [str(led_M1A),str(value_M1A)]
    else:
        led_M1A = 0
        value_M1A = 60 #---------------------------------------------->SENSOR自動加入數值
        data_M1A = [str(led_M1A),str(value_M1A)]
    #return data_M2A
##############################
#-----刷新M2A讀取數值---------#
##############################
def Ｍ2A():
    global led_M2A,value_M2A,data_M2A
    if (judge_M2A == 1):  #VCC
        led_M2A = 1       #LED亮;表示有設備
        value_M2A = 60 #---------------------------------------------->SENSOR自動加入數值
        data_M2A = [led_M2A,value_M2A]
    else:
        led_M2A = 0
        value_M2A = 60 #---------------------------------------------->SENSOR自動加入數值
        data_M2A = [led_M2A,value_M2A]
    #return data_M2A        
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
        print("----刷新----FAIL")
    else:
        line_alarm = 0                #啟動Line告警
        abnormalM1A = 0               #狀態異常
        content_msg = "normal"
        print("----刷新----PASS")
#######################################
#-----檢查M2A取值並刷新告警變數---------#
#######################################
def check_M2A():
    global line_alarm,abnormalM2A,content_msg,buzzer_alarm

    if(int(data_M2A[1])>int(M2_H) or int(data_M2A[1])<int(M2_L)):
        line_alarm = 1                #啟動Line告警
        abnormalM2A = 1               #狀態異常
        content_msg = "M2A-NG"
        send_msg()
        print("----刷新----FAIL")
    else:
        line_alarm = 0                #啟動Line告警
        abnormalM2A = 0               #狀態異常
        content_msg = "normal"
        print("----刷新----PASS")
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
    
###########################
#         程式開始         #
###########################
def data_Refresh():
    Now()#刷新-時間
    checkButton()#刷新-按鈕狀態
    Ｍ1A()#刷新-接口狀態
    check_M1A()#刷新-判斷變數
    Ｍ2A()
    check_M2A()
    buzzer_Alarm()#判斷-現場告警
    

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
'''
除錯DEBUG
print(M1_H)
print(M1_L)
print(str(data_M1A[1]))
print(M2_H)
print(M2_L)
print(str(data_M2A[1]))
'''