# wordpy
A dictionary program for nix* terminals

## Installation

Simply use pip to install the latest stable version - 

```sh
$ pip install wordpy
```

## Usage

### Getting API keys

This package wouldn't be possible without the existence of [Oxford Dictionaries](https://developer.oxforddictionaries.com). However, service hosting is costly and they must make some money themselves so they only let a simple, developer option for their prolix API. Register for it [here](https://developer.oxforddictionaries.com/signup?plan_ids[]=2357355869422). 

When you first use wordpy, you'll recieve a prompt to enter your recently acquired credentials and store it for future usage. Don't worry, everything remains on your local system.

The program is extremely simple - you literally just get the definition of a word in your terminal. Or the synonyms, antonyms or even the origin i.e. etymology of the word if you're feeling adventurous.

### Flags

|       Flag      |       Usage       |
|:---------------:|:-----------------:|
|  -s, --synonyms |  display synonyms |
|  -a, --antonyms |  display antonyms |
| -e, --etymology |   show etymology  |
|  -v, --version  |  display version  |
|    -h, --help   | show help message |

### Commands

```sh
$ wordpy <word>
```

To get synonyms - 

```sh
$ wordpy -s <word>
```

Antonyms can be derived by - 

```sh
$ wordpy -a <word>
```

And finally, etymology - 

```sh
$ wordpy -e <word>
```

These flags can be combined to get whatever the user asks for. For example to get the definition, antonyms and the etymology, you can use - 

```sh
$ wordpy -ae <word>
```

### Examples

```sh
$ wordpy apple
[s] Apple (noun)
The round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh.
```

```sh
$ wordpy -s car # synonyms
[s] Car (noun)
A road vehicle, typically with four wheels, powered by an internal combustion engine and able to carry a small number of people
[s] Synonyms
auto, automobile, bus, convertible, jeep, limousine, machine, motor, pickup, ride, station wagon, truck, van, wagon, bucket, buggy, compact, conveyance, coupe, hardtop, hatchback, heap, jalopy, junker, motorcar, roadster, sedan, subcompact, wheels, wreck, clunker, gas guzzler, touring car
```

```sh
$ wordpy -as happy # antonyms and synonyms
[s] Happy (adjective)
Feeling or showing pleasure or contentment
[s] Synonyms
cheerful, contented, delighted, ecstatic, elated, glad, joyful, joyous, jubilant, lively, merry, overjoyed, peaceful, pleasant, pleased, thrilled, upbeat, blessed, blest, blissful, blithe, can't complain, captivated, chipper, chirpy, content, convivial, exultant, flying high, gay, gleeful, gratified, intoxicated, jolly, laughing, light, looking good, mirthful, on cloud nine, peppy, perky, playful, sparkling, sunny, tickled, tickled pink, up, walking on air
[s] Antonyms
depressed, disappointed, disturbed, down, grave, melancholy, miserable, sad, serious, sorrowful, troubled, unfriendly, unhappy, upset, discouraged, dissatisfied, forsaken, hopeless, morose, pained, unfortunate, unlucky
```

```sh
$ wordpy -e computer
[s] Computer (noun)
An electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program.
[s] Etymology
1640s, "one who calculates," agent noun from compute (v.). Meaning "calculating machine" (of any type) is from 1897; in modern use, "programmable digital electronic computer" (1945 under this name; theoretical from 1937, as Turing machine). ENIAC (1946) usually is considered the first. Computer literacy is recorded from 1970; an attempt to establish computerate (adjective, on model of literate) in this sense in the early 1980s didn't catch on. Computerese "the jargon of programmers" is from 1960, as are computerize and computerization.
```

## Development

### Contributing

Make an issue if you stumble upon a bug. Any ideas or features you'd like to be added, once again, make an issue out of. 

To do something more simulating like writing code, just clone this repo, get it on your local system, make a branch, push it back to your master and finally, make a pull request.

I follow PEP-8 so you have to follow it too. Don't see why that's not already baked into the syntax.

### Testing

To run tests, simply install nose - 

```sh
$ pip install nose
$ python setup.py test
```

or run `nosetests` for a cleaner output - 

```sh
$ nosetests
```

I've never been a big fan of testing... let me rephrase, I've never been a big fan of writing tests myself but there's a handful of them in `tests/` that should succeed before you even think about committing. 

Any new feature should come with its own `test_<name_of_feature>.py` file in the said `tests/` directory and should be verbose with at least two cases.

### Features To Add

- [x] Basic usage
- [x] Testing
- [ ] Optimization
- [ ] Documentation (?)
- [ ] Even more features
- - [x] antonyms
- - [x] etymologies
- - [ ] different definitions
