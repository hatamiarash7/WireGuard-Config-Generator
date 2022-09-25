import environ
import json

env = environ.Env()
environ.Env.read_env()

# Load all IP addresses from the given file

finalIps = []

with open('ip-list.json', 'r') as file:
    lists = json.load(file)
    for list in lists:
        for ip in lists[list]:
            finalIps.append(ip)

finalIps = ", ".join(map(str, finalIps))

# Load other config options from .env file

PrivateKey = env('PRIVATE_KEY')
PublicKey = env('PUBLIC_KEY')
Address = env('ADDRESS')
MTU = env('MTU')
PersistentKeepalive = env('PERSISTENT_KEEPALIVE')

# Generate the config file for each endpoint

with open('endpoints.json', 'r') as file:
    endpoints = json.load(file)
    for endpoint in endpoints:
        with open(endpoint['name']+'.conf', 'w') as file:
            file.write('[Interface]\n')
            file.write('PrivateKey = ' + PrivateKey + '\n')
            file.write('Address = ' + Address + '\n')
            file.write('MTU = ' + MTU + '\n\n')
            file.write('[Peer]\n')
            file.write('PublicKey = ' + PublicKey + '\n')
            file.write('AllowedIPs = ' + finalIps + '\n')
            file.write('Endpoint = ' + endpoint['address'] + '\n')
            file.write('PersistentKeepalive = ' + PersistentKeepalive + '\n')
