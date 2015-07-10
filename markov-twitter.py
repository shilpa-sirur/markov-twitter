import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        # Get the name of the log file to open from the command line

        # list_filenames = open(filenames)
        all_word_list = []
        for f in filenames:
        # Read each line from the log file and process it
            filename = open(f)
            for line in filename:
                # Each line should be in the format:
                seperate_words = line.rstrip().split(" ") 
                all_word_list.extend(seperate_words)
        # print all_word_list
        return all_word_list

    def make_chains(self, all_word_list):
        """Takes input text as string; stores chains."""
        bigram_dict = {}        
        for i in range(len(all_word_list)-2):
            bigram = (all_word_list[i], all_word_list[i+1])
            value_word = all_word_list[i+2]

            if bigram not in bigram_dict:
                bigram_dict[bigram] = []
            bigram_dict[bigram].append(value_word)
        # print bigram_dict
        return bigram_dict

    def make_text(self, bigram_dict):
        """Takes dictionary of markov chains; returns random text."""
        random_key1 = choice(bigram_dict.keys())
        random_value = choice(bigram_dict[random_key1])
        random_text = str(random_key1[0] + " " + random_key1[1]) + " " + str(random_value)
        new_key1 = (random_key1[1], random_value)
        # print new_key1
        while new_key1 in bigram_dict: 
            # This will select second word of key pair and combine it with value to create new key
            new_value1 = choice(bigram_dict[new_key1])
            new_key1 = (new_key1[1], new_value1)
            random_text = random_text + " " + new_value1
        return random_text[:550]

       


if __name__ == "__main__":

    # we should get list of filenames from sys.argv

    filenames = sys.argv[1:]
    # we should make an instance of class SimpleMarkovGenerator
    w = SimpleMarkovGenerator()

    # we should call the read_files method with the list of filenames
    u = w.read_files(filenames)

    z = w.make_chains(u)

    # we should call the make_text method 5x
   
    print  w.make_text(z)

    pass
