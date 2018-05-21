#!/usr/bin/env bash

HOME_START_POINT=/home/midmih/Documents/django_projects/workbook/src
LOGS_START_POINT=${HOME_START_POINT}/myapps/crypto/cron/run.log
VENV_START_POINT=/home/midmih/Documents/django_projects/venv/wb/bin/activate

echo "$(date "+%m%d%Y %H:%M:%S") :0" >> ${LOGS_START_POINT} 2>&1

cd ${HOME_START_POINT}

source ${VENV_START_POINT}
python manage.py update
python manage.py calculate
python manage.py notify
deactivate

echo "$(date "+%m%d%Y %H:%M:%S") :1" >> ${LOGS_START_POINT} 2>&1