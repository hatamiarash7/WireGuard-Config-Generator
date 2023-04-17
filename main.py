"""
Generate WireGuard tunnel configuration files from your data
"""

from typing import List
import environ
import toml

# Load environment variables from .env file
env = environ.Env()
environ.Env.read_env()


def get_ips() -> List[str]:
    """
    Load the list of IP addresses from the `ip-list.toml` file
    and return a list of unique IP addresses.

    Returns:
        A list of unique IP addresses.
    """
    with open('ip-list.toml', 'r', encoding='UTF-8') as ip_list:
        ips = []
        # Load IP addresses from TOML file
        lists = toml.load(ip_list)
        # Iterate over groups of IP addresses
        for section in lists:
            # Iterate over individual IP addresses
            for endpoint_ip in lists[section]:
                ips.extend([
                    value for value in lists[section][endpoint_ip].values()
                ])
        # Return a list of unique IP addresses
        return list(set(ips))


def generate_config(endpoint: str, address: str) -> None:
    """
    Generate a WireGuard configuration file for the specified endpoint.

    Args:
        endpoint: The endpoint's name.
        address: The endpoint's address.

    Returns:
        None
    """
    # Get the list of unique IP addresses
    ips = ", ".join(map(str, get_ips()))
    # Define the filename for the configuration file
    filename = endpoint + '.conf'
    # Get environment variables with default values
    address = env('ADDRESS', default='10.0.0.1/24')
    mtu = env('MTU', default='1420')
    keepalive = env('PERSISTENT_KEEPALIVE', default='25')
    # Write the configuration file
    with open(filename, 'w', encoding='UTF-8') as profile_file:
        # Write the [Interface] section
        profile_file.write("[Interface]\n")
        profile_file.write(f"PrivateKey = {env('PRIVATE_KEY')}\n")
        profile_file.write(f"Address = {address}\n")
        profile_file.write(f"MTU = {mtu}\n\n")
        # Write the [Peer] section
        profile_file.write("[Peer]\n")
        profile_file.write(f"PublicKey = {env('PUBLIC_KEY')}\n")
        profile_file.write(f"AllowedIPs = {ips}\n")
        profile_file.write(f"Endpoint = {address}\n")
        profile_file.write(f"PersistentKeepalive = {keepalive}\n")


def main():
    """The main function"""

    # Load endpoint data from TOML file
    with open('endpoints.toml', 'r', encoding='UTF-8') as endpoints_file:
        endpoints = toml.load(endpoints_file)
        # Generate a configuration file for each endpoint
        for endpoint in endpoints:
            generate_config(endpoint, endpoints[endpoint])


if __name__ == '__main__':
    main()
