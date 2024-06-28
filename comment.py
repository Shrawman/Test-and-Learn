import argparse

if __name__ == "__main__ ":
    parse =argparse.ArgumentParser()
    parse.add_argument("number1", help = "first number")
    parse.add_argument("number1", help = "second number")
    parse.add_argument("operation", help = "operation")

    args= parse.parse_args()
    print(args.numeber1)
    print(args.numeber2)
    print(args.operation)
