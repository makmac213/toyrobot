Installation
------------
Script was created using Python 3.9.6

#### Using Virtualenv
If you want to run this simple script in its own virtual environment follow the following step.

```bash
pip3 install -r requirements.txt
```

Install Flake8 (optional)
```bash
python -m pip install flake8
```

#### Using Docker
Ensure you have Docker installed in your machine.

[Get Started with Docker](https://www.docker.com/get-started/)

Once you are all setup run the following command.

```bash
docker-compose up --build
```

Use docker exec command to run the script. Run the following command to get your app's container ID.

```bash
docker ps
```

Then run a shell in your container by doing:
```bash
docker exec -it your_container_id /bin/bash
```

Run the script
--------------

```bash
python3 main.py
```


Run tests
---------

```bash
python3 -m pytest
```


Run Flake8 (optional)
---------------------

Flake8: Your Tool For Style Guide Enforcement

https://flake8.pycqa.org/en/latest/#

```bash
flake8
```

Example Input and Output:
-------------------------

```
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
```


```
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST
```


```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
```

Added EXIT command to terminate the script.
