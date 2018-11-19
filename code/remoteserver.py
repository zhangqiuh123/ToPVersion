import socket
import os
import threading

import urllib.parse
import ctypes
import datetime

local_ip = '192.168.3.12'
local_port = 18432

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((local_ip,local_port))
server.listen()

#admin_filter = {}
#admin_filter['0.0.0.0']={'exe'}
#admin_filter['127.0.0.1']={'exe'}

#print('white list:' + str(admin_filter))
print('server bind on %s:%s'% (local_ip,local_port))
print('---------------server starting success----------------')

def exe_prog(msg):
    os.system(msg)


while 1:
    conn,addr = server.accept()
    msg = urllib.parse.unquote(conn.recv(1024).decode('utf-8'))

    peer_name = conn.getpeername()
    sock_name = conn.getsockname()

    now_dt = str(datetime.datetime.now())
    
    print(u'%s, visitor: %s:%s'%(now_dt, peer_name[0],peer_name[1]))

    #if peer_name[0] in admin_filter.keys():
    #    print(msg)
    #    if '"quit"' == msg:
    #        conn.close()
    #        exit(0)
            
    t = threading.Thread(target=exe_prog,args=(msg,))
    t.start()


