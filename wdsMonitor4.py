# -*- coding: utf-8 -*-

import Wds
import time
import os

lsn_url = 'https://wds.modian.com/show_weidashang_pro/4559#1'
tlj_url = 'https://wds.modian.com/show_weidashang_pro/4558#1'
#group = 'BEJ48-刘胜男应援会'
group = '空'
interval = 30

def qqReport(msg, group):
    cmd = 'qq send group ' + group + ' ' + msg
    os.system(cmd)

lsnWds = Wds.Wds(lsn_url)
tljWds = Wds.Wds(tlj_url)

while True:
    time.sleep(interval)
    lsnWds.refreshInfo()
    tljWds.refreshInfo()
    if lsnWds.isChanged == False and tljWds.isChanged == False:
        continue
    msg = ''
    if lsnWds.isChanged:
        for user in lsnWds.addedUserInfo:
            msg = msg + user + ' 刚刚支持了小树' + lsnWds.addedUserInfo[user][3:] + '\n'
        msg += '感谢大家的支持！'
    if tljWds.isChanged:
        msg = msg + '莉佳集资刚刚增长了' + str(tljWds.addedAmount) + '元\n'
    msg += '【北广暗黑拯救战】唐莉佳x刘胜男联合企划正在进行中，目前比分小树'
    msg = msg + str(lsnWds.amount) + ':' + str(tljWds.amount) + '莉佳\n'
    if lsnWds.amount < tljWds.amount:
        msg += '暂时落后。'
    elif lsnWds.amount > tljWds.amount:
        msg += '暂时领先。'
    else:
        msg += '打平。'
    msg += '为了让小树远离凉茶的威胁，园丁们加油集资吧！微打赏链接：http://t.cn/RSjqqgc'
    qqReport(msg, group)