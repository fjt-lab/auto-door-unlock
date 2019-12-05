# coding: utf-8

import os
import datetime
from datetime import timedelta

#現在時刻の取得
def get_time():
    dt_now = datetime.datetime.now()
    sent = dt_now.strftime('%Y/%m/%d %H:%M:%S')
    return sent

#ログのリストを更新
def update_log(dat, usrid):
    for i in range(len(dat)):
        if dat[i][0] == usrid:   #登録されているユーザー
            if dat[i][1] == "1":    #入室フラグが立っているとき
                dat[i][1] = "0"
                dat[i][2] = ""
                dat[i][3] = get_time()
            else:                   #入室フラグが立っていないとき
                dat[i][1] = "1"
                dat[i][2] = get_time()
                dat[i][3] = ""

#ログファイルの確認・更新後にパスを返す
def check_log():
    #cwd = os.getcwd()
    cwd = os.path.dirname(os.path.realpath(__file__))
    cdir = cwd + "/"
    fname = "-logfile.txt"
    path = ""

    today = datetime.date.today()

    if today.weekday() != 0:
        someday = (today - timedelta(days = today.weekday()))
        sent = someday.strftime('%Y-%m-%d')
        path = cdir + sent + fname
    else:
        sent = today.strftime('%Y-%m-%d')
        path = cdir + sent + fname
        f = open(path, mode="a")
        f.close()
    return path

#今日の日付をファイルに書き込み
def s_write_log():
    f = open(check_log(), mode = "a")
    dt_now = datetime.datetime.now()
    sent = "   " + dt_now.strftime('%Y/%m/%d') + "\n"
    
    f.write(sent)
    f.close()

def write_log(dat, usrid):
    f = open(check_log(), mode = "a")
    logs = ""

    for j in range(len(dat)):
        if dat[j][0] == usrid:
            if dat[j][1] == "1":
                logs += "[ENTRY] "
            else :
                logs += "[EXIT ] "
            for i in range(2):
                if i == 0:
                    logs += dat[j][i]
                    logs += " "
                if i == 1:
                    if dat[j][i] == "1":
                        logs += dat[j][2]   #入室時間
                    else:
                        logs += dat[j][3]   #退室時間
    logs += "\n"

    f.write(logs)
    f.close()

if __name__ == "__main__":
    check_log()
