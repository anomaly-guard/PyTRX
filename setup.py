# -*- coding: utf-8 -*-
from setuptools import setup

packages = ['pytrx', 'pytrx.keys', 'pytrx.providers']

package_data = {'': ['*']}

install_requires = [
    'base58>=2.0.0,<3.0.0',
    'ecdsa>=0.15,<0.16',
    'eth_abi>=2.1.1,<3.0.0',
    'pycryptodome>=3.9.7,<4.0.0',
    'requests>=2.23.0,<3.0.0',
    'httpx==0.16.1',
]

setup_kwargs = {
    'name': 'pytrx',
    'version': '0.1.0',
    'description': 'Easy to use Tron Client',
    'long_description': '# PyTRX\n\nEasy to use Tron Client',
    'author': 'Connor Holmes',
    'author_email': 'connorholmes.0x05d@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Connor-Holmes/PyTRX',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
