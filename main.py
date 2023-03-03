"""
Generate WireGuard tunnel configuration files from your data
"""

import json
import environ
from typing import List

# Load environment variables from .env file
env = environ.Env()
environ.Env.read_env()


def get_ips() -> List[str]:
    """
    Load the list of IP addresses from the `ip-list.json` file and return a list of unique IP addresses.

    Returns:
        A list of unique IP addresses.
    """
    with open('ip-list.json', 'r', encoding='UTF-8') as f:
        ips = []
        # Load IP addresses from JSON file
        lists = json.load(f)
        # Iterate over groups of IP addresses
        for group in lists:
            # Iterate over individual IP addresses
            for ip in lists[group]:
                ips.append(ip)
        # Return a list of unique IP addresses
        return list(set(ips))


def generate_config(endpoint: dict) -> None:
    """
    Generate a WireGuard configuration file for the specified endpoint.

    Args:
        endpoint: A dictionary containing the endpoint name and address.

    Returns:
        None
    """
    # Get the list of unique IP addresses
    ips = ", ".join(map(str, get_ips()))
    # Define the filename for the configuration file
    filename = endpoint['name'] + '.conf'
    # Get environment variables with default values
    address = env('ADDRESS', default='10.0.0.1/24')
    mtu = env('MTU', default='1420')
    persistent_keepalive = env('PERSISTENT_KEEPALIVE', default='25')
    # Write the configuration file
    with open(filename, 'w', encoding='UTF-8') as f:
        # Write the [Interface] section
        f.write('[Interface]\n')
        f.write('PrivateKey = {}\n'.format(env('PRIVATE_KEY')))
        f.write('Address = {}\n'.format(address))
        f.write('MTU = {}\n\n'.format(mtu))
        # Write the [Peer] section
        f.write('[Peer]\n')
        f.write('PublicKey = {}\n'.format(env('PUBLIC_KEY')))
        f.write('AllowedIPs = {}\n'.format(ips))
        f.write('Endpoint = {}\n'.format(endpoint['address']))
        f.write('PersistentKeepalive = {}\n'.format(persistent_keepalive))


# Load endpoint data from JSON file
with open('endpoints.json', 'r', encoding='UTF-8') as f:
    endpoints = json.load(f)
    # Generate a configuration file for each endpoint
    for endpoint in endpoints:
        generate_config(endpoint)
