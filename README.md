# netexpand
> Expands networks given in CIDR, dashed, or splat format.

[![PyPI Version](https://img.shields.io/pypi/v/netexpand.svg)](https://pypi.org/project/netexpand/)
[![Python Versions](https://img.shields.io/pypi/pyversions/netexpand.svg)](https://pypi.org/project/netexpand/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/sjtrotter/netexpand/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/sjtrotter/netexpand.svg)](https://github.com/sjtrotter/netexpand/issues)
[![Code Size](https://img.shields.io/github/languages/code-size/sjtrotter/netexpand.svg)](https://github.com/sjtrotter/netexpand)

`netexpand` takes a given network (which can be notated with CIDR, dashed, or splat format) and expands the network; i.e., it prints each valid address within the network given.

**Supported Notations:**
* **CIDR:** `x.x.x.x/x` (e.g., `192.168.1.0/24`)
* **Dashed:** `x.x.x.x-x` (e.g., `192.168.1.1-254`)
* **Splat:** `x.x.x.*`   (e.g., `192.168.1.*`)

*NOTE: Network notations should not be mixed; the program will report an error and exit upon detection.*

By default, the tool prints each valid host address to stdout. It also includes options to randomize the output addresses and to select specific network components (like network addresses or broadcast addresses).

## Installation

Requires a current Python 3.7+ installation with standard libraries. 

**Install from PyPI (Recommended):**
```bash
pip install netexpand
```

**Install from Source:**
```bash
git clone [https://github.com/sjtrotter/netexpand.git](https://github.com/sjtrotter/netexpand.git)
cd netexpand
pip install .
```

## Usage Example

Once installed, you can call `netexpand` natively from anywhere in your terminal.

**Standard Host Expansion (Default):**
```bash
$ netexpand 192.168.1.0/30
192.168.1.1
192.168.1.2
```

**Randomized Output:**
```bash
$ netexpand 192.168.1.10-15 -r
192.168.1.14
192.168.1.11
192.168.1.15
192.168.1.10
192.168.1.12
192.168.1.13
```

**Output Specific Network Components:**
You can specify whether you want to output `hosts`, `networks`, or `broadcast` addresses using the `-t` or `--type` flag.
```bash
$ netexpand 10.0.0.* -t broadcast
10.0.0.255
```

## Development Setup

To work on `netexpand` locally without needing to reinstall after every change, install the package in "editable" mode:

```bash
git clone [https://github.com/sjtrotter/netexpand.git](https://github.com/sjtrotter/netexpand.git)
cd netexpand
pip install -e .
```

## Meta

Stephen Trotter – stephen@trotter.cloud

Distributed under the GNU GPLv3 license. See `LICENSE` for more information.

[https://github.com/sjtrotter/netexpand](https://github.com/sjtrotter/netexpand)

## Contributing

1. Fork it (<https://github.com/sjtrotter/netexpand/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request