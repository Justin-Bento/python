"""
 Pick a random application pprogramming interface.
 Fetch the data from that A.P.I and log it into the console. 
 Display a error message if data is not found if the data is found display a success message.
 Allow the user to input specific infromation reguaring the data set.
"""
import requests

res = requests.get('https://randomuser.me/api')

if res.status_code == 200:
  print('Successful connection')
  print(res.json())
else:
  print('No connection')

