import tkinter as tk
show_M1A=[]    #顯示模組1的設定name,H,L
show_M1B=[]
show_M2A=[]    #顯示模組2的設定name,H,L
show_M2A=[]

o=[]
def get():
    global old,show_M1A,show_M1B,show_M2A,show_M2B,o
    #先讀取現有數值
    f = open(r'module.txt')
    old = []
    for line in f:
        old.append(line)
    data=[
            str(old[0]).replace('\n', ''),str(old[1]).replace('\n', ''),str(old[2]).replace('\n', ''),
            str(old[3]).replace('\n', ''),str(old[4]).replace('\n', ''),str(old[5]).replace('\n', ''),
            str(old[6]).replace('\n', ''),str(old[7]).replace('\n', ''),str(old[8]).replace('\n', ''),
            str(old[9]).replace('\n', ''),str(old[10]).replace('\n', ''),str(old[11]).replace('\n', '')
         ]
    show_M1A=[data[0].replace('\n', ''),data[1].replace('\n', ''),data[2].replace('\n', '')]
    #print(show_M1A)
    show_M1B=[data[3].replace('\n', ''),data[4].replace('\n', ''),data[5].replace('\n', '')]
    #print(show_M1B)
    show_M2A=[data[6].replace('\n', ''),data[7].replace('\n', ''),data[8].replace('\n', '')]
    #print(show_M2A)
    show_M2B=[data[9].replace('\n', ''),data[10].replace('\n', ''),data[11].replace('\n', '')]
    #print(show_M2B)
    
def build():
    '''
    修改後數值
    '''
    Output1="module.txt"
    with open(Output1, 'w') as outfile:
            outfile.write(str(show_M1A[0]+"\n")+str(show_M1A[1]+"\n")+str(show_M1A[2]+"\n")),
            outfile.write(str(show_M1B[0]+"\n")+str(show_M1B[1]+"\n")+str(show_M1B[2]+"\n")),
            outfile.write(str(show_M2A[0]+"\n")+str(show_M2A[1]+"\n")+str(show_M2A[2]+"\n")),
            outfile.write(str(show_M2B[0]+"\n")+str(show_M2B[1]+"\n")+str(show_M2B[2]+"\n"))
            
#####################################
#            共用函數
#####################################
name=0     #公用變數
H=0        #公用變數
L=0        #公用變數

def btn_name():
    global name
    name = format(entry.get())    
def setupH():
    global H
    H = format(entry.get())
def setupL():
    global L
    L = format(entry.get())
#####################################
#            menu函數
#####################################    
def menu():
    global entry
    window = tk.Tk()#產出對話匡
    window.title('模組菜單')
    window.geometry("300x200+0+150")    
    button = tk.Button(window, text = "模組-M1A", command = Module_1A)
    button.pack()
    button = tk.Button(window, text = "模組-M1B", command = Module_1B)
    button.pack()
    button = tk.Button(window, text = "模組-M2A", command = Module_2A)
    button.pack()
    button = tk.Button(window, text = "模組-M2B", command = Module_2B)
    button.pack()
    
    window.mainloop()
#####################################
#            Module_1A函數
#####################################    
def Module_1A():
    global entry
    window = tk.Tk()#產出對話匡
    window.title('M1A')
    window.geometry("300x200+250+150")    # 標示文字
    label = tk.Label(window, text = '請輸入')
    label.pack()    # 輸入欄位
    entry = tk.Entry(window, width = 20) #輸入欄位所在視窗, 輸入欄位的寬度
    entry.pack()    # 按鈕
    button = tk.Button(window, text = "更名", command = btn_name)
    button.pack()
    button = tk.Button(window, text = "設定M1_H數值", command = setupH)
    button.pack()
    button = tk.Button(window, text = "設定M1_L數值", command = setupL)
    button.pack()
    button = tk.Button(window, text = "修改送出", command = btn_show_M1A)
    button.pack()
    window.mainloop()
