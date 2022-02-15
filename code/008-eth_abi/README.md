# Decoding with `eth-abi` and extra unconsumed data

In this directory you'll find an example where we use `eth-abi` to decode a
tuple, but the data we provide includes extra padding that the decoding won't
need.

Running:

```sh
poetry install
poetry run python main.py
```
