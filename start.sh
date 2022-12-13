#!/bin/bash
isrun=$(ps -ef | grep switch-cron | grep -v grep | wc -l)
if [ $isrun == 0 ];then
    nohup /home/project/switch-cron/venv/bin/python /home/project/switch-cron/app.py >/dev/null 2>&1 &
fi