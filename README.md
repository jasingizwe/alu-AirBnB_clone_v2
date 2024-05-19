AirBnB clone project

Project description

This project is the initial phase of creating a comprehensive web application, an AirBnB clone. The primary goal of this step is to develop a command interpreter that manages various AirBnB objects. This foundational tool will be essential for subsequent projects involving HTML/CSS templating, database storage, API development, and front-end integration.


This project is the first step in creating a comprehensive web application: an AirBnB clone. The initial focus is on developing a command interpreter to manage AirBnB objects. This command interpreter allows for:

Creation of new objects (e.g., User, State, City, Place)
Retrieval of objects from a file, database, etc.
Performing operations on objects (e.g., counting, computing statistics)
Updating object attributes
Destroying objects
This foundational step is critical for future development, including HTML/CSS templating, database storage, API creation, and front-end integration.

Features

Object Management: Create, read, update, and delete objects.
Storage Engine: File storage for serializing and deserializing instances to and from a JSON file.
Modes: The command interpreter operates in both interactive and non-interactive modes.
Command Interpreter
The command interpreter is implemented using Python's cmd module, providing a REPL environment for interaction.

How to Start

To start the command interpreter in interactive mode, execute:

./console.py

Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

Command	Example
Run the console	./console.py
Quit the console	(hbnb) quit
Display the help for a command	(hbnb) help <command>
Create an object (prints its id)	(hbnb) create <class>
Show an object	(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object	(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects, or all instances of a class	(hbnb) all or (hbnb) all <class>
Update an attribute of an object	(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")
