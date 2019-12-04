# coding: utf-8

import os
import binascii
import nfc
import sys

import time
import schedule
import threading

from card_hash import sha512
from authenticated_cards import authenticated_cards

import add_log
import servo

def startup(targets):
    return targets

def init():
    dat = []
    vals = authenticated_cards.keys()
    for i in range(len(vals)):
        usr = []
        usr.append(vals[i])
        for j in range(3):
            if j == 0:
                usr.append("0")
            else :
                usr.append("")
        dat.append(usr)
    return dat

def get_val(datalist, val):
    for i in range(len(datalist)):
        if val in datalist[i]:
            return datalist[i]
    return ""

def get_key(dic, val):
    key = [k for k, v in dic.items() if v == val]
    return key[0]

def connected(tag):
    # 製造ID (IDm)
    idm = binascii.hexlify(tag.identifier).upper()
    # 製造パラメータ (PMm)
    pmm = binascii.hexlify(tag.pmm).upper()
    # システムコード (sys)
    syscode = "%04X" % tag.sys

    card_hash = sha512(idm, pmm, syscode)
    card_list = authenticated_cards.values()
    card_val = get_val(card_list, card_hash)

    if card_val != "":
        servo.servo_con()
        usrid = get_key(authenticated_cards, card_val) 
        add_log.update_log(dat, usrid)
        add_log.write_log(dat, usrid)
        return True
    
    return False

def reset_log(dat):
    for i in range(len(dat)):
        if dat[i][1] == "1":    #入室フラグが立っているとき
            dat[i][1] = "0"
            dat[i][2] = ""
            dat[i][3] = "_SYSTEM_EXIT_"
            add_log.write_log(dat, dat[i][0])

def main_thread():
    clf = nfc.ContactlessFrontend('usb')    
    while clf.connect(rdwr={
        'on-startup': startup,
        'on-connect': connected,}):
        pass
    
def sub_thread():
    schedule.every().day.at("20:00").do(reset_log, dat)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    dat = init()
    
    thread_1 = threading.Thread(target=main_thread)
    thread_2 = threading.Thread(target=sub_thread)
    thread_1.start()
    thread_2.start()
