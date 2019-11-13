To build the project there are two options :

- Build a docker image using Dockerfile. It should be ok but I didn't manage to make it work. 

- recreate the virtual environment venv and import the requirements.txt in the app folder. 

In both cases, if the build is successful run "python main.py" in the app folder to launch the app. running nose2 should launch all the tests.
