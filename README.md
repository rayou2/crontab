# Crontab

Crontab with Python deploy on VM

We used GCP to test automation in the python file for cron jobs

For once a day:

'0 0 * * */usr/bin/python3 /home/ramon_you/crontab/app.py'

Sunday at 10 pm: 

'00 22 * * 7/usr/bin/python3 /home/ramon_you/crontab/app.py'

End fo quarter:

'59 23 31 3,12 */usr/bin/python3 /home/ramon_you/crontab/app.py' 
'59 23 30 6,9 */usr/bin/python3 /home/ramon_you/crontab/app.py'
