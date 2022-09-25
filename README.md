# WireGuard config generator

This script will generate tunnel config files for WireGuard.

## How to use

You need to give two file contains your information:

- `endpoints.json` : Contains the endpoints you want to connect to ( Name, Address ).
- `ip-list.json` : Contains the IP addresses you want to use.

And also give private/other information as a `.env` file.

### endpoints.json

```json
[
  {
    "name": "Company-Server-1",
    "address": "wg-1.domain.xyz:1234"
  },
  {
    "name": "Company-Server-2",
    "address": "wg-2.domain.xyz:1234"
  }
]
```

### ip-list.json

```json
{
  "k8s-cluster": [
    "1.2.3.4/32", 
    "5.6.7.8.9/32", 
    "1.2.3.4/27"
  ],
  "grafana": [
    "1.2.3.4/32", 
    "5.6.7.8.9/32", 
    "1.2.3.4/27"
  ],
  "other": [
    "1.2.3.4/32", 
    "5.6.7.8.9/32", 
    "1.2.3.4/27"
  ]
}
```

> **Note**: Array keys ( `grafana`, `other`, etc ) are not important and can be used to group IP addresses for you to read/edit better.

### .env

```env
PRIVATE_KEY=
PUBLIC_KEY=
ADDRESS=
MTU=
PERSISTENT_KEEPALIVE=
```

> **Note**: If you need extra data than the above, you should add your variables in `main.py` too.

## Run

To generate config files for all endpoints, run:

```bash
python main.py
```

This script will create file(s) based on the given endpoints. In this example, it will create `Company-Server-1.conf` and `Company-Server-2.conf` files like this:

```ini
[Interface]
PrivateKey = <PRIVATE_KEY>
Address = <ADDRESS>
MTU = <MTU>

[Peer]
PublicKey = <PUBLIC_KEY>
Endpoint = wg-1.domain.xyz:1234
AllowedIPs = 1.2.3.4/32, 5.6.7.8/32, ...
PersistentKeepalive = <PERSISTENT_KEEPALIVE>
```

---

## Support 💛

[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/bc1qmmh6vt366yzjt3grjxjjqynrrxs3frun8gnxrz)](https://en.cryptobadges.io/donate/bc1qmmh6vt366yzjt3grjxjjqynrrxs3frun8gnxrz) [![Donate with Ethereum](https://en.cryptobadges.io/badge/micro/0x0831bD72Ea8904B38Be9D6185Da2f930d6078094)](https://en.cryptobadges.io/donate/0x0831bD72Ea8904B38Be9D6185Da2f930d6078094)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/D1D1WGU9)

<div><a href="https://payping.ir/@hatamiarash7"><img src="https://cdn.payping.ir/statics/Payping-logo/Trust/blue.svg" height="128" width="128"></a></div>

## Contributing 🤝

Don't be shy and reach out to us if you want to contribute 😉

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Issues

Each project may have many problems. Contributing to the better development of this project by reporting them. 👍
