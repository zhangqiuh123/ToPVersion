import time

def stamp_to_time(value):
    format="%Y-%m-%d %H:%M:%S"
    t=time.localtime(value)
    dt=time.strftime(format,t)
    return dt

def stat_proc():
    orders=open('./login.txt')
    player_list = [i.split("\t")[1] for i in orders]
    print("PV:",len(player_list))

#print(stamp_to_time())


if __name__=='__main__':
    stat_proc()
    time.sleep(1)
