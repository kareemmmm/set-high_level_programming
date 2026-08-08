#!/usr/bin/python3
"""Reads from standard input and computes log statistics."""
import sys


def print_stats(size, status_codes):
    """Prints accumulated statistics."""
    print("File size: {}".format(size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    file_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(file_size, status_codes)
                line_count = 0

            tokens = line.split()
            try:
                code = int(tokens[-2])
                if code in status_codes:
                    status_codes[code] += 1
            except (IndexError, ValueError):
                pass

            try:
                file_size += int(tokens[-1])
            except (IndexError, ValueError):
                pass

            line_count += 1

        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
