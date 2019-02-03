# wordpy
A dictionary program for nix* terminals

## Installation

Simply use pip to install the latest stable version - 

```sh
$ pip install wordpy
```

## Usage

The program is extremly simple - you literally just get the definiton of a word in your terminal. Or the synonyms if you're feeling adventurous.

```sh
$ wordpy <word>
```

To get synonyms - 

```sh
$ wordpy -s <word>
```

### Examples

```sh
$ wordpy apple
[s] Apple (noun)
The round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh.
```

```sh
$ wordpy -s car 
[s] Car (noun)
A road vehicle, typically with four wheels, powered by an internal combustion engine and able to carry a small number of people
[s] Synonyms
auto, automobile, bus, convertible, jeep, limousine, machine, motor, pickup, ride, station wagon, truck, van, wagon, bucket, buggy, compact, conveyance, coupe, hardtop, hatchback, heap, jalopy, junker, motorcar, roadster, sedan, subcompact, wheels, wreck, clunker, gas guzzler, touring car

```
