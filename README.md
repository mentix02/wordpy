# wordpy
A dictionary program for nix* terminals

## Installation

Simply use pip to install the latest stable version - 

```sh
$ pip install wordpy
```

## Usage

#### Getting API keys

This package wouldn't be possible without the existence of [Oxford Dictionaries](https://developer.oxforddictionaries.com). However, service hosting is costly and they must make some money themselves so they only let a simple, developer option for their prolix API. Register for it [here](https://developer.oxforddictionaries.com/signup?plan_ids[]=2357355869422). 

When you first use wordpy, you'll recieve a prompt to enter your recently acquired credentials and store it for future usage. Don't worry, everything remains on your local system.

The program is extremely simple - you literally just get the definition of a word in your terminal. Or the synonyms if you're feeling adventurous.

```sh
$ wordpy <word>
```

To get synonyms - 

```sh
$ wordpy -s <word>
```

#### Examples

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

## Development

#### Contributing

Make an issue if you stumble upon a bug. Any ideas or features you'd like to be added, once again, make an issue out of. 

To do something more simulating like writing code, just clone this repo, get it on your local system, make a branch, push it back to your master and finally, make a pull request.

I follow PEP-8 so you have to follow it too. Don't see why that's not already baked into the syntax.

#### Testing

To run tests, simply install nose - 

```sh
$ pip install nose
$ python setup.py test
```

I've never been a big fan of testing... let me rephrase, I've never been a big fan of writing tests myself but there's a handful of them in `tests/` that should succeed before you even think about committing. 

Any new feature should come with its own `test_<name_of_feature>.py` file in the said `tests/` directory and should be verbose with at least two cases.

#### Features To Add

- [x] Basic usage
- [x] Testing
- [ ] Optimization
- [ ] Documentation (?)
- [ ] Even more features
- - [ ] antonyms
- - [ ] etymologies
- - [ ] different definitions
