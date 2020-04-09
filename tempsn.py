#coding:utf-8
#!/usr/bin/python3
from selenium import webdriver
import time
import random
import csv
import re
import json
import serial
import os

#this is for github test
#echo修改/etc/config/system文件,echo.输出一个空行
os.system("echo \"Hello World\"")
os.system("echo config system 'system' > dhb333")
os.system("echo \toption timezone 'UTC' >> dhb333")
os.system("echo \toption ttylogin '1' >> dhb333")
os.system("echo \toption log_size '10240' >> dhb333")
os.system("echo \toption conloglevel '6' >> dhb333")
os.system("echo \toption klogconloglevel '6' >> dhb333")
os.system("echo \toption urandom_seed '0' >> dhb333")
os.system("echo \toption log_proto 'udp' >> dhb333")
os.system("echo \toption log_port '514' >> dhb333")
os.system("echo \toption log_file '/var/log/messages' >> dhb333")
os.system("echo \toption log_ip 'log.dyiots.com' >> dhb333")
os.system("echo \toption netmodel '0' >> dhb333")
os.system("echo \toption hostname '21012C000007' >> dhb333")
os.system("echo.  >> dhb333")
os.system("echo config timeserver 'ntp' >> dhb333")
os.system("echo \toption enabled '1' >> dhb333")
os.system("echo \toption enable_server '1' >> dhb333")
os.system("echo \tlist server 'pool.ntp.org' >> dhb333")
os.system("echo \tlist server 'cn.ntp.org.cn' >> dhb333")

#if连写
# err=0
# status = 1 if err else 0
# print (status)

#目录操作
# currentpwd=os.getcwd()
# logdir=currentpwd+"\log"
# filename=logdir+'\\'+"bbb.txt"
# print (currentpwd,logdir)
# with open(filename, "w") as csvwritefile:
#     print ("haha")
#     csvwritefile.close()

#float比较-20,24.9
# devrealdata_value=24.9
# simulate_value=24.9
# if (float(devrealdata_value)!= float(simulate_value)):
#     print ("不相等")
# else:
#     print ("相等")

#字符串转元组
# params5 = (('page', '1'),('size', '50'),('upLinkDeviceId', '20478042'),('pageNum', '1'),)
# print (params5,params5[2][1])
# params5="(('page', '1'),('size', '50'),('upLinkDeviceId', '"+str(19999999)+"'),('pageNum', '1'))"
# print (params5)
# changepara5=tuple(eval(params5))
# print (changepara5)
#元组嵌套
# aaa=[('a', 2), ('d', 4), ('e', 3), ('f', 8)]
# print (aaa[0][0])
# print (aaa[0][1])

# for i in range(1,5+1):
#     print (i)

# dfhtmp='Filesystem   Size      Used Available Use% Mounted on /dev/root  3.6G    185.2M      3.2G   5% / tmpfs   248.4M    160.1M     88.3M  64% /tmp tmpfs       512.0K    0    512.0K   0% /dev'
# apppercentage=re.search('(\d+)%',str(dfhtmp)).group()
# digitapppercentage=re.search('\d+',str(apppercentage)).group()
# percentage=re.search('tmpfs(.*)(\d+)%',str(dfhtmp)).group()
# tmppercentage=re.search('\d+%',str(percentage)).group()
# digittmppercent=re.search('\d+',str(tmppercentage)).group()
# #print ("dfhtmp:",dfhtmp)
# #print ("percentage:",percentage)
# print ("apppercentage:",apppercentage)
# print ("digitapppercentage:",digitapppercentage)
# if int(digittmppercent)>=50:
#     print ("tmp too large")
# else:
#     print ("Fine")

# def on_message(msg):
#     print ("msg:",msg)
#     payload = msg.payload.decode().strip().replace('\\n', '').replace('\\t', '')
#     print("payload:", payload)
#     data = json.loads(payload)
#     print ("data:",data)
#     to_serial = base64.b64decode(data['raw_data'])
#     print("to_serial:", to_serial)
#     #self.ser.write(to_serial)
#
# xshellprint={'identifier':'transparent'}
# jsonxshell=json.loads(xshellprint)
# on_message(jsonxshell)

#在Python标准库的json包中，提供了JSONEncoder和JSONDecoder两个类来实现Json字符串和dict类型数据的互相转换。
# if __name__=="__main__":
#    d={}
#    d['a'] =1
#    d['b']=2
#    d[3]='c'
#    d[4]=['k','k1']
#    #将Python dict类型转换成标准Json字符串
#    k=json.JSONEncoder().encode(d)
#    print(type(k))
#    print(k)
#    #将json字符串转换成Python dict类型
#    json_str='{"a":1,"b":2,"3":"c","4":["k","k1"]}'
#    d=json.JSONDecoder().decode(json_str)
#    print(type(d))
#    print(d)

