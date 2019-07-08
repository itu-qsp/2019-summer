"""
Adapted from: https://wiki.python.org/moin/Powerful%20Python%20One-Liners
"""
import sys


if __name__ == '__main__':
    # Call me from the CLI for example with:
    # echo "My cat looks weirdly. The neighbours cat too..." | python cli_program.py cat dog
    pattern = sys.argv[1]
    substitution = sys.argv[2]

    for line in sys.stdin:
        sys.stdout.write(line.replace(pattern, substitution))
