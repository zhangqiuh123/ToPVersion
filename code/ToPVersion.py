from tkinter import *
from hashlib import sha1
import socket
from urllib import parse
import pymysql
import hashlib
import time
import easygui

LOG_LINE_NUM = 0

class TPV_LoginGui():
    def __init__(self,login):
        self.login = login
        

    def LoginMenu(self):
        self.login.title("ToPVersion 1.0")
        self.login.geometry('280x120+800+200')
        self.login["bg"] = "GhostWhite"
        self.login.attributes("-alpha",1)
        self.user_for_login=Label(self.login,text='帐号 :').grid(row=0,column=0)
        self.passwd_for_login=Label(self.login,text='密码 :').grid(row=1,column=0)

        v1=StringVar()
        v2=StringVar()

        self.e1 = Entry(self.login,textvariable=v1)
        self.e2 = Entry(self.login,textvariable=v2,show='*')
        self.e1.grid(row=0,column=1,padx=10,pady=5)
        self.e2.grid(row=1,column=1,padx=10,pady=5)

        Button(self.login,text='登录',width=10,command=self.ToLoginForUser).grid(row=5,column=0,sticky=W,padx=10,pady=5)
        Button(self.login,text='退出',width=10,command=self.LoginClose).grid(row=5,column=1,sticky=E,padx=10,pady=5)

        self.login.mainloop()

    def ToLoginForUser(self):
        UserName = self.e1.get()
        UserPasswd = self.e2.get()

        db = pymysql.Connect(host='192.168.3.13',port=5532,user='dbuser',passwd='sj@#$dsf8jhKIJ2f',db='deployversion',charset='utf8')
        cursor = db.cursor()
        SqlForUser = "SELECT COUNT(*) FROM userlogin WHERE username= '%s' AND passwd='%s'" % (UserName,UserPasswd)
        SqlForValid = "SELECT isValid FROM userlogin WHERE username= '%s' AND passwd='%s'" % (UserName,UserPasswd)

        cursor.execute(SqlForUser)
        result_user = cursor.fetchone()
        
        cursor.execute(SqlForValid)
        result_valid = cursor.fetchone()

        if result_user[0] != 1:
            easygui.msgbox('用户名或密码错误，请重新输入',title='输入有误',ok_button="确定")
            #print("用户名或密码错误，请重新输入")
        else:
            if result_valid[0] != 1:
                easygui.msgbox('该用户已被禁用!',title='登陆',ok_button="确定")
            else:
                easygui.msgbox('登陆成功!',title='登陆',ok_button="确定")
                #print("成功登陆！")
                self.LoginClose()
                TPV_LoginGui.MainMenu()
            #TPV_LoginGui.MainMenu.Logs("成功登陆!")
            
        db.close()
        
    def LoginClose(self):
        self.login.destroy()


    def MainMenu():
        menu = Tk()
        menu.title("ToPVersion 1.0 测试版")
        menu.geometry('550x400+800+200')
        menu["bg"] = "GhostWhite"
        menu.attributes("-alpha",1)
    
        label_uat=Label(menu,text='UAT版本发布 :').grid(row=0,column=0)
        label_rp=Label(menu,text='72版本发布 :').grid(row=1,column=0)
        label_awl=Label(menu,text='爱玩乐（不可用）:').grid(row=2,column=0)
        label_jwen=Label(menu,text='佳雯(不可用):').grid(row=3,column=0)
        label_kum=Label(menu,text='昆明（不可用):').grid(row=4,column=0)
        label_logs=Label(menu,text='日志:').grid(row=5,column=0)

        UpdateUatRetailking=Button(menu,text='reailking',width=10,command=TPV_Update.Update_Uat_Retailking).grid(row=0,column=1,sticky=W,padx=10,pady=5) 
        UpdateUatDatacenter=Button(menu,text='datacenter',width=10,command=TPV_Update.Update_Uat_Datacenter).grid(row=0,column=2,sticky=E,padx=10,pady=5)
        UpdateUatRpeort=Button(menu,text='report',width=10,command=TPV_Update.Update_Uat_Report).grid(row=0,column=3,sticky=E,padx=10,pady=5)
        UpdateUatHis=Button(menu,text='his',width=10,command=TPV_Update.Update_Uat_His).grid(row=0,column=4,sticky=E,padx=10,pady=5)

        Update72Retailking=Button(menu,text='reailking',width=10,command=TPV_Update.Update_72_Retailking).grid(row=1,column=1,sticky=W,padx=10,pady=5) 
        Update72Datacenter=Button(menu,text='datacenter',width=10,command=TPV_Update.Update_72_Datacenter).grid(row=1,column=2,sticky=E,padx=10,pady=5)
        Update72Rpeort=Button(menu,text='report',width=10,command=TPV_Update.Update_72_Report).grid(row=1,column=3,sticky=E,padx=10,pady=5)
        Update72His=Button(menu,text='his',width=10,command=TPV_Update.Update_72_His).grid(row=1,column=4,sticky=E,padx=10,pady=5)

        UpdateAWLRetailking=Button(menu,text='reailking',width=10,command=TPV_Update.Update_AWL_Retailking).grid(row=2,column=1,sticky=W,padx=10,pady=5) 
        UpdateAWLDatacenter=Button(menu,text='datacenter',width=10,command=TPV_Update.Update_AWL_Datacenter).grid(row=2,column=2,sticky=E,padx=10,pady=5)
        UpdateAWLRpeort=Button(menu,text='report',width=10,command=TPV_Update.Update_AWL_Report).grid(row=2,column=3,sticky=E,padx=10,pady=5)
        UpdateAWLHis=Button(menu,text='his',width=10,command=TPV_Update.Update_AWL_His).grid(row=2,column=4,sticky=E,padx=10,pady=5)

        UpdateJiaWenRetailking=Button(menu,text='reailking',width=10,command=TPV_Update.Update_JiaWen_Retailking).grid(row=3,column=1,sticky=W,padx=10,pady=5) 
        UpdateJiaWenDatacenter=Button(menu,text='datacenter',width=10,command=TPV_Update.Update_JiaWen_Datacenter).grid(row=3,column=2,sticky=E,padx=10,pady=5)
        UpdateJiaWenRpeort=Button(menu,text='report',width=10,command=TPV_Update.Update_JiaWen_Report).grid(row=3,column=3,sticky=E,padx=10,pady=5)
        UpdateJiaWenHis=Button(menu,text='his',width=10,command=TPV_Update.Update_JiaWen_His).grid(row=3,column=4,sticky=E,padx=10,pady=5)

        UpdateKunMRetailking=Button(menu,text='reailking',width=10,command=TPV_Update.Update_KunM_Retailking).grid(row=4,column=1,sticky=W,padx=10,pady=5) 
        UpdateKunMDatacenter=Button(menu,text='datacenter',width=10,command=TPV_Update.Update_KunM_Datacenter).grid(row=4,column=2,sticky=E,padx=10,pady=5)
        UpdateKunMRpeort=Button(menu,text='report',width=10,command=TPV_Update.Update_KunM_Report).grid(row=4,column=3,sticky=E,padx=10,pady=5)
        UpdateKunMHis=Button(menu,text='his',width=10,command=TPV_Update.Update_KunM_His).grid(row=4,column=4,sticky=E,padx=10,pady=5)

        log_data_Text = Text(menu, width=66, height=12)
        log_data_Text.grid(row=6, column=0, columnspan=10)
        
        mainloop()

        def get_current_time():
            current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            return current_time
    
        def Logs(logmsg):
            global LOG_LINE_NUM
            current_time = TPV_LoginGuiget_current_time()
            logmsg_in = str(current_time) +": " + str(logmsg) + "\n"
            if LOG_LINE_NUM <= 7:
                log_data_Text.insert(END,logmsg_in)
                LOG_LINE_NUM = LOG_LINE_NUM + 1
            else:
                log_data_Text.delete(1.0,2.0)
                log_data_Text.insert(END,logmsg_in)
            
        

