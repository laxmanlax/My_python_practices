import subprocess
import os

def execute_commands(cmd):
    try:
        subprocess.run(cmd.split())
    except Exception:
        print "Command not found {}".format(cmd)
        

def psh_cd(path):
    """convert to absolute path and change directory"""
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print "cd: no such file or directory: {}".format(path)

def main():
    while True:
        command = raw_input("$ ")
        if command == "exit":
            break
        elif command == "help":
            print("psh: a simple shell written in Python")
        elif command[:3] == "cd ":
            psh_cd(command[:3])
        elif command[0] == "mkdir":
            os.mkdir(command[1])
        else:
            execute_commands(command)


if __name__ == '__main__':
    main()
