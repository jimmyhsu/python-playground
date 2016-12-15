import random
import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

# duplicate, not modify original via slice
# drop first one as it is the name of the file
input_data = sys.argv[1:]


def randomize_input():
    # random.shuffle modifies input argument
    random.shuffle(input_data)


if __name__ == '__main__':
    randomize_input()
    # create a string by joining data from a list by a space
    print(' '.join(input_data))
