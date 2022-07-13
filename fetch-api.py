"""
 Pick a random application pprogramming interface.
 Fetch the data from that A.P.I and log it into the console. 
 Display a error message if data is not found if the data is found display a success message.
 Allow the user to input specific infromation reguaring the data set.
"""
# Imported urllib request modle and json modle to request and .
import urllib.request, json

# Created a variable called url to grab the url infromation.
url = "https://randomuser.me/api/?results=1"

# Created a response varirable to request the url to be read in a string format.
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# Print the fetch rersponse and display the data for 1 result. 
print (data)