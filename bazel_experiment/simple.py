import sys

with open(sys.argv[1], "w") as f:
    f.write("Hello World!\n")


with open("bazel_experiment/test.txt") as f:
    print(f.readline())
