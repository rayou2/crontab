## Importing packages
import pandas as pd
import requests
import os
import sys
import time

## Pulling data from API
df = pd.read_json('https://health.data.ny.gov/resource/xdss-u53e.json')
df

## Saving data locally
df.to_csv('data/covid19.csv', index=None)

## Getting the time on the system
currentTime = time.time()
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(currentTime))
print('The current time is: ', listTime)

## Getting the current working directory
cwd = os.getcwd()
print(cwd)

## Creating a ile in the current working directory
with open(cwd + '/assignment6_' + nowStr + '.txt', 'w') as f:
    f.write(str(df))