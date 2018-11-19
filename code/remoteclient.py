import socket
from urllib import parse

def send_cmd(instr):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.3.240',18432))
        client.settimeout(5)
        client.sendall(parse.quote(instr).encode('utf-8'))

    except Exception as e:
        print(e)
    finally:
        client.close()

msg = u"E:\\bat\\t.bat"

send_cmd(msg)
