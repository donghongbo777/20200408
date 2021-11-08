# coding=utf-8
import json
import csv
import time
import re
import requests
import os
import emailexample

url="http://iot.lnxall.com"     #生产
username="jiguanju"
password="jgj123456"
#排除的设备
nopowerdev=['218812000043_26']

#得到当前时间ticks
ticks=time.time()
curtime=re.search('\w{10}',str(ticks))
currenttime=curtime.group()

#设备离线上报到csv格式
outputcsv=[]
csvindex=['设备名称','设备SN','在线状态','最后通讯时间']
outputcsv.append(csvindex)
csvdata=[]

#得到当前时间ticks
ticks=time.time()
curtime=re.search('\w{10}',str(ticks))
currenttime=curtime.group()
#生成文件名
getdatetime=time.strftime("%Y%m%d%H%M%S", time.localtime())
randomname="gwoffline"+getdatetime+".csv"
currentpwd=os.getcwd()
logdir=currentpwd+"\log"
filename=logdir+'\\'+randomname
print (filename,getdatetime)

msglist=[]
def devops(sendmsg):    #机管局机器人
    headers = {'Content-Type': 'application/json',}
    params = (('key', 'acb620de-ddd0-4128-b79a-33ae814f2659'),)
    data = '{"msgtype": "text","text": {"content": "'+sendmsg+'"}}'
    response = requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send', headers=headers, params=params,data=data)

with open(filename, "w") as csvwritefile:
    writer = csv.writer(csvwritefile, lineterminator='\n')  # 加上, lineterminator='\n'可以使csv写入中间没有多余空行
    writer.writerow(csvindex)
    #1、------------------得到用户登录token
    cookies1 = {'p_h5_u': '0B1AAE8D-57E7-4D9F-9900-44B5636B68A7','UM_distinctid': '17b56fbe6573d6-0ebc08ef0cad3c-3373266-1fa400-17b56fbe658c91',}
    headers1 = {'Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8','Origin': 'http://iot.lnxall.com','Referer': 'http://iot.lnxall.com/login',}
    data1 = '{"username":"'+username+'","password":"'+password+'"}'
    response1 = requests.post('%s/iot/system/user/login' % url,headers=headers1,cookies=cookies1, data=data1,verify=False)
    tokenjson=json.loads(response1.text)     #将字符串转为dict输出，反正dumps可以将dict转为str输出
    admintokenhead=tokenjson['data']['tokenHead']
    admintoken=tokenjson['data']['token']
    userauth = admintokenhead + admintoken
    #2、得到该用户的设备列表
    cookies2 = {'p_h5_u': '0B1AAE8D-57E7-4D9F-9900-44B5636B68A7','UM_distinctid': '17b56fbe6573d6-0ebc08ef0cad3c-3373266-1fa400-17b56fbe658c91',
        'loginToken': 'WOOKONGeyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0aWFuaGVfd2FuZyIsImNyZWF0ZWQiOjE2MzE5NDk5Mzk2MTMsImV4cCI6MTYzMTk4NTkzOSwidGlkIjoiVmJmcU1PY1kifQ.un97G6JN6EYzduCjByhuoK3guhm4nvIcqAr_LB2lw-QxIN8EwpW67iuVMBUhfC5zGK86_-iHb2odeZ1v2bneKA',
        'gateway_local_env': 'single','tenantId': 'VbfqMOcY',}
    headers2 = {'Connection': 'keep-alive','Accept': 'application/json, text/plain, */*',
        'Authorization': 'WOOKONGeyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0aWFuaGVfd2FuZyIsImNyZWF0ZWQiOjE2MzE5NDk5Mzk2MTMsImV4cCI6MTYzMTk4NTkzOSwidGlkIjoiVmJmcU1PY1kifQ.un97G6JN6EYzduCjByhuoK3guhm4nvIcqAr_LB2lw-QxIN8EwpW67iuVMBUhfC5zGK86_-iHb2odeZ1v2bneKA',
        'Accept-Language': 'zh-CN','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'Referer': 'http://iot.lnxall.com/devmgr/device',}
    headers2['Authorization'] = userauth
    params2 = (('page', '1'),('size', '200'),('isDev', '1'),('type', '0,1'),('upLinkDeviceId', ''),)
    response2 = requests.get('%s/iot/device/findPageList' % url, headers=headers2, params=params2,cookies=cookies2, verify=False)
    devinfo=json.loads(response2.text)
    devcount=devinfo['pagination']['totalCount']
    devlist=devinfo['data']

    if devcount != 0:  # 没有设备情况跳出
        for devnumber in range(devcount):
            devchannelnumber=devinfo['data'][devnumber]['channelNumber']
            if (devchannelnumber in nopowerdev) or ('218878FF' in devchannelnumber):
                continue
            else:
                devname = devinfo['data'][devnumber]['name']
                devstatus=devinfo['data'][devnumber]['status']
                devlastConnectTime = devinfo['data'][devnumber]['lastConnectTime']
                csvdata.append(devinfo['data'][devnumber]['name'])  # 第一列，网关名称
                csvdata.append(devchannelnumber + '\t')   # 第二列，网关SN
                online_status = '在线'
                if devstatus == 1: online_status = '在线'
                elif devstatus == 0: online_status = '离线'
                else: online_status = '新增'
                csvdata.append(online_status)  # 第三列，网关在线状态

                if devlastConnectTime != None:
                    lastime = re.search('\w{10}', str(devlastConnectTime)).group()
                    if (int(currenttime)-int(lastime)>14400):
                        sendmsg='--------Jiguanju device offline:    '+devchannelnumber+'    '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(lastime)))
                        msglist.append(sendmsg)
                    timeArray = time.localtime(float(lastime))
                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    csvdata.append(otherStyleTime)  # 第四列，网关最后心跳
                else:
                    csvdata.append("Null")  # 第四列，网关最后心跳

            if (len(csvdata)!=0):
                writer.writerow(csvdata)
            csvdata=[]  #添加后，清空进行下一次
            time.sleep(0.1)

csvwritefile.close()

if (len(msglist)!= 0):  # msglist一次性发，免得邮件或消息太多
    msgstrtotal=''
    for msgitem in msglist:
        msgstrtotal = msgstrtotal+' ' + msgitem
    #print("msgstrtotal",msgstrtotal)
    emailexample.sendemail('Monitor lora device offline report', msgstrtotal, 'hongbo.dong@lnxall.com')
    emailexample.sendemail('Monitor lora device offline report',msgstrtotal,'wudachen@shdatabuilding.com')
    devops(msgstrtotal)