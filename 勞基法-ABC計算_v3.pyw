
import tkinter as tk
import datetime
import json    

#取得Name
import getpass
user=getpass.getuser()

basic = 0 #底薪
level = 0 #階級
whole = 0 #全新

onBoard='2020-01-01'
resign='2020-01-01'
start = datetime.datetime.strptime(onBoard, "%Y-%m-%d")
end =datetime.datetime.strptime(resign, "%Y-%m-%d")
days=0
total_M = 0

pay1=0     #預告期
pay2=0     #資遣費
pay3=0     #失業補助
pay123=0   #加總

def build_creds():
    Output1="creds.json"
    with open(Output1, 'w') as outfile:
            outfile.write('{\n')
            outfile.write(' "type": "service_account",\n')
            outfile.write(' "project_id": "hr-department-282500",\n')
            outfile.write(' "private_key_id": "402999e424a628f561ca9b78044aa98dda78c48d",\n')
            outfile.write(' "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDVmVs1FAV9gqHE\\nzW7KRSeAx1Q3HArE6zTFt45wgKZZxU/VFGmqd8fTi6E0QCk4nECWlGvxJ5K4s7RN\\nBvqWx9GQNB2kla4t/IxHC403NCYZZIkld5XH13zvyNzf4QYxiGukp3bLROmvU6SO\\nmNmCHk44+g7nK+hvv/x77YU2xat3a6ZV3SgTi5HLbxgymdJ6PcNXe/Z2FIUBRmG0\\nIqxSkE25o7HdndFvfAQbR7faTKEDhPojBcb1ETCBj64fvB4SXyq/0I+sc1vmeYUz\\nW9UuPJclT4z0krv08eDhlD8pS846CTVfkuS54929MhxFgLkg09Sq31Z0RPVoCkBj\\nhA77+9LHAgMBAAECggEAQyk1nvJdKZIuCEHp4Iqu+ZRzO+LC1hj4nmRxUpl49MgQ\\nKnkBInsIJ1GDjfjQnT6wJkijyg892HqUqhWULF3G3FcurOXtfwMmHl6Y9+8bPae5\\nYcEApPXyEDkxjelkt6Vj50FKnm5cJecgWj/gQEQEJ3Ekx3YsXxrYKiVMWiT8HY91\\n1shg25DUlBHutgghCGtO/bpenG7J2YF/xu9NHJfXHG0n7VW0hvMNS0Wse5s3RTUE\\nNEy3GAzy1tQdHKk7FwVNUIFg/hHBiz5ybeloSoyFPF7A62/Z8f888k5NzY3YxWJS\\n7HiyXMoztSPlQMRYVzjAiB0kiPawuIp0XqMCLyLkrQKBgQD3CG3IGtgZtyUMWHfM\\nJP06E8eWfPzds1NtosZEe6iXOM5I5c7bvZ6YQsEx825Mr1zF4uG3Li1PcrbYNfdo\\nvVQomvaHET7o3PiU2liQW2VhT7L78Ass1Bpumr9aH1SA+JTDC/oabLZinXXP4xEZ\\njs8A7R8FMHnnlWvkaYu0/XGd0wKBgQDdWj2hYXOhXO2NNbNYVqB4Qa5rgRdTt5Ro\\nqTWk+1yel2QWOqs2qQseApDy/9ySs2C3+HJ8HFY6/iaWW8jsQ8aoWdpoBhdwi9er\\nczWRcDu8XggWEx+dd3RNoKR62LyqiGvtNrxw3D/XsqhyhAVnL8MZQ3LAPZKRv6vC\\nRlGda3W6vQKBgAcZ+u3xt5yloy8DrA32UkFFKEuvNCW7bf6M215En8gZHfUChjvS\\n66g84wjokpcpw2T87LgzX6IVDiSRCJe+OZkhO00OtdxD3fGJhVpBBl0RyXdsoyWa\\nw1fCoxWYKPm8K6qfwYTY8zVKiYR8ZpVxgYnpRycDCb4akYtzbUy6rHV5AoGAI/lV\\niNPIshHjPY7breCuRb0O9sPNIbr1MKlHYZ/EZrXd+0rfpouElgT+v69bjq/+aQfE\\nu2zzirThWpBiMBu3voaT21IaHx1rGJ8ptpBR9QQnNkc3XSUbzr3r3Vc6GlD/kVbS\\n+1igO5L6k1nncuStRX7TuHCJUIyhAnrhKr9bK9UCgYALpjtERFkmUOJ1uUhmY+iP\\nyVVGuBtiQLgTaMgj/62bKYv4URlG+Or3vF3f31zbQ5pXtNQidHs3iM1xlYIUYCQ3\\nWjnzy35ywMEhKRslZZANfmVHa+cMDXIyQMbBm8wZ9ZULpiP26XG3v13ITaIzQskk\\n3MtrOpW2WsVssVZoLmSp/Q==\\n-----END PRIVATE KEY-----\\n",\n')
            outfile.write(' "client_email": "es-728@hr-department-282500.iam.gserviceaccount.com",\n')
            outfile.write(' "client_id": "106031428464360725980",\n')
            outfile.write(' "auth_uri": "https://accounts.google.com/o/oauth2/auth",\n')
            outfile.write(' "token_uri": "https://oauth2.googleapis.com/token",\n')
            outfile.write(' "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\n')
            outfile.write(' "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/es-728%40hr-department-282500.iam.gserviceaccount.com"\n')
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
    sheet = client.open("ES-AUTO").worksheet('HR-資遣成本')#指定googlesheet
    
    ###################################
    #             寫入方式             #
    ###################################
    title ="底薪", "階級津貼","全薪","到職天","滿月份","1.預告期","2.資遣費","3.失業補助","4.加總123成本" ,"Name"
    text = str(basic),str(level),str(whole),str(days),str(total_M),str(pay1),str(pay2),str(pay3),str(pay123),str(user)
    #print(title)
    #print(text)
    #index = 1
    #sheet.insert_row(title, index)
    index = 2
    sheet.insert_row(text, index)
