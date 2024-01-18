## Build a Command-Line To-Do App With Python and Typer

Building user-friendly command-line interface (CLI) applications is a fundamental skill to have as a Python developer. In the Python ecosystem, you’ll find several tools for creating this kind of application. 
Libraries such as argparse, Click, and Typer are good examples of those tools in Python. Here, you built a CLI application to manage a list of to-dos using Python and Typer.

In this application, you learned how to:

Build a to-do application with Python and Typer
Add commands, arguments, and options to your to-do application using Typer
Test your to-do application using Typer’s CliRunner and pytest in Python

#### Tutorial
To create a Python virtual environment, move to your favorite working directory and create a folder called rptodo_project/. Then fire up a terminal or command line and run the following commands
$ cd todo_project/
$ python -m venv ./venv
$ source venv/bin/activate

Now your users can automatically install the listed dependencies by running the following command:

(venv) $ python -m pip install -r requirements.txt

You’re ready to run your to-do application for the first time.
(venv) $ python -m todo_project -v

 You can run the test with pytest
 (venv) python -m pytest tests/
 
