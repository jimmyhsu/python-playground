import random


# A histogram() function which takes a source_text argument (can be either a filename or the contents of file as a string, your choice),
# and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
def get_text_list(file_path):
    """

    """
    file = open(file_path, 'r')
    word_list = file.read().split()

    return word_list


def histogram_dictionary(word_list):
    histogram = {}
    for word in word_list:
        if histogram.get(word.lower()) is None:
            histogram[word.lower()] = 1
        else:
            histogram[word.lower()] += 1

    return histogram


# A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram.
# For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.
def unique_words(histogram):
    return len(histogram.keys())


# A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text.
# For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
def frequency(word, histogram):
    return histogram[word]


def get_random_word_flat(histogram):
    words = histogram.keys()
    random_index = random.randint(0, len(words)-1)
    return words[random_index]


def create_probability_index(histogram):
    probability_index = []
    count = 0
    for word, frequency in histogram.iteritems():
        count += frequency
        probability_index.append((word, count))

    return probability_index


def get_random_word_by_frequency(histogram):
    probability_index = create_probability_index(histogram)

    # get a random number based off last item in probability_index
    # print random.randint(0, probability_index[len(probability_index)-1][1])
    last_number = probability_index[len(probability_index)-1][1]
    random_number = random.randint(1, last_number)
    previous_number = 0
    for i in range(0, len(probability_index)):
        # print "Previous Number:"
        # print previous_number
        # print "Current Number:"
        # print probability_index[i][1]
        # print "Rand:"
        # print random_number
        # print "True?:"
        # print previous_number > random_number and
        # probability_index[i][1] < random_number
        # print "----"

        # check if it is greater than the previous tuple number, yet smaller or equal than the current tuple number
        if previous_number < random_number and probability_index[i][1] >= random_number:
            return probability_index[i][0]
        previous_number = probability_index[i][1]


def random_word_frequency_checker(histogram):
    result = {}
    for key in histogram.keys():
        result[key] = 0

    for x in range(0, 1000000):
        result[get_random_word_by_frequency(histogram)] += 1

    return result


if __name__ == '__main__':
    # print get_text_list('life_is_short.txt')
    # create a string by joining data from a list by a space
    # print histogram_dictionary(get_text_list('life_is_short.txt'))
    test_hist = histogram_dictionary(get_text_list('markov/corpus/combined.txt'))
    # test_hist = histogram_dictionary(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
    print(test_hist)
    # print(unique_words(test_hist))
    # print frequency('one', test_hist)
    # print get_random_word_flat(test_hist)
    # print get_random_word_by_frequency(test_hist)
    # print get_random_word_by_frequency(test_hist)
    # print(random_word_frequency_checker(test_hist))
