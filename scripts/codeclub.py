#!/usr/bin/python
import argparse


class CodeClub:
    def __init__(self):
        parser = argparse.ArgumentParser(description='CodeClub Podcast Tools', usage='''codeclub <command> [<args>]
        Commands:
        next    Return next episode number

        ''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def next():
        parser = argparse.ArgumentParser(
            description='Get Next Episode')
        args = parser.parse_args(sys.argv[2:])
        print 'Running next, amend=%s' % args.amend

if __name__ == '__main__':
    CodeClub()