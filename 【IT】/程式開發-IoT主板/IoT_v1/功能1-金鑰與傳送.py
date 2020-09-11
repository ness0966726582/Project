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
    title ="S","A"
    text = "1","2"
    #print(title)
    #print(text)
    index = 1
    sheet.insert_row(title, index)
    index = 2
    sheet.insert_row(text, index)
Sendsheet()