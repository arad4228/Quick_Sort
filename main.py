import sys
import psutil
import pandas as pd
import numpy as np


def usage():
    print("./QuicSort [Options] ")
    print("Option: S -> Order Random Number CSV")
    print("Option: R -> ReverseOrder Random Number CSV")

def make_CSV_File(options):
    df = pd.DataFrame(
        np.random.randint(0, 2147483647, size=1000000)
    )

    if options == "S":
        df.sort_values(0)
    elif options == "R":
        df.sort_values(0, ascending=False)

    df.to_csv('./GenerateNumbers.csv', index=False)
    return True


if __name__ == "__main__":
    if len(sys.argv) < 1:
        usage()
    option = sys.argv[1]
    make_CSV_File(option)