# def read_data():
#     global books
#     with open('books.txt','r') as f:
#         print ("f.read:",f.read())
#         books = eval(f.read())
#         print ("books:",books)
# read_data()

#生成随机数，并补齐为两位的09格式
# lowbit=hex(random.randint(1,255))
# zerolowbit=str(lowbit)[2:].zfill(2).upper()
# print ("lowbit:",lowbit,"zerolowbit:",zerolowbit)

# def Tabuada():
#     for i in range(1,10):
#         for j in range(1,i + 1):
#             print("{} * {} = {:<4d}".format(j,i,j * i), end='')
#         print()
#
# Tabuada()

# print("**********第一题**********")
# price = float(input("请输入购买价格："))
# while price >= 50:
#     if price <= 100:
#         print("折扣10%,最终价格{}".format((price * 0.9)))
#         break
#     elif price > 100:
#         print("折扣20%,最终价格{}".format(price * 0.8))
#         break
# else:
#     print("无优惠")

#unix时间转化为日期
# timeStamp = '1582629889'
# timeArray = time.localtime(float(timeStamp))
# otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
# print (otherStyleTime)   # 2013--10--10 23:40:00

#地址码1和01转换，zfill(2)前面不够2位填0
# term_start=0xAA
# term_list=[]
# for i in range(20):
#     term_addr=term_start+i
#     term_hex=hex(term_addr)[2:] #转化为16进制后，0x1，只取后面的值，不要0x
#     term_list.append(str(term_hex).zfill(2).upper())    #a先转为0a，再转为大写0A
# print (term_list)

# #z字符串转化为字典,互相转化
# data4 = '{"name":"666677771112","devEui":null,"channelNumber":"666677771112","offline_times":30,"upLinkDeviceId":14001331,"upLinkDeviceType":15,"lorawanAppEui":null,"lorawanAppKey":null,"protocolType":1,"templateId":14146852,"connect_port":"RS485_4","term_addr":"2","protocol":"GW_PROTC_MODBUS"}'
# datadict=json.loads(data4)  #字符串转为字典
# print (datadict)
# data4str=json.dumps(data4)  #字典转为字符串

#模拟485发送
# ser = serial.Serial("com3", 9600,timeout=0.5)   # 选择串口，并设置波特率
# ser = serial.Serial( #下面这些参数根据情况修改
#   port='COM3',
#   baudrate=9600,
#   parity=serial.PARITY_ODD,
#   stopbits=serial.STOPBITS_TWO,
#   bytesize=serial.SEVENBITS
# )
# data = ''
# while ser.inWaiting() > 0:
#   data += ser.read(1)
# if data != '':
#   print (data)

# 获取一行信息
# def recv(serial):
#     print('2')
#     data = ''
#     while serial.inWaiting() > 0:
#         print(serial.inWaiting())
#         print('3')
#         # data += str(serial.read(15)) # ok 要配合timeout 使用, 否则要传入已知 的 size
#         # data += str(serial.readline())  # ok 要配合timeout 使用
#         # data += str(serial.readlines())  # ok 要配合timeout 使用
#         # data += str(serial.readall())     # ok 要配合timeout 使用
#         data += str(serial.read_all())    # ok 要配合timeout 使用
#
#         print("************************************")
#         #print(serial.read(13))
#         print('准备打印data')
#         # data = str(serial.read(19))
#         print(data)
#         print('data:%s'%data)
#         print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
#     return data
#
# while True:
#     print('1')
#     data = recv(ser)
#     print('4')
#     if data != '':
#         print('5')
#         print(data)
#         break
#
# ser.close()

# def calc_crc(string):
#     data = bytearray.fromhex(string)
#     #print ("fromhex:",data)
#     datahex=bytearray.hex(data)
#     #print("hex:", datahex)
#     crc = 0xFFFF
#     for pos in data:
#         crc ^= pos
#         for i in range(8):
#             if ((crc & 1) != 0):
#                 crc >>= 1
#                 crc ^= 0xA001
#             else:
#                 crc >>= 1
#     crcresult=hex(((crc & 0xff) << 8) + (crc >> 8))
#     #print (crcresult,len(crcresult))
#     if (len(crcresult)==6):
#         crcfirst=crcresult[2:4].zfill(2).upper()
#         crcsecond=crcresult[4:6].zfill(2).upper()
#     else:
#         crcfirst=crcresult[2:3].zfill(2).upper()
#         crcsecond=crcresult[3:5].zfill(2).upper()
#     crclist=[crcfirst,crcsecond]
#     return crclist
#
# #return s[4:6] + s[2:4] if invert == True else s[2:4] + s[4:6]
# print (calc_crc("01 03 04 00 1D 0F 87"))  #0x2fa7
# print (calc_crc("0E 03 04 00 1D 0F 87"))
# print (calc_crc("03 03 04 00 1D 0F 87"))

