import random
import sys
import timeit

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

# duplicate, not modify original via slice
# drop first one as it is the name of the file
input_number = sys.argv[1]


def get_word_list_1(file_path):
    word_list = open(file_path, 'r').read().split()
    return word_list


def get_word_list_2(file_path):
    word_list = open(file_path, 'r').readlines()
    return word_list


def get_word_list_3(file_path):
    word_list = open(file_path, 'r').read().splitlines()
    return word_list


def generate_sentence(number_of_words, word_list):
    random_word_list = []
    length_of_word_list = len(word_list)

    for i in range(int(number_of_words)):
        random_number = random.randint(0, length_of_word_list)
        random_word = word_list[random_number]
        random_word_list.append(random_word.rstrip())

    return ' '.join(random_word_list)


def generate_sentence_super_optimized(number_of_words):
    f = open('/usr/share/dict/words', 'r')
    print(f)

    random_word_list = {}

    # o(1)
    for i in range(int(number_of_words)):
        # assumes a known length
        random_word_list[random.randint(0, 235886)] = ""

        # o(1)
        highest_line_value = max(random_word_list.keys(), key=int)

        # loop over file up until highest_line_value
        # this becomes highly coupled to reading the file, however
        for line_number, line in enumerate(f):
            for seeked_line_number in random_word_list:
                if line_number == seeked_line_number:
                    # print line
                    random_word_list[line_number] = line.rstrip()

        # print line_number
        # end reading file at highest value
        if line_number == highest_line_value:
            break

        # print random_word_list
        return(' '.join(random_word_list.values()))


if __name__ == '__main__':
    # print(get_word_list_3("/usr/share/dict/words"))
    print(generate_sentence(input_number, get_word_list_2('/usr/share/dict/words')))
    # print generate_sentence_super_optimized(input_number)
    # create a string by joining data from a list by a space
