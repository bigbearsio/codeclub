#!/usr/bin/python3
import argparse
import sys

from lib import ghost
from lib import podcast

class CodeClub:
    def __init__(self):
        parser = argparse.ArgumentParser(description='CodeClub Podcast Tools', usage='''codeclub <command> [<args>]
        
Commands:
latest    Return latest episode number
links     Return latest episode links

Command Helps:
   ./codeclub.py [command] --help
        ''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        
        getattr(self, args.command)()

    def latest(self):
        parser = argparse.ArgumentParser(
           description='Get Current Episode Number')
        args = parser.parse_args(sys.argv[2:])
        print(ghost.get_latest_episode())

    def links(self):
        parser = argparse.ArgumentParser(description='Get Episode Links')
        parser.add_argument('-l', '--link', help='Get nth link', type=int, default=0)
        args = parser.parse_args(sys.argv[2:])
        

        for (chanel, links) in podcast.latest_episode_links():
            print("{:7}  ::  {}".format(chanel, links[args.link]))


if __name__ == '__main__':
    CodeClub()