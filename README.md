# DiscordBot
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## Contributors
Hyunwoo Kim - [Github: hyunwoo312](https://github.com/hyunwoo312) & Discord: hy#1999

Ryan Perry - [Github: RPerry57](https://github.com/RPerry57) & Discord: Perry#0057

Matthew Li - [Github: officialmattli](https://github.com/officialmattli) & Discord: bigmatt#5217

Andy Huang - [Github: Andy051](https://github.com/Andy051) & Discord: Azurnity#3835

Devin Huang - [Github: huandevi](https://github.com/huandevi) & Discord: crown jewel#9588

## Set up this repository

1. You will first have to install [poetry](https://python-poetry.org/docs/) and [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

```
# install poetry and venv in your system
$ python3 -m pip install poetry, virtualenv
```

2. Clone this repository into your desired workspace

3. Navigate to the cloned repository

```
$ cd /path/to/your/cloned/repository/DiscordBot
```

e.g. `cd /home/hyunwoo312/docs/DiscordBot`

4. Create your virtual environment

```
$ python3 -m venv .venv
```

5. Activate your virtual environment

```
# initialize your virtual environment (Unix/Linux)
$ source .venv/bin/activate
# initialize your virtual environment (Windows)
$ python -m venv .\env\Scripts\activate
```

6. Install dependencies

```
# install all the dependencies
$ poetry install
```


## How to run the App
1. Initialize your virtual environment that you set up

```
# initialize your virtual environment (Unix/Linux)
$ source .venv/bin/activate
# initialize your virtual environment (Windows)
$ python -m venv .\env\Scripts\activate
```

2. Install dependencies (skip if you already did)

```
# install all the dependencies
$ poetry install
```

3. Start the bot!
Note: You need to have the ENV file, which has the Discord Auth Token to start. Ask Hyun for File

```
# start up the bot
$ poetry run task start
```

## Contributing

* ### Always make sure to have your virtual environment active when making/testing changes to ensure our bot is running with only the expected environment settings.

* ### Always make sure to commit your changes to a SEPARATE remote branch (e.g. NO direct commits to `mainline` is allowed)
Refer to this article on creating your own local & remote branch for changes you wish to make
https://stackoverflow.com/questions/1519006/how-do-i-create-a-remote-git-branch

* ### Always make sure that your commits pass all the lint tests (the linting tests will automatically run when you commit)
You can manually run the linting tests by executing the following
```
$ poetry run task lint
```
