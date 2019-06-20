#!/bin/bash

# systemctlでプロセス管理用

cat >/dev/null <<EOS

Usge:

  # 起動と停止
  sudo systemctl start cardauth
  sudo systemctl stop cardauth
  
  # 状態確認
  systemctl status cardauth

EOS

/usr/bin/python2 /home/pi/automatic_door_unlocking/card_auth.py

