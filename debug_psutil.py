import psutil
import os
import sys

print(f"Python version: {sys.version}")
print(f"psutil version: {psutil.__version__}")
print(f"psutil file: {psutil.__file__}")
print(f"sys.path: {sys.path}")

paths_to_test = [
    '/',
    '\\',
    'C:',
    'C:\\',
    'C:/',
    os.path.abspath(os.sep),
    u'C:\\'
]

for p in paths_to_test:
    print(f"\nTesting path: '{p}' (type: {type(p)})")
    try:
        usage = psutil.disk_usage(p)
        print(f"Success: {usage}")
    except Exception as e:
        print(f"Error: {e}")
