# Jokenpo with Tests

## About 

This project uses a Jokenpo Python script to test automated testing using GitHub Actions. 

### Test Pipeline 

First the test_game.py test are excecuted, then we test the code style using flake8 and finally using mypy we check the typing of all the source files. All of these steps are executed in Windows, Mac and Ubuntu latest version to check if the script is cross-platform compatible.

### Installing

Use the following commands to create a virtual environment on your Mac/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

To install the dependencies of the project, use this command:

```
python3 -m pip install -r requirements.txt
```

To play the game run the src/game/main.py file.

```
python src/game/main.py
```

### Running tests locally

After installing all the dependencies just use this command:

```
tox
```
