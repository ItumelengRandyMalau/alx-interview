#!/usr/bin/python3

"""
A script that reads stdin line by line and computes metrics.
"""

import sys


def print_stats(status_counts: dict, file_size: int) -> None:
    """Prints the statistics including file size and status counts.

    Args:
        status_counts (dict): Dictionary with status codes as keys,
        and counts as values.
        file_size (int): Total size of the file in bytes.
    """
    print("File size: {}".format(file_size))
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def print_logs() -> None:
    """Reads logs from standard input and generates reports.

    Reports:
        -Prints log size after reading every 10 lines and at KeyboardInterrupt.
    """
    stdin = sys.stdin
    line_read = 0
    total_size = 0
    status_counts = {}

    for line in stdin:
        line = line.strip()
        if not line:
            continue

        try:
            parts = line.split()
            size = int(parts[-1])
            status = parts[-2]

            total_size += size
            status_counts[status] = status_counts.get(status, 0) + 1

            line_read += 1
            if line_read % 10 == 0:
                print_stats(status_counts, total_size)

        except (IndexError, ValueError):
            continue

    print_stats(status_counts, total_size)
