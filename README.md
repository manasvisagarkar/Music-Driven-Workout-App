# Music-Driven-Workout-App
CS 220 Music Driven Workout App Project

Before running anything, make sure you have Python3 installed, the app will use the ```python3``` executables.

Make sure you have VirtualEnv installed - ```sudo pip3 install python-virtualenv```

## Local Setup
```source setup.sh``` to install the necessary dependencies to run the app and tests.

This should probably be run every time you pull from master.

If your script uses a new dependency, please add it to this script. You can view your requirements via a ```pip freeze```

## Testing
Tests will be stored in the "Tests" folder. 

```sh test.sh``` to run all test files locally.

If you create a new test script and would like it to run, please add it to this script.

## Server Setup
The server will build itself and run the unit tests upon a push to the GitHub repository.

For manual setup, ```source setup-server.sh``

## Scripts
Place scripts in the "Scripts" folder, import them where necessary.