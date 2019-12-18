import subprocess
import os
def execute_commands(command):
    try:
        if "|" in command:
            s_in, s_out = (0,0)

            s_in = os.dup(0)
            s_out = os.dup(1)

            fdin = os.dup(s_in)

            for cmd in command.split():
                os.dup2(fdin, 0)
                os.close(fdin)

                if cmd == command.split("|"):
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()




def main():
    while True:
        command = raw_input("$ ")
        #print command
        cmd = command.split()
        if cmd[0] == "exit":
            break
        elif cmd[0] == "mkdir":
            psh_mkdir()
        elif cmd[0] == "cd":
            psh_cd()
        elif cmd[0] == "history":
            phs_history()
        elif cmd[0] == "ls":
            phs_ls()
        else:
            execute_commands(command)


if __name__ == '__main__':
    main()
