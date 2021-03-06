[![GitHub Release][releases-shield]][releases]
[![PyPI][pypi-releases-shield]][pypi-releases]
[![PyPI - Downloads][pypi-downloads]][pypi-statistics]
[![Buy me a coffee][buy-me-a-coffee-shield]][buy-me-a-coffee]

# brother
Python wrapper for getting data from Brother laser and inkjet printers via snmp

## How to use package
```py
import asyncio

from brother import Brother, SnmpError, UnsupportedModel

# printer IP address/hostname
HOST = "192.172.10.12"


async def main():
    # argument kind: laser - for laser printer
    #                ink   - for inkjet printer
    brother = Brother(HOST, kind="laser")
    try:
        await brother.async_update()
    except (ConnectionError, SnmpError, UnsupportedModel) as error:
        print(f"{error}")
        return

    if brother.available:
        print(f"Data available: {brother.available}")
        print(f"Model: {brother.model}")
        print(f"Firmware: {brother.firmware}")
        print(f"Status: {brother.data['status']}")
        print(f"Serial no: {brother.serial}")
        print(f"Sensors data: {brother.data}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```
[releases]: https://github.com/bieniu/brother/releases
[releases-shield]: https://img.shields.io/github/release/bieniu/brother.svg?style=popout
[pypi-releases]: https://pypi.org/project/brother/
[pypi-statistics]: https://pypistats.org/packages/brother
[pypi-releases-shield]: https://img.shields.io/pypi/v/brother
[pypi-downloads]: https://img.shields.io/pypi/dm/brother
[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/QnLdxeaqO