def btn_show_M1A():
    global show_M1A
    show_M1A= [name,H,L]
    build()
    window = tk.Tk()         #產出對話匡
    window.title('M1A')
    window.geometry("600x200+550+150")
    # 標示文字
    label = tk.Label(window, text = "命名:" + str(name) + "正常區間" + str(H) + "~ 數值 ~" + str(L))
    label.pack()
    
#####################################
#            Module_1B函數
#####################################    
def Module_1B():
    global entry
    window = tk.Tk()#產出對話匡
    window.title('M1B')
    window.geometry("300x200+250+150")    # 標示文字
    label = tk.Label(window, text = '請輸入')
    label.pack()    # 輸入欄位
    entry = tk.Entry(window, width = 20) #輸入欄位所在視窗, 輸入欄位的寬度
    entry.pack()    # 按鈕
    button = tk.Button(window, text = "更名", command = btn_name)
    button.pack()
    button = tk.Button(window, text = "設定M1_H數值", command = setupH)
    button.pack()
    button = tk.Button(window, text = "設定M1_L數值", command = setupL)
    button.pack()
    button = tk.Button(window, text = "修改送出", command = btn_show_M1B)
    button.pack()
    window.mainloop()
def btn_show_M1B():
    global show_M1B
    show_M1B= [name,H,L]
    build()
    window = tk.Tk()         #產出對話匡
    window.title('M1B')
    window.geometry("600x200+550+150")
    # 標示文字
    label = tk.Label(window, text = "命名:" + str(name) + "正常區間" + str(H) + "~ 數值 ~" + str(L))
    label.pack()
    
#####################################
#            Module_2A函數
#####################################    
def Module_2A():
    global entry
    window = tk.Tk()#產出對話匡
    window.title('M2A')
    window.geometry("300x200+250+150")    # 標示文字
    label = tk.Label(window, text = '請輸入')
    label.pack()    # 輸入欄位
    entry = tk.Entry(window, width = 20) #輸入欄位所在視窗, 輸入欄位的寬度
    entry.pack()    # 按鈕
    button = tk.Button(window, text = "更名", command = btn_name)
    button.pack()
    button = tk.Button(window, text = "設定M2_H數值", command = setupH)
    button.pack()
    button = tk.Button(window, text = "設定M2_L數值", command = setupL)
    button.pack()
    button = tk.Button(window, text = "修改送出", command = btn_show_M2A)
    button.pack()
    window.mainloop()
def btn_show_M2A():
    global show_M2A
    show_M2A=[name,H,L]
    build()
    window = tk.Tk()         #產出對話匡
    window.title('M2A')
    window.geometry("600x200+550+150")
    # 標示文字
    label = tk.Label(window, text = "命名:" + str(name) + "正常區間" + str(H) + "~ 數值 ~" + str(L))
    label.pack()
#####################################
#            Module_2B函數
#####################################    
def Module_2B():
    global entry
    window = tk.Tk()#產出對話匡
    window.title('M2B')
    window.geometry("300x200+250+150")    # 標示文字
    label = tk.Label(window, text = '請輸入')
    label.pack()    # 輸入欄位
    entry = tk.Entry(window, width = 20) #輸入欄位所在視窗, 輸入欄位的寬度
    entry.pack()    # 按鈕
    button = tk.Button(window, text = "更名", command = btn_name)
    button.pack()
    button = tk.Button(window, text = "設定M2_H數值", command = setupH)
    button.pack()
    button = tk.Button(window, text = "設定M2_L數值", command = setupL)
    button.pack()
    button = tk.Button(window, text = "修改送出", command = btn_show_M2B)
    button.pack()
    window.mainloop()
def btn_show_M2B():
    global show_M2B
    show_M2B=[name,H,L]
    build()
    window = tk.Tk()         #產出對話匡
    window.title('M2B')
    window.geometry("600x200+550+150")
    # 標示文字
    label = tk.Label(window, text = "命名:" + str(name) + "正常區間" + str(H) + "~ 數值 ~" + str(L))
    label.pack()    
get()
menu()