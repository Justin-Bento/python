"""
 Pick a random application pprogramming interface.
 Fetch the data from that A.P.I and log it into the console. 
 Display a error message if data is not found if the data is found display a success message.
 Allow the user to input specific infromation reguaring the data set.
"""
import requests
import time

url = f'https://randomuser.me/api'
res = requests.get(url)

print(' ')

if res.status_code == 200:
  time.sleep(0.600)
  print('Successful connection')
  time.sleep(0.600)
  print(' ')
  print(res.json())
else:
  print('No connection')

print(' ')

class user:
  first_name = res.json()['results'][0]['name']['first']
  last_name = res.json()['results'][0]['name']['last']
  age = res.json()['results'][0]['dob']['age']
  gender = res.json()['results'][0]['gender']

print(f'Hi. My name is {user.first_name} {user.last_name}, and I am {user.age} years old {user.gender}.')

print(' ')