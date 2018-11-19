import os

net_dict={}

data=os.popen('ipconfig').readlines()

for line in data:

    if "网适配器" in line:

        interface=line[line.index('器')+3:].split(':')[0]

        net_dict[interface]=''

    if 'IPv4' in line:

        ip=line.split(":")[1].strip().split('(')[0]

        net_dict[interface]=ip

for net in net_dict.keys():

    print (net+":"+net_dict[net])       

os.system('pause')