# frpname="21012C00003A.ssh_21012C00003A"
# sshname="ssh_21012C00003A"
# if (sshname in frpname):
#     print ("Yes")

# ticks=time.time()
# curtime=re.search('\w{10}',str(ticks))
# currenttime=curtime.group()
# print (ticks)
# localtime = time.localtime(time.time())
# print (localtime)
# #print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# getdatetime=time.strftime("%Y%m%d%H%M%S", time.localtime())
# print (getdatetime)

# authinfo="root@localhost's password: Authentication failed"
# if ('Authentication failed' in authinfo):
#     print ("failed")

# dict={}
# dict['ssh_1']=2101
# dict['ssh_2']=2201
# print (dict)
# #{'ssh_1': 2101, 'ssh_2': 2201}
# for k,v in dict.items():
#     print ("key:",k,"value:",v)

# #申通物流,6F,72,79,A5密码dywl123.com
# gwsn_shentong=['21012C00006E','21012C00006F','21012C000072','21012C000074','21012C000079','21012C000092','21012C0000A1','21012C0000A2','21012C0000A5']
# shentong_passwd='dywl123.com'   #申通ssh部分密码被改了
# #山林防火主配电箱
# gwsn_fanghuo=['21012C000010','21012C000025','21012C000030','21012C00006A','21012C00007A','21012C00007E','21012C000083','21012C000084','21012C000088','21012C00008A','21012C000090','21012C000093','21012C00009A']
# #上海数筑
# gwsn_shuzhu=['21012C00007B','21012C000096','21012C00009C','21012C00009F']
#
# all_gw=gwsn_shentong+gwsn_fanghuo+gwsn_shuzhu
# print (all_gw)

# value='线路电流1'
# devicedata='-200'
# if ('电流' in value):
#     print ("Include")
# else:
#     print ("Not")
# if (devicedata=='-200'):
#     print ("It is -200")
# if (float(devicedata)>80) or (float(devicedata)<-20):
#     print (">80")

# #字典双循环
# dict1={'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# for key,value in dict1.items():
#     print ("This is key：",key)
#     print("This is value：", value)

# #设备实时数据上报到csv格式
# outputcsv=[]
# csvindex=['编号','名称','账号','类型','在线','最后通讯时间','上报数据间隔','版本号','上行设备','实时数据1','实时数据2']
# outputcsv.append(csvindex)
# csvdata=['1111','1111名称','111账号','111类型','111在线','111最后通讯时间','111上报数据间隔','111版本号','111上行设备','111实时数据1','111实时数据2']
# outputcsv.append(csvdata)
# print ("outputcsv:",outputcsv)
# with open("testwrite.csv", "w") as csvwritefile:
#     writer = csv.writer(csvwritefile,lineterminator='\n')   #加上, lineterminator='\n'可以使csv写入中间没有多余空行
#     for i in range(2):
#         # 先写入columns_name
#         writer.writerow(outputcsv[i])
#         #writer.writerow(csvindex)
#         # 写入多行用writerows
#         # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])
#         #writer.writerow(csvdata)
#     csvwritefile.close()

#csv行数
# with open('Adddevice.csv') as f1:
# #    print(len(f1.readlines()))
#     numbers=len(f1.readlines())
#     print(numbers)
#     f1.close()
# #csv读取
# with open('Adddevice.csv') as f:
#     # 创建csv文件读取器
#     print(numbers)
#     reader = csv.reader(f)
#     for i in range(0,numbers):
#         # 读取第一行，这行是真正的数据。
#         first_row = next(reader)
# #    first111 = "['210000000B1C']"
#         devicesn = re.search('\w{12}',str(first_row))
#         device=devicesn.group()
#         print (device)

#csv_file=csv.reader(open('Adddevice.csv','r'))
#print (csv_file)
#for stu in csv_file:
#	print(stu)
#    restu = re.search('\w\w\w\w\w\w\w\w\w\w\w\w',first111)
#    aaa=restu.group()
#    print (aaa)



