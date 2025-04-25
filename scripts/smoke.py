import sys
import yyjson

inv = b'["bar\x80"]'.decode('utf8', errors='replace')
outv = yyjson.loads(inv)
exp = ['bar�']

if outv != exp:
    print(f'FAILED: {outv} != {exp}')
    sys.exit(1)

print('SUCCESS!')
sys.exit(0)
