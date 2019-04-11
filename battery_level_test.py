#!/usr/bin/env python3
"""`cat` for Python 3.
 - if a file has no newline at the end then the last line is merged
   with the first line of the next file like `cat` does
 - os.fsencode() is not used to encode error message therefore there
   could be surrogates in the output (encoded using the default for
   errors 'backslashreplace' error handler): it is always possible to
   restore the original filename whatever (ascii-based) locale
   settings are
 - line separator is always b'\n' regardless of the platform
"""
import fileinput
import os
import sys

def progname():
    """Get program name."""
    # NOTE: to follow symlinks, os.path.realpath() could be used
    return os.path.basename(sys.argv[0]) or 'cat.py'


if sys.version_info[:3] < (3, 4, 1): # see http://bugs.python.org/issue21075
    sys.stdin = sys.stdin.detach() # use binary mode for files
# XXX Is it necessary to call:
#    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
#  on Windows (to avoid b'\n' -> b'\r\n')?
output_file = sys.stdout = sys.stdout.detach()
input_file = fileinput.input(mode='rb')
while True:
    try:
        line = input_file.readline()
    except OSError as e:
        print('{}: error: {}'.format(progname(), e), file=sys.stderr)
        # # `cat`-like error message (ignore locales):
        # sys.stderr.buffer.write(os.fsencode(progname()) + b': ' +
        #                         os.fsencode(e.filename) + b': ' +
        #                         e.strerror.encode() + b'\n')
    else:
        if not line:
            break
        output_file.write(line)
