"""
Generate WireGuard tunnel configuration files from your data
"""

import json
import environ

env = environ.Env()
environ.Env.read_env()

# Load all IP addresses from the given file

IPS = []

with open(file='ip-list.json', mode='r', encoding='UTF-8') as file:
    lists = json.load(file)
    for group in lists:
        for ip in lists[group]:
            IPS.append(ip)

IPS = ", ".join(map(str, IPS))

# Load other config options from .env file

PrivateKey = env('PRIVATE_KEY')
PublicKey = env('PUBLIC_KEY')
Address = env('ADDRESS')
MTU = env('MTU')
PersistentKeepalive = env('PERSISTENT_KEEPALIVE')

# Generate the config file for each endpoint

with open(file='endpoints.json', mode='r', encoding='UTF-8') as file:
    endpoints = json.load(file)
    for endpoint in endpoints:
        with open(file=endpoint['name']+'.conf', mode='w', encoding='UTF-8') as file:
            file.write('[Interface]\n')
            file.write('PrivateKey = ' + PrivateKey + '\n')
            file.write('Address = ' + Address + '\n')
            file.write('MTU = ' + MTU + '\n\n')
            file.write('[Peer]\n')
            file.write('PublicKey = ' + PublicKey + '\n')
            file.write('AllowedIPs = ' + IPS + '\n')
            file.write('Endpoint = ' + endpoint['address'] + '\n')
            file.write('PersistentKeepalive = ' + PersistentKeepalive + '\n')
