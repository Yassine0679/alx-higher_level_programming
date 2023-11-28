#!/usr/bin/python3
output = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
file = open(1, 'w')  # 1 refers to stdout
file.write(output)
file.close()

