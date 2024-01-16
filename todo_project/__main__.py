""" To Do app entry script. """

from todo_project import  cli, __app_name__

def main():
    cli.app(prog_name= __app_name__)

if __name__ == "__main__":
    main()

