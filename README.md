# 0x00. AirBnB clone

![AirBnB_clone logo](https://user-images.githubusercontent.com/77997252/233435464-4278c2c9-81cb-43ea-937d-dfd6b81ed2f1.png)

The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://intranet.alxswe.com/rltoken/m8g02HcD2ovrl_K-zulYBw). You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track

**Expected result at end of project looks like this**
![expected result](https://camo.githubusercontent.com/2f3dee607ad33243ded305672c7c7f4b219e7fb59da68dc6a07a54896b217eef/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236382f382d696e6465782e706e67)

## Steps

This application will be build in steps. Each step will link to a concept for modularity and easy work flow
These steps include:

1. **The console**
This will be a simple console in python which will help us to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

- how to start the console `$ ./console.py`
- how to use the console in interavive mode 
```
$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
- how to use the console in non-interavive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
