import sys
import argparse
import importlib

from pypm.pypm import debug_dump


def parse_args():
    parser = argparse.ArgumentParser('pypm - post_mortem debugging of python dumps using pypm.save_dump')
    parser.add_argument('dump', help='Path to the dump file')
    parser.add_argument('--debugger', default='ipdb', help='Debugger to use (must implement `post_morgem`)')
    return parser.parse_args()

def _debug(debugger, dump_file):
    with debug_dump(dump_file) as tb:
        debugger.post_mortem(tb)

def main():
    args = parse_args()
    debugger = importlib.import_module(args.debugger)
    _debug(debugger, args.dump)

if __name__ == '__main__':
    main()
