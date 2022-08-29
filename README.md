# Developing Nautobot Plugins Blog Series

This code is for the Developing Nautobot Plugins [blog series](https://blog.networktocode.com/post/developing-nautobot-plugins-1/). Before using this code, you will need to install Python and [Python Poetry](https://python-poetry.org/). Once the pre-requisites have been installed, clone the repository and checkout the tagged commit for whichever article you are one:

```shell
$ git clone https://github.com/networktocode-llc/nautobot-plugin-tutorial
$ git checkout part1
```

Once the code is cloned and checked out, simply start the development environment:

```shell
$ poetry shell
$ poetry install
$ invoke build debug
```
