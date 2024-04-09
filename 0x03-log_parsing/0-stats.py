#!/usr/bin/python3
"""
Log parsing: Parses log data from stdin and computes statistics.
"""

import sys

if __name__ == "__main__":
    # Initialize variables
    total_filesize, line_count = 0, 0
    # Define status codes to track
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Initialize dictionary to store status code frequencies
    status_code_counts = {code: 0 for code in status_codes}

    def print_stats(status_code_counts: dict, file_size: int) -> None:
        print("File size: {:d}".format(total_filesize))
        for k, v in sorted(status_code_counts.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except BaseException:
                pass
            try:
                total_filesize += int(data[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_stats(status_code_counts, total_filesize)
        print_stats(status_code_counts, total_filesize)
    except KeyboardInterrupt:
        print_stats(status_code_counts, total_filesize)
        raise
