import tkinter as tk
show1=[]    #顯示模組1的設定name,H,L
show2=[]    #顯示模組2的設定name,H,L
o=[]
def get():
    global old,show1,show2,o
    #先讀取現有數值
    f = open(r'module.txt')
    old = []
    for line in f:
        old.append(line)
    data=[
            str(old[0]).replace('\n', ''),str(old[1]).replace('\n', ''),str(old[2]).replace('\n', ''),
            str(old[3]).replace('\n', ''),str(old[4]).replace('\n', ''),str(old[5]).replace('\n', '')
         ]
    show1=[data[0].replace('\n', ''),data[1].replace('\n', ''),data[2].replace('\n', '')]
    #print(show1)
    show2=[data[3].replace('\n', ''),data[4].replace('\n', ''),data[5].replace('\n', '')]
    #print(show2)
    
def build():
    '''
    修改後數值
    '''
    Output1="module.txt"
    with open(Output1, 'w') as outfile:
            outfile.write(str(show1[0]+"\n")+str(show1[1]+"\n")+str(show1[2]+"\n")),
            outfile.write(str(show2[0]+"\n")+str(show2[1]+"\n")+str(show2[2]+"\n"))
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
    button = tk.Button(window, text = "模組一", command = Module_1)
    button.pack()
    button = tk.Button(window, text = "模組二", command = Module_2)
    button.pack()
    
    window.mainloop()
#####################################
#            Module_1函數
#####################################    
def Module_1():
    global entry
    window = tk.Tk()#產出對話匡
    window.title('模組一')
    window.geometry("300x200+250+150")    # 標示文字
    label = tk.Label(window, text = '請輸入')
    label.pack()    # 輸入欄位
    entry = tk.Entry(window, width = 20) #輸入欄位所在視窗, 輸入欄位的寬度
    entry.pack()    # 按鈕
    button = tk.Button(window, text = "模組一", command = btn_name)
    button.pack()
    button = tk.Button(window, text = "設定H數值", command = setupH)
    button.pack()
    button = tk.Button(window, text = "設定L數值", command = setupL)
    button.pack()
    button = tk.Button(window, text = "修改送出", command = btn_show1)
    button.pack()
    window.mainloop()
def btn_show1():
    global show1
    show1= [name,H,L]
    build()
    window = tk.Tk()         #產出對話匡
    window.title('模組一')
    window.geometry("600x200+550+150")
    # 標示文字
    label = tk.Label(window, text = "命名:" + str(name) + "正常區間" + str(H) + "~ 數值 ~" + str(L))
    label.pack()
#####################################
#            Module_2函數
#####################################    
def Module_2():
    global entry
    window = tk.Tk()#產出對話匡
    window.title('模組二')
    window.geometry("300x200+250+150")    # 標示文字
    label = tk.Label(window, text = '請輸入')
    label.pack()    # 輸入欄位
    entry = tk.Entry(window, width = 20) #輸入欄位所在視窗, 輸入欄位的寬度
    entry.pack()    # 按鈕
    button = tk.Button(window, text = "模組二", command = btn_name)
    button.pack()
    button = tk.Button(window, text = "設定H數值", command = setupH)
    button.pack()
    button = tk.Button(window, text = "設定L數值", command = setupL)
    button.pack()
    button = tk.Button(window, text = "修改送出", command = btn_show2)
    button.pack()
    window.mainloop()
def btn_show2():
    global show2
    show2=[name,H,L]
    build()
    window = tk.Tk()         #產出對話匡
    window.title('模組二')
    window.geometry("600x200+550+150")
    # 標示文字
    label = tk.Label(window, text = "命名:" + str(name) + "正常區間" + str(H) + "~ 數值 ~" + str(L))
    label.pack()
get()
menu()