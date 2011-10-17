################################################################################
# Ryan James
#
# Complexity Sciences Center
# Department of Physics
# UC Davis
#
# codepadr/cli.py

"""
codepadr
========

codepadr uploads pastes to codepad.org.
"""

import sys

import argparse

import requests


FILE_TYPES = {'c': 'C',
              'cpp': 'C++',
              'd': 'D',
              'hs': 'Haskell',
              'lua': 'Lua',
              'ml': 'OCaml',
              'php': 'PHP',
              'pl': 'Perl',
              'txt': 'Plain Text',
              'py': 'Python',
              'rb': 'Ruby',
              'scm': 'Scheme',
              'tcl': 'Tcl',}

DEFAULT_TYPE = FILE_TYPES['txt']


def get_args():
    """
    Define & grab the arguments using argparse.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lang', dest='lang', help="Set the language of the paste. The option is only relavent for pastes input on stdin.", choices=FILE_TYPES.keys(), default='txt')
    parser.add_argument('-p', '--private', dest='private', action='store_true', help="Set the paste as private.")
    parser.add_argument('-r', '--run', dest='run', action='store_true', help="Set the paste to be run.")
    parser.add_argument('code', nargs='*', help="The file(s) to be uploaded")
    return parser.parse_args()

def upload_paste(code="", lang="Plain Text", private=False, run=False):
    """
    Upload code to codepad.org, setting the appropriate flags.

    Arguments
    ---------
    code: string
        The body of the paste.

    lang: string
        The language of the paste. Used for syntax highlighting and when running
        the code.

    private: bool
        Whether the paste should be private or not.

    run: bool
        Whether the paste should be executed or not.
    """
    data = {'code': code,
            'lang': lang,
            'private': private,
            'run': run,
            'submit': 'Submit'}
    request = requests.post("http://codepad.org/", data=data)
    if request.ok:
        return request.url
    else:
        return "Code could not be uploaded."

def process_file(source, args):
    """
    Process a data source (file or stdin) before uploading it.

    Arguments
    ---------
    source: string, stdin
        Either a file name or stdin. The source of the body of the paste.

    args: ArgumentParser
        argparse's parsed arguments, or a similar objected.
    """
    if source is sys.stdin:
        content = source.read()
        file_type = FILE_TYPES[args.lang]
    else:
        with open(source) as data:
            content = data.read()
        file_ext = source.split('.')[-1]
        file_type = FILE_TYPES.get(file_ext, DEFAULT_TYPE)

    private = args.private
    run = args.run

    return upload_paste(content, file_type, private, run)

def main():
    """
    Reads in the arguments and dispatches to process_file.
    """
    args = get_args()
    if args.code and args.code != ['-']:
        for source in args.code:
            print process_file(source, args)
    else:
        print process_file(sys.stdin, args)

if __name__ == '__main__':
    main()
