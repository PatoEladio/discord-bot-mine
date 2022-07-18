# Import
from python_aternos import Client

# Log in
aternos = Client.from_credentials('Funaland_2', 'deathnote1')

# Returns AternosServer list
servs = aternos.list_servers()

# Get the first server by the 0 index
myserv = servs[0]

print(myserv)

# Run server
myserv.start()
