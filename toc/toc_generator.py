import sys
import os

# First arg is an output file, the rest of the args are input files. Generates a toc
# at output for all the markdown files in the input set, assuming the first heading is
# the document title.


def main():
    output_file = sys.argv[1]
    with open(output_file, "w") as out:
        for file in sys.argv[2:]:
            pre, ext = os.path.splitext(os.path.basename(file))
            html_path = pre + ".html"
            with open(file) as f:
                lines = f.read().splitlines()
            for line in lines:
                if line.startswith("# "):
                    title = line[2:]
                    out.write(f"1. [{title}]({html_path})\n")
                    break


if __name__ == "__main__":
    main()
