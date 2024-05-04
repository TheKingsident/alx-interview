#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys
import re


status_code_count = {}
total_file_size = 0
lines_count = 0
regex = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] ' \
        r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'

try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(regex, line)

        if not match:
            continue

        ip_address, date, status_code, file_size = match.groups()

        status_code = int(status_code)
        file_size = int(file_size)

        total_file_size += file_size
        lines_count += 1

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_code_count[status_code] = status_code_count.get(
                status_code, 0) + 1

        if lines_count % 10 == 0:
            print("File size:", total_file_size)
            for code in sorted(status_code_count.keys()):
                print(f"{code}: {status_code_count[code]}")

    print("File size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    print("File size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")
