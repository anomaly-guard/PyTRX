# PyTRX

[comment]: <> ([![PyPI version]&#40;https://badge.fury.io/py/tronpy.svg&#41;]&#40;https://pypi.org/project/tronpy/&#41;)

Easy to use Tron Client

[comment]: <> ([Documentation]&#40;https://tronpy.readthedocs.io/en/latest/index.html&#41;)

## Usage

```python
from pytrx import Tron
from pytrx.keys import PrivateKey

client = Tron(network="nile")
priv_key = PrivateKey(bytes.fromhex("8888888888888888888888888888888888888888888888888888888888888888"))

txn = (
    client.trx.transfer("TJzXt1sZautjqXnpjQT4xSCBHNSYgBkDr3", "TVjsyZ7fYF3qLF6BQgPmTEZy1xrNNyVAAA", 1_000)
    .memo("test memo")
    .build()
    .inspect()
    .sign(priv_key)
    .broadcast()
)

print(txn)
# > {'result': True, 'txid': '5182b96bc0d74f416d6ba8e22380e5920d8627f8fb5ef5a6a11d4df030459132'}
print(txn.wait())
# > {'id': '5182b96bc0d74f416d6ba8e22380e5920d8627f8fb5ef5a6a11d4df030459132', 'blockNumber': 6415370, 'blockTimeStamp': 1591951155000, 'contractResult': [''], 'receipt': {'net_usage': 283}}
```

### Goals
This project's codebase is a fork of [tronpy](https://github.com/andelf/tronpy).
Our goal is to provide easy to use Tron Client, but due to different approaches/goals and code structures
we decided to present a new package instead of remaining a fork.
Initial versions are too close to the main fork but as the project is developed
the deviation will be clear. 

Here is a general list of our goals:

- [ ] Easy To Use APIs built top of low-level APIs
- [ ] Tron Solidity integration and automatic contract compilation APIs

### Contribution
Contributions are welcome. If you're interested, [Contact me](mailto:connorholmes.0x05d@gmail.com) and we can 
have a talk about project and its goals. 