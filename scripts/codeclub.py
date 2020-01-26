#!/usr/bin/python3
import argparse
import sys

from lib import ghost

class CodeClub:
    def __init__(self):
        parser = argparse.ArgumentParser(description='CodeClub Podcast Tools', usage='''codeclub <command> [<args>]
        
Commands:
latest    Return latest episode number
        ''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        
        getattr(self, args.command)()

    def latest(self):
        #parser = argparse.ArgumentParser(
        #    description='Get Current Episode')
        #args = parser.parse_args(sys.argv[2:])
        print(ghost.get_latest_episode())

if __name__ == '__main__':
    CodeClub()