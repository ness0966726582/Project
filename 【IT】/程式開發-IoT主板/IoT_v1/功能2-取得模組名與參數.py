M1A=0
M1_H=0
M1_L=0
M2A=0
M2_H=0
M2_L=0
#################################
#主程式取得模組與數值判斷
#################################
def get():
    global M1A,M1_H,M1_L
    global M2A,M2_H,M2_L
    
    '''
    取得數值
    '''
    f = open(r'module.txt')
    old = []
    for line in f:
        old.append(line)
        
    data=[ str(old[0]).replace('\n', ''),str(old[1]).replace('\n', ''),str(old[2]).replace('\n', ''),
           str(old[3]).replace('\n', ''),str(old[4]).replace('\n', ''),str(old[5]).replace('\n', '')]
    '''
    顯示模組分配
    '''
    M1=[data[0].replace('\n', ''),data[1].replace('\n', ''),data[2].replace('\n', '')]
    M2=[data[3].replace('\n', ''),data[4].replace('\n', ''),data[5].replace('\n', '')]
    print("模組一:"+"\n"+str(M1))
    print("模組二:"+"\n"+str(M2))
    M1A=M1[0]
    M1_H=M1[1]      #共用參數
    M1_L=M1[2]      #共用參數
    M2A=M2[0]
    M2_H=M2[1]      #共用參數
    M2_L=M2[2]      #共用參數
get()
print(M1A,M1_H,M1_L)
print(M2A,M2_H,M2_L)