print("#!/bin/bash")
for i in range(1000):
    print("nc -v 10.133.7.200 445 &")
print("wait")
