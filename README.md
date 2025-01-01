# Kupi.cz prices parser

This is an asynchronous library for getting prices for items on [kupi.cz](https://kupi.cz).

This library is in beta testing. It means that critical errors and security issues may occur during operation, which may be fixed in the next updates.


## Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. virtualenv is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With virtualenv, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

### Mac/Linux

```
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install git+https://github.com/prostmich/pykupi.git
```

### Windows

```
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install git+https://github.com/prostmich/pykupi.git
```

## Supported Python Versions

Python 3.9 is fully supported. This library may work on later versions of 3, but I do not currently run tests against those versions.

## Example
Getting information about offers for bananas over 15 CZK per kilo.

```Python
import asyncio
from pykupi import KupiParser

async def task():
    parser = KupiParser()
    result = await parser.get_prices("banany", min_price=15)
    cheapest = result.offers[0]
    print(
        f'The cheapest bananas now in {cheapest.offered_by} for {cheapest.price} {cheapest.price_currency} '
        f'until {cheapest.valid_until.strftime("%d.%m.%Y")}'
    )
    # The cheapest bananas now in Kaufland for 24.9 CZK until 08.03.2022
    await parser.session.close()


asyncio.run(task())
```

## Third Party Libraries and Dependencies

The following libraries will be installed when you install the client library:
* [aiohttp](https://github.com/aio-libs/aiohttp)
* [pydantic](https://github.com/samuelcolvin/pydantic)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Contributing
For technical issues particular to this module, please [report the issue](https://github.com/prostmich/pykupi/issues) on this GitHub repository.

New features, as well as bug fixes, by sending a pull request is always welcomed.