class TPV_Update():

    def send_cmd(ipaddr,instr):
        if easygui.ccbox("是否发布版本？",choices=("确定","我再考虑考虑")):
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((ipaddr,18432))
                client.settimeout(5)
                client.sendall(parse.quote(instr).encode('utf-8'))
            except Exception as e:
                easygui.msgbox(e,title='提示',ok_button="确定")
            finally:
                client.close()
        else:
            sys.exit(0)
            
        
    def Update_72_Retailking():
        msg = u"D:\\web\\bat\\retailkingupdate.bat"
        addr = "14.116.138.72"
        TPV_Update.send_cmd(addr,msg)
        easygui.msgbox("成功发布！",title='提示',ok_button="确定")
        
    def Update_72_Datacenter():
        msg = u"D:\\web\\bat\\datacenterupdate.bat"
        addr = "14.116.138.72"
        TPV_Update.send_cmd(addr,msg)
        easygui.msgbox("成功发布！",title='提示',ok_button="确定")
        
    def Update_72_Report():
        msg = u"D:\\web\\bat\\reportupdate.bat"
        addr = "14.116.138.72"
        TPV_Update.send_cmd(addr,msg)
        easygui.msgbox("成功发布！",title='提示',ok_button="确定")
        
    def Update_72_His():
        msg = u"D:\\web\\bat\\hisupdate.bat"
        addr = "14.116.138.72"
        TPV_Update.send_cmd(addr,msg)
        easygui.msgbox("成功发布！",title='提示',ok_button="确定")

    def Update_Uat_Retailking():
        msg = u"D:\\web\\bat\\retailkingupdate.bat"
        addr = "192.168.3.12"
        TPV_Update.send_cmd(addr,msg)
        easygui.msgbox("成功发布！",title='提示',ok_button="确定")
        
    def Update_Uat_Datacenter():
        msg = u"D:\\web\\bat\\datacenterupdate.bat"
        addr = "192.168.3.12"
        TPV_Update.send_cmd(addr,msg)
        easygui.msgbox("成功发布！",title='提示',ok_button="确定")
        
    def Update_Uat_Report():
        msg = u"D:\\web\\bat\\reportupdate.bat"
        addr = "192.168.3.12"
        TPV_Update.send_cmd(addr,msg)
        easygui.msgbox("成功发布！",title='提示',ok_button="确定")
        
    def Update_Uat_His():
        msg = u"D:\\web\\bat\\hisupdate.bat"
        addr = "192.168.3.12"
        TPV_Update.send_cmd(addr,msg)
        easygui.msgbox("成功发布！",title='提示',ok_button="确定")

    def Update_AWL_Retailking():
        msg = u"D:\\web\\bat\\retailkingupdate.bat"
        addr = "139.224.223.90"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_AWL_Datacenter():
        msg = u"D:\\web\\bat\\datacenterupdate.bat"
        addr = "139.224.223.90"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_AWL_Report():
        msg = u"D:\\web\\bat\\reportupdate.bat"
        addr = "139.224.223.90"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_AWL_His():
        msg = u"D:\\web\\bat\\hisupdate.bat"
        addr = "139.224.223.90"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)

    def Update_JiaWen_Retailking():
        msg = u"D:\\web\\bat\\retailkingupdate.bat"
        addr = "39.104.160.254"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_JiaWen_Datacenter():
        msg = u"D:\\web\\bat\\datacenterupdate.bat"
        addr = "39.104.160.254"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_JiaWen_Report():
        msg = u"D:\\web\\bat\\reportupdate.bat"
        addr = "39.104.160.254"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_JiaWen_His():
        msg = u"D:\\web\\bat\\hisupdate.bat"
        addr = "39.104.160.254"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)

    def Update_KunM_Retailking():
        msg = u"D:\\web\\bat\\retailkingupdate.bat"
        addr = "120.79.21.122"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_KunM_Datacenter():
        msg = u"D:\\web\\bat\\datacenterupdate.bat"
        addr = "120.79.21.122"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_KunM_Report():
        msg = u"D:\\web\\bat\\reportupdate.bat"
        addr = "120.79.21.122"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)
        
    def Update_KunM_His():
        msg = u"D:\\web\\bat\\hisupdate.bat"
        addr = "120.79.21.122"
        easygui.msgbox('该功能暂时不可用!',title='提示',ok_button="确定")
        #TPV_Update.send_cmd(addr,msg)


def GuiStart():
    ToPVersion = Tk()
    login = TPV_LoginGui(ToPVersion)
    login.LoginMenu()


GuiStart()