############################################
#            ＧＵＩ相關
############################################

def openTK():
    global M1A,M1B,entry    
    window = tk.Tk()#產出對話匡
    window.title('HR資遣計算')
    window.geometry("300x200+250+150")
    # 標示文字
    label = tk.Label(window, text = '輸入金額')
    label.pack()
    # 輸入欄位
    entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width = 20) # 輸入欄位的寬度
    entry.pack()
    # 按鈕
    button = tk.Button(window, text = "底薪確認", command = btn_basicPay)
    button.pack()
    button = tk.Button(window, text = "階級津貼確認", command = btn_level_pay)
    button.pack()
    button = tk.Button(window, text = "上班日期yyyy-mm-dd", command = btn_onBoard)
    button.pack()
    button = tk.Button(window, text = "資遣日期yyyy-mm-dd", command = btn_resign)
    button.pack()
    button = tk.Button(window, text = "顯示成本", command = btn_show)
    button.pack()
    
    
    window.mainloop()

######################################################################
#    按鈕   # 本薪 /  階級  /全薪  /到職日  /資遣日期   /顯示全部  
######################################################################
def btn_basicPay():
    global basic
    basic = format(entry.get())
    #print("底薪="+str(basic))

def btn_level_pay():
    global level
    level = format(entry.get())
    #print("階級津貼="+str(level))
    
def btn_whole_pay():
    global whole
    whole = int(basic)+int(level)

def btn_onBoard():
    global onBoard
    onBoard = format(entry.get())
    #print(onBoard)
def btn_resign():
    global resign
    resign = format(entry.get())
    #print(resign)
    
def btn_show():
    
    check_days()                   #加入天數計算
    btn_whole_pay()                #全薪計算
    sent_pay1()
    sent_pay2()
    sent_pay3()
    sent_pay123()
    Sendsheet()
    
    window = tk.Tk()         #產出對話匡
    window.title('HR資遣計算')
    window.geometry("600x200+550+150")
    # 標示文字
    label = tk.Label(window, text = "底薪:"+str(basic)+" + "+"階級津貼："+str(level)+" = "+"全薪:"+str(whole)+"[到職天:"+str(days)+"共"+str(total_M)+"月]"+"\n"+"計算結果:"+"\n" + "1.預告期:" + str(pay1) + "\n" +"2.資遣費" + str(pay2) +"\n" + "3.失業補助" + str(pay3) + "\n" +"4.總共" + str(pay123))
    label.pack()
###########################################
#計算區 # 計算到職天數
###########################################
def check_days():
    import datetime
    global days ,start,end,total_M
    # 计算今天和未来一个日期的天数差值
    start = datetime.datetime.strptime(onBoard, "%Y-%m-%d")
    end = datetime.datetime.strptime(resign, "%Y-%m-%d")
    days = (end - start).days
    
    #換算幾個月
    total_M = int(days/30)
    #print(round(total_M))


def sent_pay1(): #預告期
    global pay1
    if(total_M<3):
        pay1=0
    elif(total_M>=3 and total_M<12):
        pay1= int(whole)/30*10
    elif(total_M>=1 and total_M<36):
        pay1= float(whole)/30*20
    elif(total_M>=36):
        pay1= float(whole)/30*30
    #print(whole)
    #print(pay1)
    
def sent_pay2(): #資遣費
    global pay2
    y=int(total_M/12)
    if (y>=1):#一年以上
        pay2 = float(whole*y)
    elif(y<1):
        pay2 = float(whole*(total_M/12))
    
def sent_pay3(): #失業補助
    global pay3
    pay3=float(basic)*0.6*6
    
def sent_pay123():
    global pay123
    pay123=float(pay1)+float(pay2)+float(pay3)
    
openTK()
