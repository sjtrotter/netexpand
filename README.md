# netexpand
> Expands networks given in CIDR, dashed, or splat format.

netexpand takes a given network (which can be notated with CIDR or in a dashed format), and expands the network; i.e. it prints each valid address within the network given.

CIDR:   x.x.x.x/x

dashed: x.x.x.x-x

splat:  x.x.x.\*

NOTE: Network notations should not be mixed; program reports error and exits on detection.

Default behaivor prints each valid address to stdout. Also includes an option to randomize the output addresses.

![screenshot?]()

## Installation

Nothing extra required other than a current Python3 installation with standard libraries installed. Utilizes sys module and argparse module.

## Usage example

(will be built when completed)

## Development setup

Same as install, nothing special here. Just beed a working Python3 install, with sys and argparse modules.

## Release History

* 0.0.0
    * Working on README, LICENSE, and deciding on best commandline argument parser for python.

## Meta

Stephen Trotter – stephen.j.trotter@gmail.com

Distributed under the GNU GPLv3 license. See ``LICENSE`` for more information.

[https://github.com/sjtrotter/netexpand](https://github.com/sjtrotter/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[wiki]: https://github.com/sjtrotter/netexpand/wiki

